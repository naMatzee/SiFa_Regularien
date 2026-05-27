#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_psa_vorlage.py – PSA_Auswahl_Management.docx erzeugen.

Erzeugt die PSA-Auswahlhilfe als DOCX-Datei im aktuellen Verzeichnis.
Keine externen Abhängigkeiten außer der Python-Standardbibliothek.

Verwendung:
    python3 01_psa_vorlage.py
"""

import base64
import os
import sys

# ── Eingebettete DOCX-Vorlage (Base64) ───────────────────────────────────────
# Aktualisieren mit: python3 03_gb_selbst.py embed neue_vorlage.docx -o 01_psa_vorlage.py
# → Ähnliche Embed-Struktur in 02_tn_vorlage.py und 03_gb_selbst.py

_VORLAGE_B64 = (
    "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"
)


def vorlage_ausgeben():
    """Erzeugt PSA_Auswahl_Management.docx im Verzeichnis dieses Skripts."""
    ausgabe = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "PSA_Auswahl_Management.docx")
    if os.path.exists(ausgabe):
        antwort = input(f"{ausgabe} existiert bereits. Überschreiben? [j/N] ").strip().lower()
        if antwort not in ("j", "ja", "y", "yes"):
            print("Abgebrochen.")
            sys.exit(0)

    with open(ausgabe, "wb") as datei:
        datei.write(base64.b64decode(_VORLAGE_B64))

    groesse = os.path.getsize(ausgabe)
    print(f"Gespeichert: {ausgabe}  ({groesse:,} Bytes)")


if __name__ == "__main__":
    vorlage_ausgeben()
