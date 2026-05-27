#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_gb_aus_vorlage.py – STAPCON-Gefährdungsbeurteilung aus externer Vorlage befüllen.

Verwendet eine bestehende DOCX-Vorlage und eine JSON-Datei und erzeugt daraus
eine fertig ausgefüllte Gefährdungsbeurteilung.

Verwendung:
    python3 04_gb_aus_vorlage.py --template GB_Vorlage.docx --json meine_gb.json
    python3 04_gb_aus_vorlage.py --template GB_Vorlage.docx --json meine_gb.json --output Ergebnis.docx
    python3 04_gb_aus_vorlage.py --template GB_Vorlage.docx --example-json beispiel.json

Argumente:
    --template / -t   Pfad zur leeren DOCX-Vorlage (Pflicht)
    --json    / -j    Pfad zur JSON-Datei (fehlt → Dateiauswahl-Dialog)
    --output  / -o    Ausgabepfad (Standard: JSON-Dateiname + _GB.docx)
    --no-password     Kein Schreibschutz
    --password        Schutzpasswort (Standard: holiday)
    --example-json    Speichert ein Beispiel-JSON unter dem angegebenen Pfad

JSON-Schema (vereinheitlicht, flach):
{
  "titel":                    "Bezeichnung des Arbeitssystems",
  "firma":                    "Musterwerk GmbH",
  "betriebsort":              "Musterstadt",
  "taetigkeit":               "Maschinenbedienung XY-200",
  "arbeitsbereich":           "Produktion Halle 3",
  "taetigkeitsbeschreibung":  "Fließtext (\\n = Absatzumbruch)",
  "maschinendaten":           "Hersteller | Typ | Bj. | Nr.",
  "eintraege": [
    {
      "nr":          "1.1",
      "gefaehrdung": "Beschreibung der Gefährdung",
      "zustand":     "N",
      "datum":       "[# Datum]",
      "risiko":      5,
      "restrisiko":  3,
      "massnahmen": [
        {
          "massnahme":   "...",
          "typ":         "T",
          "zustaendig":  "[# verantw. FK]",
          "termin":      "[# kurzfristig]",
          "verweis":     "BetrSichV § 6",
          "status":      "offen",
          "wirksamkeit": 2
        }
      ]
    }
  ]
}

Hinweise:
  - Rückwärtskompatibel: altes Schema mit "meta": {...} wird automatisch abgeflacht.
  - Restrisiko-Logik: wirksamkeit (pro Maßnahme) hat Vorrang vor restrisiko (pro Eintrag).
    restrisiko füllt nur die erste Maßnahmenzeile (Fallback).
    wirksamkeit füllt die jeweilige Maßnahmenzeile (höchste Priorität).
  - status: unterstützt Symbole (○◔◑◕●) direkt und Text ("offen"/"erledigt").
  - Wirksamkeit (Spalte 17) bleibt immer leer (reserviert).
  - Passwort für Schreibschutz: "holiday"
