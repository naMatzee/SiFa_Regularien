#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
stapcon_kern.py – Gemeinsames Kernmodul für alle STAPCON-Skripte.

Enthält: XML-Hilfsfunktionen, Risiko-Logik, Farben, Spalten-Indizes,
Status-Symbole und Dokumentschutz (SHA-1 + Salt, passwort: "holiday").

Dieses Modul wird nicht direkt ausgeführt, sondern von den Einzelskripten importiert:
    01_psa_vorlage.py     – PSA_Auswahl_Management.docx erzeugen
    02_tn_vorlage.py      – TN_Vorlage.docx erzeugen
    03_gb_selbst.py       – GB self-contained (Blob + fill + embed + check)
    04_gb_aus_vorlage.py  – GB aus externer .docx-Vorlage + JSON befüllen
"""

import base64
import hashlib
import os
from lxml import etree

# ── OOXML-Namespace ──────────────────────────────────────────────────────────

NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def w(bezeichner: str) -> str:
    """Erzeugt einen voll qualifizierten OOXML-Tag-Namen, z.B. w('p') → '{...ns...}p'."""
    return f"{{{NS_W}}}{bezeichner}"

# ── Risiko-Farben ────────────────────────────────────────────────────────────
# ERWEITERBAR: Weitere Risikostufen oder eigene Unternehmensfarben hier ergänzen.

FARBE_GRUEN = "00FF00"   # K-Spalte: Klein-Risiko  (Wert 1-2)
FARBE_GELB  = "FFFF00"   # M-Spalte: Mittel-Risiko (Wert 3-4)
FARBE_ROT   = "FF0000"   # H-Spalte: Hoch-Risiko   (Wert 5-7)
FARBE_WEISS = "FFFFFF"

# ── Spalten-Indizes der 21-Spalten-Datenzeile ────────────────────────────────
# ERWEITERBAR: Neue Spalten am Ende ergänzen und COL_*-Konstante hinzufügen.

SPALTE_NR        = 0    # Gefährdungs-Nr.
SPALTE_GEF       = 1    # Gefährdungsfaktor / Beschreibung
SPALTE_NORMAL    = 2    # Zustand: Normalbetrieb (N)
SPALTE_BESONDERS = 3    # Zustand: Besonderer Betrieb (B)
SPALTE_DATUM     = 4    # Datum der Beurteilung
SPALTE_K         = 5    # Risiko Klein
SPALTE_M         = 6    # Risiko Mittel
SPALTE_H         = 7    # Risiko Hoch
SPALTE_MASSNAHME = 8    # Maßnahmen-Beschreibung
SPALTE_S         = 9    # Maßnahmen-Typ: Substitution
SPALTE_T         = 10   # Maßnahmen-Typ: Technisch
SPALTE_O         = 11   # Maßnahmen-Typ: Organisatorisch
SPALTE_P         = 12   # Maßnahmen-Typ: Persönlich (PSA)
SPALTE_ZUST      = 13   # Zuständig
SPALTE_TERMIN    = 14   # Termin
SPALTE_VERWEIS   = 15   # Rechtsgrundlage / Verweis
SPALTE_STATUS    = 16   # Umsetzungsstatus (Symbol)
SPALTE_WIRK      = 17   # Wirksamkeit (bleibt immer leer – reserviert)
SPALTE_RR_K      = 18   # Restrisiko Klein
SPALTE_RR_M      = 19   # Restrisiko Mittel
SPALTE_RR_H      = 20   # Restrisiko Hoch

# ── Status-Symbol-Mapping ─────────────────────────────────────────────────────
# Unterstützt direkte Symbole (○●◔◑◕) und deutschen Klartext.
# ERWEITERBAR: Weitere Status-Stufen hier ergänzen.

STATUS_SYMBOLE = {
    "offen":          "○",
    "in_bearbeitung": "◔",
    "teilweise":      "◑",
    "fast_fertig":    "◕",
    "erledigt":       "●",
}
_SYMBOLE_DIREKT = frozenset("○◔◑◕●")


def status_symbol(wert: str) -> str:
    """Gibt das Status-Symbol zurück.

    Akzeptiert Symbole direkt (○●◔◑◕) und deutschen Text (offen/erledigt).
    Fallback bei unbekanntem Wert: ○ (offen).
    """
    if wert in _SYMBOLE_DIREKT:
        return wert
    schluessel = str(wert or "").lower().strip()
    # Kurzform "erl..." → erledigt (Abwärtskompatibilität)
    if schluessel.startswith("erl"):
        return STATUS_SYMBOLE["erledigt"]
    return STATUS_SYMBOLE.get(schluessel, "○")


# ── Risiko-Logik ──────────────────────────────────────────────────────────────
# → Ähnliche Logik in 03_gb_selbst.py (RISIKO_FARBE dict + inline)

def risiko_spalten(wert) -> tuple:
    """Berechnet K/M/H-Text und Hintergrundfarbe für einen Risikowert (1-7).

    Gibt (k_text, m_text, h_text, k_farbe, m_farbe, h_farbe) zurück.
    Ungültige Werte (None, 0, nicht-int) → alles leer/weiß.

    ERWEITERBAR: Weitere Risikostufen → Schwellenwerte hier anpassen.
    """
    try:
        v = int(wert)
        if v <= 0:
            raise ValueError
    except (TypeError, ValueError):
        return ("", "", "", FARBE_WEISS, FARBE_WEISS, FARBE_WEISS)

    s = str(v)
    if v <= 2:
        return (s,  "",  "",  FARBE_GRUEN, FARBE_WEISS, FARBE_WEISS)
    elif v <= 4:
        return ("",  s,  "",  FARBE_WEISS, FARBE_GELB,  FARBE_WEISS)
    else:
        return ("",  "",  s,  FARBE_WEISS, FARBE_WEISS, FARBE_ROT)


# ── XML-Hilfsfunktionen ────────────────────────────────────────────────────────

def tcpr_sicherstellen(zelle) -> etree._Element:
    """Liefert das <w:tcPr>-Element der Zelle, legt es bei Bedarf an."""
    tcpr = zelle.find(w("tcPr"))
    if tcpr is None:
        tcpr = etree.Element(w("tcPr"))
        zelle.insert(0, tcpr)
    return tcpr


def schattierung_setzen(zelle, farbe: str | None):
    """Setzt die Hintergrundfarbe (<w:shd>) einer Tabellenzelle.

    farbe: Hex-String ohne '#', z.B. "FF0000". None entfernt vorhandene Schattierung.
    → Ähnliche Logik in 03_gb_selbst.py (_set_fill)
    """
    tcpr = tcpr_sicherstellen(zelle)
    shd = tcpr.find(w("shd"))

    if farbe is None:
        if shd is not None:
            tcpr.remove(shd)
        return

    if shd is None:
        shd = etree.SubElement(tcpr, w("shd"))

    # Alle Attribute leeren, dann neu setzen (verhindert theme-Überschreibung)
    for attr in list(shd.attrib):
        del shd.attrib[attr]
    shd.set(w("val"),   "clear")
    shd.set(w("color"), "auto")
    shd.set(w("fill"),  farbe)


def vmerge_setzen(zelle, modus: str | None):
    """Setzt oder entfernt <w:vMerge> in einer Tabellenzelle.

    modus: 'restart' (erste Zelle einer vertikalen Gruppe),
           'continue' (Folgezellen, kein w:val-Attribut),
           None (vMerge entfernen).
    """
    tcpr = zelle.find(w("tcPr"))
    if tcpr is None:
        if modus is None:
            return
        tcpr = etree.Element(w("tcPr"))
        zelle.insert(0, tcpr)

    vm = tcpr.find(w("vMerge"))

    if modus is None:
        if vm is not None:
            tcpr.remove(vm)
        return

    if vm is None:
        vm = etree.SubElement(tcpr, w("vMerge"))

    if modus == "restart":
        vm.set(w("val"), "restart")
    else:
        # "continue": kein val-Attribut
        if w("val") in vm.attrib:
            del vm.attrib[w("val")]


# OOXML-konforme Reihenfolge der Rahmen-Seiten (für Schema-Validität)
_RAHMEN_REIHENFOLGE = ["top", "left", "bottom", "right", "insideH", "insideV", "tl2br", "tr2bl"]


def rahmen_anwenden(zelle, rahmen: dict):
    """Setzt Rahmen auf eine Tabellenzelle in OOXML-konformer Reihenfolge.

    rahmen: {seite: (val, sz, color)}, z.B.:
        {"top": ("single", "12", "000000"), "bottom": ("nil", "0", "auto")}
    Nicht genannte Seiten werden nicht verändert (Template-Default bleibt).

    ERWEITERBAR: Weitere Rahmenseiten (tl2br, tr2bl) einfach im Dict ergänzen.
    → Ähnliche Logik in 04_gb_aus_vorlage.py (_apply_borders)
    """
    tcpr = tcpr_sicherstellen(zelle)

    # Vorhandene tcBorders auslesen
    alt = tcpr.find(w("tcBorders"))
    vorhanden = {}
    if alt is not None:
        for kind in alt:
            seite = etree.QName(kind).localname
            vorhanden[seite] = dict(kind.attrib)
        tcpr.remove(alt)

    # Übergebene Rahmen zusammenführen (überschreiben vorhandene)
    for seite, spez in rahmen.items():
        vorhanden[seite] = {
            w("val"):   spez[0],
            w("sz"):    spez[1],
            w("space"): "0",
            w("color"): spez[2],
        }

    if not vorhanden:
        return

    # tcBorders vor w:shd einfügen (OOXML-Schemareihenfolge)
    shd = tcpr.find(w("shd"))
    if shd is not None:
        tcb = etree.Element(w("tcBorders"))
        tcpr.insert(list(tcpr).index(shd), tcb)
    else:
        tcb = etree.SubElement(tcpr, w("tcBorders"))

    # Elemente in OOXML-Reihenfolge schreiben
    for seite in _RAHMEN_REIHENFOLGE:
        if seite in vorhanden:
            b = etree.SubElement(tcb, w(seite))
            for k, v in vorhanden[seite].items():
                b.set(k, v)


def rahmen_setzen(zelle, seite: str, staerke: str = "12"):
    """Setzt eine einzelne Rahmenkante (schwarz, 'single') auf eine Zelle.

    Kurzform für rahmen_anwenden mit einer Seite.
    staerke: '4' = 0,5 pt, '12' = 1,5 pt (OOXML: achtel Punkt).
    """
    rahmen_anwenden(zelle, {seite: ("single", staerke, "000000")})


def absatz_erstellen(text: str = "", schriftgroesse: int = 16,
                     fett: bool = False, ausrichtung: str | None = None) -> etree._Element:
    """Erstellt ein <w:p>-Element mit Arial-Schrift, kompaktem Abstand.

    schriftgroesse: in halben Punkten (16 = 8 pt, 20 = 10 pt).
    ausrichtung: None | 'center' | 'left' | 'right'.
    → Ähnliche Logik in 04_gb_aus_vorlage.py (make_para)
    """
    p = etree.Element(w("p"))
    ppr = etree.SubElement(p, w("pPr"))
    sp = etree.SubElement(ppr, w("spacing"))
    sp.set(w("before"), "60")
    sp.set(w("after"),  "60")
    if ausrichtung:
        etree.SubElement(ppr, w("jc")).set(w("val"), ausrichtung)

    def _run_props(eltern):
        rpr = etree.SubElement(eltern, w("rPr"))
        rf = etree.SubElement(rpr, w("rFonts"))
        for attr in ("ascii", "hAnsi", "cs"):
            rf.set(w(attr), "Arial")
        etree.SubElement(rpr, w("sz")).set(w("val"),   str(schriftgroesse))
        etree.SubElement(rpr, w("szCs")).set(w("val"), str(schriftgroesse))
        if fett:
            etree.SubElement(rpr, w("b"))
            etree.SubElement(rpr, w("bCs"))
        return rpr

    _run_props(ppr)                 # pPr-rPr (Absatz-Standardformat)
    r = etree.SubElement(p, w("r"))
    _run_props(r)                   # r-rPr
    t = etree.SubElement(r, w("t"))
    if text and (text.startswith(" ") or text.endswith(" ")):
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
    t.text = text or ""
    return p


def zelle_beschriften(zelle, text: str, zentriert: bool = False,
                      mehrzeilig: bool = False, fett: bool = False,
                      schriftgroesse: int = 16):
    """Ersetzt den Inhalt einer Tabellenzelle durch neuen Text.

    Entfernt alle vorhandenen <w:p>, schreibt einen neuen mit expliziter Formatierung.
    Bei mehrzeilig=True und '\\n' im Text werden mehrere Absätze erzeugt.

    → Ähnliche Logik in 03_gb_selbst.py (_cell_set_text / _cell_set_multiline)
    """
    for p in list(zelle.findall(w("p"))):
        zelle.remove(p)

    ausrichtung = "center" if zentriert else None

    if mehrzeilig and text and "\n" in text:
        for zeile in text.split("\n"):
            zelle.append(absatz_erstellen(
                zeile, schriftgroesse=schriftgroesse,
                fett=fett, ausrichtung=ausrichtung,
            ))
    else:
        zelle.append(absatz_erstellen(
            text or "", schriftgroesse=schriftgroesse,
            fett=fett, ausrichtung=ausrichtung,
        ))


# ── Passwortschutz ─────────────────────────────────────────────────────────────

def passwort_hash(passwort: str) -> tuple[str, str]:
    """Berechnet SHA-1 + Zufalls-Salt für OOXML-documentProtection.

    Rückgabe: (base64_hash, base64_salt)
    Algorithmus: ISO/IEC 29500, cryptAlgorithmSid=4 (SHA-1), spinCount=100000.
    ERWEITERBAR: spinCount für höhere Sicherheit erhöhen (>= 100000 empfohlen).
    """
    salt = os.urandom(16)
    pw = passwort.encode("utf-16-le")
    h = hashlib.sha1(salt + pw).digest()
    for i in range(100000):
        h = hashlib.sha1(h + i.to_bytes(4, "little")).digest()
    return base64.b64encode(h).decode(), base64.b64encode(salt).decode()


def dokumentschutz_setzen(settings_pfad: str, passwort: str = "holiday"):
    """Setzt OOXML-documentProtection (readOnly) in settings.xml.

    Verwendet SHA-1 + zufälliges Salt (sicherer als ältere XOR-Methode).
    → Ähnliche Logik in 03_gb_selbst.py (set_protection) und
      04_gb_aus_vorlage.py (apply_protection – dort noch XOR, hier SHA-1).
    """
    from lxml import etree as _etree

    if not os.path.isfile(settings_pfad):
        return

    baum = _etree.parse(settings_pfad)
    wurzel = baum.getroot()

    # Alte Schutzeinstellung entfernen
    for alt in wurzel.findall(w("documentProtection")):
        wurzel.remove(alt)

    h, salt = passwort_hash(passwort)

    prot = _etree.Element(w("documentProtection"))
    prot.set(w("edit"),               "readOnly")
    prot.set(w("enforcement"),        "1")
    prot.set(w("cryptProviderType"),  "rsaFull")
    prot.set(w("cryptAlgorithmClass"),"hash")
    prot.set(w("cryptAlgorithmType"), "typeAny")
    prot.set(w("cryptAlgorithmSid"),  "4")       # SHA-1
    prot.set(w("cryptSpinCount"),     "100000")
    prot.set(w("hash"),               h)
    prot.set(w("salt"),               salt)

    wurzel.insert(0, prot)
    baum.write(settings_pfad, xml_declaration=True, encoding="UTF-8", standalone=True)
