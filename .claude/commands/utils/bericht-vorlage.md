# Bericht-Vorlage

Formatiert beliebige SiFa-Inhalte in eine einheitliche, professionelle Berichtsstruktur.

## Argument

`$ARGUMENTS` — Berichtstyp und Rohinhalte (z.B. "Tagesbericht", "GBU-Zusammenfassung", "Mängelliste").

## Ablauf

### 1. Berichtstyp erkennen

| Typ | Vorlage |
|-----|---------|
| Tagesbericht | Datum, Ort, Tätigkeiten, Mängel, Offene Punkte, Unterschrift |
| Mängelliste | Nummerierte Tabelle: Mangel, Ort, Risiko, Maßnahme, Termin, Status |
| Besprechungsprotokoll | Datum, Teilnehmer, TOP, Ergebnis, Verantwortlich, Termin |
| Prüfprotokoll | Prüfgegenstand, Prüfdatum, Prüfer, Kriterien, Befund, Ergebnis |
| Zusammenfassung | Titel, Datum, Kurzfassung (max. 5 Sätze), Kernpunkte als Liste |

### 2. Kopfzeile einheitlich setzen

Jeder Bericht beginnt mit:
```
**[Berichtstyp]**
Datum: ___________  |  Erstellt von: ___________  |  Bereich/Projekt: ___________
```

### 3. Inhalte einfügen

Füge die übergebenen Inhalte in die passende Vorlage ein. Fehlende Pflichtfelder als leere Zeile mit `___________` kennzeichnen.

### 4. Abschluss

Jeder Bericht endet mit Unterschriftszeile und ggf. Verteiler-Hinweis.

### Ausgabe

Fertiger, formatierter Bericht — bereit zum Ausdrucken oder Ablegen in `/sifa:dokumentation`.