"""

import argparse
import copy
import json
import os
import shutil
import sys
import tempfile
import zipfile
from datetime import datetime
from lxml import etree

# → gemeinsame Logik aus stapcon_kern
from stapcon_kern import (
    w,
    FARBE_GRUEN, FARBE_GELB, FARBE_ROT, FARBE_WEISS,
    SPALTE_NR, SPALTE_GEF, SPALTE_NORMAL, SPALTE_BESONDERS, SPALTE_DATUM,
    SPALTE_K, SPALTE_M, SPALTE_H,
    SPALTE_MASSNAHME, SPALTE_S, SPALTE_T, SPALTE_O, SPALTE_P,
    SPALTE_ZUST, SPALTE_TERMIN, SPALTE_VERWEIS, SPALTE_STATUS, SPALTE_WIRK,
    SPALTE_RR_K, SPALTE_RR_M, SPALTE_RR_H,
    status_symbol, risiko_spalten,
    schattierung_setzen, vmerge_setzen, rahmen_anwenden,
    absatz_erstellen, zelle_beschriften,
    tcpr_sicherstellen,
    dokumentschutz_setzen,
)

# ── Kategorie-Labels ──────────────────────────────────────────────────────────
# ERWEITERBAR: Weitere Gefährdungskategorien hier als {int: "Label"} ergänzen.

KATEGORIE_LABELS = {
    1:  "1. Mechanische Gefährdungen",
    2:  "2. Elektrische Gefährdungen",
    3:  "3. Gefahrstoffe",
    4:  "4. Biologische Arbeitsstoffe",
    5:  "5. Brand- & Explosionsgefährdung",
    6:  "6. Gefährdungen durch spezielle physikalische Einwirkungen/ Arbeitsumgebungsbedingungen",
    7:  "7. Gefährdungen durch Arbeitsplatzgestaltung",
    8:  "8. Gefährdung durch ergonomische Faktoren/ Physische Belastungen / Arbeitsschwere",
    9:  "9. Psychische Belastungen",
    10: "10. Grundlegende organisatorische Faktoren",
    11: "11. Sonstige Gefährdungs- und Belastungsfaktoren",
}

# ── XML-Hilfsfunktionen (lokal) ───────────────────────────────────────────────

def _kategorie_nummer(nr_str: str) -> int:
    """Extrahiert die Kategorie-Nummer aus einer Gf-Nr. wie '1.1' → 1."""
    try:
        return int(str(nr_str).split(".")[0])
    except (ValueError, IndexError):
        return 11


def _zellen_text_lesen(zelle) -> str:
    """Liest den sichtbaren Text einer Zelle (alle w:t-Texte zusammengesetzt)."""
    return "".join(t.text or "" for t in zelle.findall(f".//{w('t')}"))


def _absatz_erzeugen(text="", schriftgroesse=16, fett=False, ausrichtung=None):
    """Erzeugt einen einfachen w:p mit Arial-Schrift und optionaler Ausrichtung.

    Identisch zu absatz_erstellen() im Kern, aber mit lokalem spacing (before/after 60).
    → siehe auch stapcon_kern.absatz_erstellen()
    """
    p = etree.Element(w("p"))
    pPr = etree.SubElement(p, w("pPr"))
    sp = etree.SubElement(pPr, w("spacing"))
    sp.set(w("before"), "60")
    sp.set(w("after"), "60")
    if ausrichtung:
        etree.SubElement(pPr, w("jc")).set(w("val"), ausrichtung)
    # rPr im pPr (Absatzformatierung)
    rPr_ppr = etree.SubElement(pPr, w("rPr"))
    rf = etree.SubElement(rPr_ppr, w("rFonts"))
    for a in ("ascii", "hAnsi", "cs"):
        rf.set(w(a), "Arial")
    etree.SubElement(rPr_ppr, w("sz")).set(w("val"), str(schriftgroesse))
    etree.SubElement(rPr_ppr, w("szCs")).set(w("val"), str(schriftgroesse))
    if fett:
        etree.SubElement(rPr_ppr, w("b"))
        etree.SubElement(rPr_ppr, w("bCs"))
    # r>rPr (Laufformatierung)
    r = etree.SubElement(p, w("r"))
    rPr_r = etree.SubElement(r, w("rPr"))
    rf2 = etree.SubElement(rPr_r, w("rFonts"))
    for a in ("ascii", "hAnsi", "cs"):
        rf2.set(w(a), "Arial")
    etree.SubElement(rPr_r, w("sz")).set(w("val"), str(schriftgroesse))
    etree.SubElement(rPr_r, w("szCs")).set(w("val"), str(schriftgroesse))
    if fett:
        etree.SubElement(rPr_r, w("b"))
        etree.SubElement(rPr_r, w("bCs"))
    t = etree.SubElement(r, w("t"))
    if text and (text.startswith(" ") or text.endswith(" ")):
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text or ""
    return p


def _zelle_schreiben(zelle, text: str, zentriert=False, mehrzeilig=False, fett=False):
    """Ersetzt Zellen-Inhalt mit neuem Text-Absatz.

    → siehe auch stapcon_kern.zelle_beschriften()
    Lokale Variante mit 16pt-Schriftgröße (Vorlage-Standard).
    """
    for p in list(zelle.findall(w("p"))):
        zelle.remove(p)
    ausrichtung = "center" if zentriert else None
    if mehrzeilig and text and "\n" in text:
        for zeile in text.split("\n"):
            zelle.append(_absatz_erzeugen(zeile, ausrichtung=ausrichtung, fett=fett))
    else:
        zelle.append(_absatz_erzeugen(text or "", ausrichtung=ausrichtung, fett=fett))


def _continue_zelle_leeren(zelle):
    """Leert eine vMerge-continue-Zelle (Pflicht-Leerabsatz bleibt erhalten)."""
    for p in list(zelle.findall(w("p"))):
        zelle.remove(p)
    zelle.append(_absatz_erzeugen(""))


def _rahmen_setzen_einfach(zelle, seite, staerke="12"):
    """Setzt einen einzelnen Rahmen auf eine Zelle.

    → siehe auch stapcon_kern.rahmen_setzen()
    """
    rahmen_anwenden(zelle, {seite: ("single", staerke, "000000")})


def _rahmen_loeschen(zelle, seite):
    """Entfernt einen Rahmen (setzt ihn auf 'nil')."""
    rahmen_anwenden(zelle, {seite: ("nil", "0", "auto")})


# ── Kopfzeilen-Patches ────────────────────────────────────────────────────────

def _hauptkopf_rahmen_patchen(zeile):
    """Patcht Rahmen der 13-spaltig Hauptkopfzeile.

    Gruppen-Zellen (Zustand, Risiko, Typ, Restrisiko) erhalten unteren 0,5pt-Rahmen,
    alle anderen keinen unteren Rahmen.
    """
    HALB = ("single", "4", "000000")
    NIL  = ("nil",    "0", "auto")

    def _normalisieren(s):
        return s.lower().replace("-", "").replace(" ", "").replace("\n", "")

    GRUPPEN = {"zustand", "risiko", "typ", "restrisiko"}
    zellen = zeile.findall(w("tc"))
    for zelle in zellen:
        text_norm = _normalisieren(_zellen_text_lesen(zelle))
        ist_gruppe = any(g in text_norm for g in GRUPPEN)
        rahmen_anwenden(zelle, {"bottom": HALB if ist_gruppe else NIL})


def _subkopf_zeile_patchen(zeile):
    """Patcht die 21-spaltige Sub-Kopfzeile (N/B, K/M/H, S/T/O/P, K/M/H).

    Gruppen-Zellen: oben + unten 0,5pt; Nicht-Gruppen: oben nil, unten 1,5pt.
    """
    # ERWEITERBAR: Weitere farbige Spalten in COLOR_MAP ergänzen.
    COLOR_MAP    = {5: FARBE_GRUEN, 6: FARBE_GELB, 7: FARBE_ROT,
                    18: FARBE_GRUEN, 19: FARBE_GELB, 20: FARBE_ROT}
    GRUPPEN_IDX  = {2, 3, 5, 6, 7, 9, 10, 11, 12, 18, 19, 20}
    HALB  = ("single", "4",  "000000")
    DICK  = ("single", "12", "000000")
    NIL   = ("nil",    "0",  "auto")

    zellen = zeile.findall(w("tc"))
    for i, zelle in enumerate(zellen):
        if i in COLOR_MAP:
            schattierung_setzen(zelle, COLOR_MAP[i])
        if i in GRUPPEN_IDX:
            rahmen_anwenden(zelle, {"top": HALB, "bottom": HALB})
        else:
            rahmen_anwenden(zelle, {"top": NIL, "bottom": DICK})


def _subkopf_zeile_erzeugen(vorlage_zeile):
    """Erzeugt die zweite Kopfzeile mit Labels N/B, K/M/H, S/T/O/P, K/M/H."""
    zeile = copy.deepcopy(vorlage_zeile)
    zellen = zeile.findall(w("tc"))

    labels = ["", "", "N", "B", "",  "K", "M", "H",
              "", "S", "T", "O", "P", "", "", "", "", "",
              "K", "M", "H"]
    farben = {5: FARBE_GRUEN, 6: FARBE_GELB, 7: FARBE_ROT,
              18: FARBE_GRUEN, 19: FARBE_GELB, 20: FARBE_ROT}
    GRUPPEN_IDX = {2, 3, 5, 6, 7, 9, 10, 11, 12, 18, 19, 20}
    HALB = ("single", "4",  "000000")
    DICK = ("single", "12", "000000")
    NIL  = ("nil",    "0",  "auto")

    for i, zelle in enumerate(zellen):
        vmerge_setzen(zelle, None)
        lbl = labels[i] if i < len(labels) else ""
        _zelle_schreiben(zelle, lbl, zentriert=True, fett=bool(lbl))
        schattierung_setzen(zelle, farben.get(i))
        if i in GRUPPEN_IDX:
            rahmen_anwenden(zelle, {
                "top":    HALB,
                "left":   HALB,
                "right":  HALB,
                "bottom": DICK,
            })
        else:
            rahmen_anwenden(zelle, {"top": NIL, "bottom": DICK})

    return zeile


# ── Maßnahmen-Zeilen-Builder ──────────────────────────────────────────────────

def _massnahme_spalten_fuellen(zellen, massnahme: dict,
                               rr_k, rr_m, rr_h, rr_kf, rr_mf, rr_hf):
    """Füllt Spalten 8-20 mit Maßnahmen-Daten.

    rr_k/m/h:  Restrisiko-Texte für Spalten 18-20
    rr_kf/mf/hf: Restrisiko-Farben
    Spalte 17 (Wirksamkeit) bleibt immer leer.
    """
    typ = str(massnahme.get("typ", "")).upper()

    _zelle_schreiben(zellen[SPALTE_MASSNAHME], str(massnahme.get("massnahme", "")))
    _zelle_schreiben(zellen[SPALTE_S], "X" if typ == "S" else "", zentriert=True)
    _zelle_schreiben(zellen[SPALTE_T], "X" if typ == "T" else "", zentriert=True)
    _zelle_schreiben(zellen[SPALTE_O], "X" if typ == "O" else "", zentriert=True)
    _zelle_schreiben(zellen[SPALTE_P], "X" if typ == "P" else "", zentriert=True)
    _zelle_schreiben(zellen[SPALTE_ZUST],   str(massnahme.get("zustaendig", "")))
    _zelle_schreiben(zellen[SPALTE_TERMIN], str(massnahme.get("termin",     "")))
    _zelle_schreiben(zellen[SPALTE_VERWEIS], str(massnahme.get("verweis",   "")), mehrzeilig=True)
    _zelle_schreiben(zellen[SPALTE_STATUS],
                     status_symbol(str(massnahme.get("status", "offen"))),
                     zentriert=True)
    _zelle_schreiben(zellen[SPALTE_WIRK], "")              # Wirksamkeit immer leer
    _zelle_schreiben(zellen[SPALTE_RR_K], rr_k, zentriert=True)
    _zelle_schreiben(zellen[SPALTE_RR_M], rr_m, zentriert=True)
    _zelle_schreiben(zellen[SPALTE_RR_H], rr_h, zentriert=True)
    schattierung_setzen(zellen[SPALTE_RR_K], rr_kf)
    schattierung_setzen(zellen[SPALTE_RR_M], rr_mf)
    schattierung_setzen(zellen[SPALTE_RR_H], rr_hf)


def _restrisiko_fuer_massnahme(massnahme: dict, rr_eintrag_tuple: tuple) -> tuple:
    """Bestimmt Restrisiko-Spalten für eine einzelne Maßnahme.

    Priorität: wirksamkeit (pro Maßnahme) > restrisiko (pro Eintrag).
    rr_eintrag_tuple: Ergebnis von risiko_spalten(entry["restrisiko"]).
    """
    wirksamkeit = massnahme.get("wirksamkeit")
    if wirksamkeit is not None:
        # Maßnahmen-eigene Wirksamkeit hat Vorrang
        return risiko_spalten(wirksamkeit)
    return rr_eintrag_tuple


def startzeile_bauen(vorlage_restart, vorlage_continue, eintrag: dict,
                     massnahme: dict,
                     rr_k, rr_m, rr_h, rr_kf, rr_mf, rr_hf,
                     k_text, m_text, h_text, k_farbe, m_farbe, h_farbe):
    """Baut die erste Zeile eines Eintrags (vMerge restart) mit allen Gefährdungsdaten."""
    zeile = copy.deepcopy(vorlage_restart)
    zellen = zeile.findall(w("tc"))

    # Spalten 0-7: vMerge restart + Gefährdungsdaten
    for i in range(8):
        vmerge_setzen(zellen[i], "restart")

    zustand = str(eintrag.get("zustand", "N")).upper()

    _zelle_schreiben(zellen[SPALTE_NR],         str(eintrag.get("nr",          "")), zentriert=True)
    _zelle_schreiben(zellen[SPALTE_GEF],         str(eintrag.get("gefaehrdung", "")))
    _zelle_schreiben(zellen[SPALTE_NORMAL],   "X" if zustand == "N" else "", zentriert=True)
    _zelle_schreiben(zellen[SPALTE_BESONDERS],"X" if zustand == "B" else "", zentriert=True)
    _zelle_schreiben(zellen[SPALTE_DATUM],       str(eintrag.get("datum",        "")), zentriert=True)
    _zelle_schreiben(zellen[SPALTE_K], k_text, zentriert=True)
    _zelle_schreiben(zellen[SPALTE_M], m_text, zentriert=True)
    _zelle_schreiben(zellen[SPALTE_H], h_text, zentriert=True)
    schattierung_setzen(zellen[SPALTE_K], k_farbe)
    schattierung_setzen(zellen[SPALTE_M], m_farbe)
    schattierung_setzen(zellen[SPALTE_H], h_farbe)

    # Spalten 8-20: Maßnahme
    _massnahme_spalten_fuellen(zellen, massnahme, rr_k, rr_m, rr_h, rr_kf, rr_mf, rr_hf)

    return zeile


def folgezeile_bauen(vorlage_continue, massnahme: dict,
                     rr_k, rr_m, rr_h, rr_kf, rr_mf, rr_hf,
                     k_farbe, m_farbe, h_farbe):
    """Baut eine Folgezeile (vMerge continue) für weitere Maßnahmen desselben Eintrags."""
    zeile = copy.deepcopy(vorlage_continue)
    zellen = zeile.findall(w("tc"))

    # Spalten 0-7: vMerge continue (Pflicht-Leerabsatz, Farben beibehalten)
    for i in range(8):
        vmerge_setzen(zellen[i], "continue")
        _continue_zelle_leeren(zellen[i])

    schattierung_setzen(zellen[SPALTE_K], k_farbe)
    schattierung_setzen(zellen[SPALTE_M], m_farbe)
    schattierung_setzen(zellen[SPALTE_H], h_farbe)

    # Spalten 8-20: Maßnahme
    _massnahme_spalten_fuellen(zellen, massnahme, rr_k, rr_m, rr_h, rr_kf, rr_mf, rr_hf)

    return zeile


def eintragszeilen_erzeugen(vorlage_restart, vorlage_continue, eintrag: dict) -> list:
    """Erzeugt alle Tabellenzeilen für einen Gefährdungseintrag.

    Gibt eine Liste von w:tr-Elementen zurück (1 restart + n continues).
    Restrisiko-Logik: wirksamkeit (pro Maßnahme) überschreibt restrisiko (pro Eintrag).
    restrisiko (Eintrag) füllt nur die erste Maßnahmenzeile als Fallback.
    """
    massnahmen = eintrag.get("massnahmen", [])
    if not massnahmen:
        massnahmen = [{"massnahme": "", "typ": "O",
                       "zustaendig": "", "termin": "",
                       "verweis": "", "status": "offen"}]

    # Risiko-Spalten des Eintrags (Spalten 5-7)
    k_t, m_t, h_t, k_f, m_f, h_f = risiko_spalten(eintrag.get("risiko"))

    # Restrisiko des Eintrags als Standard-Fallback (Spalten 18-20, erste Zeile)
    rr_eintrag = risiko_spalten(eintrag.get("restrisiko"))

    zeilen = []

    # ── Erste Zeile (restart) ─────────────────────────────────────────
    # Wirksamkeit der ersten Maßnahme hat Vorrang vor restrisiko des Eintrags
    rr_0 = _restrisiko_fuer_massnahme(massnahmen[0], rr_eintrag)
    zeilen.append(startzeile_bauen(
        vorlage_restart, vorlage_continue, eintrag, massnahmen[0],
        *rr_0,
        k_t, m_t, h_t, k_f, m_f, h_f,
    ))

    # ── Folgezeilen (continue) ────────────────────────────────────────
    for massnahme in massnahmen[1:]:
        # Jede Folgezeile: wirksamkeit der Maßnahme; restrisiko des Eintrags als Fallback
        rr = _restrisiko_fuer_massnahme(massnahme, rr_eintrag)
        zeilen.append(folgezeile_bauen(
            vorlage_continue, massnahme,
            *rr,
            k_f, m_f, h_f,
        ))

    return zeilen


# ── Datentabelle befüllen ─────────────────────────────────────────────────────

def datentabelle_befuellen(datentabelle, eintraege: list):
    """Befüllt die Datentabelle der Vorlage mit den Gefährdungseinträgen.

    Parst die Vorlage-Zeilen, extrahiert Template-Zeilen und baut die Tabelle neu auf.
    Kategorien ohne Einträge erhalten eine 'Keine Gefährdungen'-Zeile.
    """
    zeilen_alle = list(datentabelle.findall(w("tr")))

    # Template-Zeilen aus der Vorlage extrahieren
    vorlage_restart   = copy.deepcopy(zeilen_alle[3])   # erste Datenzeile (restart)
    vorlage_continue  = copy.deepcopy(zeilen_alle[4])   # Folgezeile (continue)
    vorlage_keine     = copy.deepcopy(zeilen_alle[10])  # "Keine Gefährdungen festgestellt."
    vorlage_trenner   = copy.deepcopy(zeilen_alle[8])   # einspaltiger Trenner

    # Einträge nach Kategorie gruppieren (Reihenfolge der JSON-Liste beibehalten)
    eintraege_nach_kat: dict[int, list] = {}
    for eintrag in eintraege:
        kat = _kategorie_nummer(eintrag.get("nr", ""))
        eintraege_nach_kat.setdefault(kat, []).append(eintrag)

    # Tabellenstruktur klassifizieren
    struktur = []
    for i, zeile in enumerate(zeilen_alle):
        zellen = zeile.findall(w("tc"))
        n = len(zellen)
        if n == 13:
            struktur.append(("spalten_kopf", zeile))
        elif n == 21 and i == 1:
            struktur.append(("sub_kopf", zeile))
        elif n == 2:
            struktur.append(("kat_kopf", zeile, _zellen_text_lesen(zellen[1])))
        elif n == 1:
            struktur.append(("spalten_kopf" if i <= 1 else "trenner", zeile))
        else:
            struktur.append(("inhalt", zeile))

    # Tabelle leeren
    for z in list(datentabelle.findall(w("tr"))):
        datentabelle.remove(z)

    # Spaltenköpfe wiederherstellen
    for item in struktur:
        if item[0] == "spalten_kopf":
            _hauptkopf_rahmen_patchen(item[1])
            datentabelle.append(item[1])
        elif item[0] == "sub_kopf":
            _subkopf_zeile_patchen(item[1])
            datentabelle.append(item[1])

    # Kategorien mit Einträgen befüllen
    ausstehende_trenner = []
    for item in struktur:
        if item[0] == "kat_kopf":
            for trenner in ausstehende_trenner:
                datentabelle.append(trenner)
            ausstehende_trenner = []

            # 1,5pt-Rahmen über Kategorie-Kopfzeile
            for zelle in item[1].findall(w("tc")):
                _rahmen_setzen_einfach(zelle, "top")
            datentabelle.append(item[1])

            # Kategorie-Nummer aus Label bestimmen
            kat_nr = None
            for k in KATEGORIE_LABELS:
                if item[2].startswith(str(k) + "."):
                    kat_nr = k
                    break

            if kat_nr is None or kat_nr not in eintraege_nach_kat:
                datentabelle.append(copy.deepcopy(vorlage_keine))
            else:
                for eintrag in eintraege_nach_kat[kat_nr]:
                    for zeile in eintragszeilen_erzeugen(vorlage_restart, vorlage_continue, eintrag):
                        datentabelle.append(zeile)

        elif item[0] == "trenner":
            if not ausstehende_trenner:
                ausstehende_trenner.append(copy.deepcopy(vorlage_trenner))

    for trenner in ausstehende_trenner:
        datentabelle.append(trenner)


# ── Metadaten befüllen ────────────────────────────────────────────────────────

def metadaten_befuellen(doc_xml: str, daten: dict):
    """Befüllt den Kopfteil des Dokuments mit Metadaten aus dem JSON.

    Parst document.xml und setzt Titel, Tätigkeitsbeschreibung und Maschinendaten.
    Ersetzt auch Datumsplatzhalter ([# Datum]) durch aktuellen Monat.
    """
    tree = etree.parse(doc_xml)
    wurzel = tree.getroot()
    koerper = wurzel.find(w("body"))
    tabellen = koerper.findall(f".//{w('tbl')}")
    tab0 = tabellen[0]
    zeilen0 = tab0.findall(w("tr"))

    # ── Titel: Zeile 0, Zelle 1, Absatz 1 ────────────────────────────
    if len(zeilen0) > 0:
        zellen_z0 = zeilen0[0].findall(w("tc"))
        if len(zellen_z0) > 1:
            absaetze = zellen_z0[1].findall(w("p"))
            ziel = absaetze[1] if len(absaetze) > 1 else absaetze[0]
            for t in ziel.findall(f".//{w('t')}"):
                t.text = daten.get("titel", "")

    # ── Tätigkeitsbeschreibung: Zeile 2, Zelle 0 ─────────────────────
    if len(zeilen0) > 2:
        zelle = zeilen0[2].find(w("tc"))
        if zelle is not None:
            absaetze = zelle.findall(w("p"))
            # Absatz 0: "Arbeitsplatz- / Tätigkeitsbeschreibung:" – unveränderlich
            # Absatz 1: Kopfzeile (Tätigkeit | Bereich | Maschinendaten) – ersetzen
            # Absatz 2: "Tätigkeitsbeschreibung:" – unveränderlich
            # Absatz 3+: Fließtext – ersetzen
            kopf = daten.get("taetigkeit", "")
            if daten.get("arbeitsbereich"):
                kopf += f" | {daten['arbeitsbereich']}"
            if daten.get("maschinendaten"):
                kopf += f" | {daten['maschinendaten']}"
            if len(absaetze) > 1:
                for t in absaetze[1].findall(f".//{w('t')}"):
                    t.text = kopf

            beschr = daten.get("taetigkeitsbeschreibung", "")
            if beschr and len(absaetze) > 3:
                for p in absaetze[3:]:
                    zelle.remove(p)
                for linie in (beschr.split("\n") if "\n" in beschr else [beschr]):
                    zelle.append(_absatz_erzeugen(linie))

    # ── Maschinendaten: Zeile 3, Zelle 0 ─────────────────────────────
    if len(zeilen0) > 3 and daten.get("maschinendaten"):
        zelle = zeilen0[3].find(w("tc"))
        if zelle is not None:
            for p in list(zelle.findall(w("p"))):
                zelle.remove(p)
            zelle.append(_absatz_erzeugen("Maschinendaten: ", fett=True))
            zelle.append(_absatz_erzeugen(daten["maschinendaten"]))

    # ── Datumsplatzhalter → aktueller Monat ──────────────────────────
    aktueller_monat = datetime.now().strftime("%m.%Y")
    for t in wurzel.findall(f".//{w('t')}"):
        text = t.text or ""
        if "MM" in text and "YY" in text:
            t.text = aktueller_monat
        elif text.strip() in ("[# Datum]", "[Datum]", "[# datum]"):
            t.text = aktueller_monat

    return tree


def kopfzeilen_befuellen(kopfzeile_xml: str, daten: dict):
    """Befüllt Platzhalter in header2.xml / header3.xml.

    Ersetzt [Kundenname, Betriebsort] und [Arbeitgeber... / Betriebsstätte]-Platzhalter.
    """
    tree = etree.parse(kopfzeile_xml)
    wurzel = tree.getroot()
    firma       = daten.get("firma", "")
    betriebsort = daten.get("betriebsort", "")
    vollstaendig = f"{firma}, {betriebsort}" if betriebsort else firma

    for t in wurzel.findall(f".//{w('t')}"):
        text = t.text or ""
        if "[Kundenname, Betriebsort]" in text:
            t.text = text.replace("[Kundenname, Betriebsort]", vollstaendig)
        elif "[Arbeitgeber" in text:
            t.text = text.replace("[Arbeitgeber", firma)
        elif "Betriebsstätte]" in text:
            t.text = text.replace("Betriebsstätte]", betriebsort)
    return tree


# ── JSON-Schema-Normalisierung ────────────────────────────────────────────────

def json_normalisieren(rohdaten: dict) -> tuple[dict, list]:
    """Normalisiert altes (meta-gekapseltes) und neues (flaches) JSON-Schema.

    Altes Schema: {"meta": {...}, "eintraege": [...]}
    Neues Schema: {"titel": ..., "firma": ..., "eintraege": [...]}
    Gibt (daten_dict, eintraege_list) zurück.
    """
    if isinstance(rohdaten, dict) and "meta" in rohdaten:
        # Rückwärtskompatibilität: meta-Wrapper auflösen
        daten = {**rohdaten.get("meta", {})}
        eintraege = rohdaten.get("eintraege", [])
    elif isinstance(rohdaten, dict):
        eintraege = rohdaten.get("eintraege", [])
        daten = {k: v for k, v in rohdaten.items() if k != "eintraege"}
    else:
        daten = {}
        eintraege = rohdaten if isinstance(rohdaten, list) else []
    return daten, eintraege


# ── XML-Baum speichern ────────────────────────────────────────────────────────

def _baum_speichern(tree, pfad: str):
    """Schreibt einen etree-Baum als XML-Datei (UTF-8, standalone)."""
    tree.write(pfad, xml_declaration=True, encoding="UTF-8", standalone=True)


# ── Hauptprogramm ─────────────────────────────────────────────────────────────

def hauptprogramm():
    """Kommandozeilen-Einstiegspunkt. Parst Argumente und orchestriert den Ablauf."""
    parser = argparse.ArgumentParser(
        description="STAPCON-GB-Vorlage mit JSON-Daten befüllen."
    )
    parser.add_argument("--template", "-t", required=False, default=None,
                        help="Pfad zur leeren DOCX-Vorlage")
    parser.add_argument("--json", "-j", default=None,
                        help="Pfad zur JSON-Datei (fehlt → Dateiauswahl-Dialog)")
    parser.add_argument("--output", "-o", default=None,
                        help="Ausgabepfad für die fertige DOCX (Standard: JSON-Name_GB.docx)")
    parser.add_argument("--no-password", action="store_true",
                        help="Kein Schreibschutz")
    parser.add_argument("--password", default="holiday",
                        help="Schutzpasswort (Standard: holiday)")
    parser.add_argument("--example-json", metavar="PFAD", default=None,
                        help="Speichert ein Beispiel-JSON und beendet")
    args = parser.parse_args()

    # Beispiel-JSON ausgeben und beenden
    if args.example_json:
        with open(args.example_json, "w", encoding="utf-8") as f:
            json.dump(BEISPIEL_JSON, f, ensure_ascii=False, indent=2)
        print(f"Beispiel-JSON gespeichert: {args.example_json}")
        return

    # Vorlage ist Pflicht für den Füll-Betrieb
    if not args.template:
        parser.error("--template ist erforderlich.")

    # JSON-Pfad per Dialog wenn nicht per Argument übergeben
    if args.json is None:
        try:
            import tkinter as tk
            from tkinter import filedialog
            root_tk = tk.Tk()
            root_tk.withdraw()
            root_tk.wm_attributes("-topmost", True)
            root_tk.update()
            args.json = filedialog.askopenfilename(
                parent=root_tk,
                title="GB-JSON auswählen",
                filetypes=[("JSON-Dateien", "*.json"), ("Alle Dateien", "*.*")],
            )
            root_tk.destroy()
        except Exception as e:
            print(f"[Fehler] Dateidialog fehlgeschlagen: {e}")
            sys.exit(1)
        if not args.json:
            print("[Abbruch] Keine Datei ausgewählt.")
            sys.exit(0)

    # Ausgabepfad ableiten wenn nicht angegeben
    if args.output is None:
        json_abs  = os.path.abspath(args.json)
        json_verz = os.path.dirname(json_abs)
        json_name = os.path.splitext(os.path.basename(json_abs))[0]
        args.output = os.path.join(json_verz, json_name + "_GB.docx")

    # ── 1. JSON laden ─────────────────────────────────────────────────
    print(f"[1/5] JSON laden: {args.json}")
    with open(args.json, encoding="utf-8") as f:
        rohdaten = json.load(f)

    daten, eintraege = json_normalisieren(rohdaten)
    print(f"      Titel:    {daten.get('titel', '(kein Titel)')}")
    print(f"      Einträge: {len(eintraege)}")

    # ── 2. Vorlage entpacken ──────────────────────────────────────────
    print(f"[2/5] Vorlage entpacken: {args.template}")
    arbeits_verz = tempfile.mkdtemp(prefix="stapcon_gb_")
    vorlage_kopie = os.path.join(arbeits_verz, "_vorlage.docx")
    try:
        shutil.copy2(args.template, vorlage_kopie)
    except PermissionError:
        print(f"[Fehler] Vorlage gesperrt (in Word geöffnet?): {args.template}")
        shutil.rmtree(arbeits_verz, ignore_errors=True)
        sys.exit(1)
    with zipfile.ZipFile(vorlage_kopie, "r") as zf:
        zf.extractall(arbeits_verz)

    doc_xml       = os.path.join(arbeits_verz, "word", "document.xml")
    settings_xml  = os.path.join(arbeits_verz, "word", "settings.xml")
    header2_xml   = os.path.join(arbeits_verz, "word", "header2.xml")
    header3_xml   = os.path.join(arbeits_verz, "word", "header3.xml")

    # ── 3. Meta + Datentabelle befüllen ──────────────────────────────
    print("[3/5] Meta und Datentabelle befüllen...")
    baum = metadaten_befuellen(doc_xml, daten)
    koerper = baum.getroot().find(w("body"))
    datentab = koerper.findall(f".//{w('tbl')}")[2]
    datentabelle_befuellen(datentab, eintraege)
    _baum_speichern(baum, doc_xml)

    for hf_pfad in [header2_xml, header3_xml]:
        if os.path.exists(hf_pfad):
            _baum_speichern(kopfzeilen_befuellen(hf_pfad, daten), hf_pfad)

    # ── 4. Passwortschutz ─────────────────────────────────────────────
    if not args.no_password and os.path.exists(settings_xml):
        print(f"[4/5] Passwortschutz setzen ('{args.password}')...")
        # → stapcon_kern.dokumentschutz_setzen() verwendet SHA-1 + Salt (ISO/IEC 29500)
        dokumentschutz_setzen(settings_xml, args.password)
    else:
        print("[4/5] Passwortschutz übersprungen.")

    # ── 5. DOCX packen ────────────────────────────────────────────────
    print(f"[5/5] DOCX erzeugen: {args.output}")
    if os.path.exists(args.output):
        try:
            os.remove(args.output)
        except PermissionError:
            basis, ext = os.path.splitext(args.output)
            args.output = f"{basis}_{datetime.now().strftime('%H%M%S')}{ext}"
            print(f"       Datei gesperrt – speichere als: {args.output}")
    with zipfile.ZipFile(args.output, "w", zipfile.ZIP_DEFLATED) as zf:
        for verz, _, dateien in os.walk(arbeits_verz):
            for dateiname in dateien:
                fp = os.path.join(verz, dateiname)
                zf.write(fp, os.path.relpath(fp, arbeits_verz))
    shutil.rmtree(arbeits_verz)

    kategorien = sorted({_kategorie_nummer(e.get("nr", ""))
                         for e in eintraege if e.get("nr")})
    print(f"\n✓  {args.output}")
    print(f"   {len(eintraege)} Einträge | Kategorien: {kategorien}")


# ── Beispiel-JSON ─────────────────────────────────────────────────────────────
# ERWEITERBAR: Weitere Eintragsbeispiele oder Kategorien ergänzen.

BEISPIEL_JSON = {
    "titel":                    "Maschinenbedienung und Instandhaltung – Anlage XY-200",
    "firma":                    "Musterwerk GmbH",
    "betriebsort":              "Musterstadt",
    "taetigkeit":               "Bedienung / Instandhaltung XY-200",
    "arbeitsbereich":           "Produktion Halle 3",
    "taetigkeitsbeschreibung": (
        "Die Mitarbeiter bedienen die Anlage XY-200 im Regelbetrieb sowie bei der "
        "regelmäßigen Wartung und Störungsbeseitigung. "
        "Die Tätigkeit wird täglich über 8 Stunden ausgeführt. "
        "Nur unterwiesene und beauftragte Personen dürfen die Anlage bedienen."
    ),
    "maschinendaten": "Hersteller: XY-GmbH | Typ: XY-200 | Bj.: 2022 | Nr.: 12345 | 15 kW",
    "eintraege": [
        {
            "nr":          "1.1",
            "gefaehrdung": "Mechanische Gefährdung | Kontakt mit rotierenden Teilen. Schnittverletzungen bis Amputation möglich.",
            "zustand":     "N",
            "datum":       "[# Datum]",
            "risiko":      5,
            "restrisiko":  3,
            "massnahmen": [
                {
                    "massnahme":   "T: Trennende Schutzeinrichtungen verriegelt (Endlagenschalter).",
                    "typ":         "T",
                    "zustaendig":  "[# verantw. FK]",
                    "termin":      "[# kurzfristig]",
                    "verweis":     "BetrSichV §§ 5-6\nDGUV V1 § 12",
                    "status":      "in_bearbeitung",
                    "wirksamkeit": 2,
                },
                {
                    "massnahme":  "O: Jährliche Unterweisung der Maschinenbediener.",
                    "typ":        "O",
                    "zustaendig": "[# verantw. FK]",
                    "termin":     "[# jährlich]",
                    "verweis":    "ArbSchG § 12\nDGUV V1 § 4",
                    "status":     "offen",
                },
                {
                    "massnahme":  "P: Sicherheitsschuhe (S2) und eng anliegende Arbeitskleidung.",
                    "typ":        "P",
                    "zustaendig": "[# verantw. FK]",
                    "termin":     "[# kurzfristig]",
                    "verweis":    "PSA-BV § 2\nDGUV Regel 112-191",
                    "status":     "erledigt",
                },
            ],
        },
        {
            "nr":          "2.1",
            "gefaehrdung": "Elektrische Gefährdung | Berühren spannungsführender Teile.",
            "zustand":     "N",
            "datum":       "[# Datum]",
            "risiko":      5,
            "restrisiko":  2,
            "massnahmen": [
                {
                    "massnahme":  "T: Elektrische Anlage nach DIN VDE 0100; Prüfung durch EFK alle 4 Jahre.",
                    "typ":        "T",
                    "zustaendig": "[# verantw. FK]",
                    "termin":     "[# gem. Prüfplan]",
                    "verweis":    "DGUV Vorschrift 3\nBetrSichV § 14",
                    "status":     "◔",
                },
                {
                    "massnahme":  "O: Wartungsarbeiten nur spannungsfrei (LOTO).",
                    "typ":        "O",
                    "zustaendig": "[# verantw. FK]",
                    "termin":     "[# kurzfristig]",
                    "verweis":    "DGUV V3 § 8\nBetrSichV § 12",
                    "status":     "◔",
                },
            ],
        },
        {
            "nr":          "10.2",
            "gefaehrdung": "Organisatorische Faktoren | Fehlende Unterweisung der Mitarbeiter.",
            "zustand":     "N",
            "datum":       "[# Datum]",
            "risiko":      4,
            "restrisiko":  2,
            "massnahmen": [
                {
                    "massnahme":  "O: Erstunterweisung vor Arbeitsbeginn, danach jährliche Wiederholung.",
                    "typ":        "O",
                    "zustaendig": "[# verantw. FK]",
                    "termin":     "[# jährlich]",
                    "verweis":    "ArbSchG § 12\nDGUV V1 § 4",
                    "status":     "offen",
                },
            ],
        },
    ],
}


if __name__ == "__main__":
    hauptprogramm()
