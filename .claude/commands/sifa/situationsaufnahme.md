# Situationsaufnahme

Erfasst systematisch die Ausgangssituation als Grundlage für alle weiteren SiFa-Prozessschritte.

## Argument

`$ARGUMENTS` — Freitext-Beschreibung **oder** `--interview` für geführten Modus.

## Ablauf

### Modus erkennen

Enthält `$ARGUMENTS` den Flag `--interview` oder ist die Eingabe sehr kurz/unklar?
→ **Interview-Modus**: Stelle die Fragen aus "Strukturierte Abfrage" nacheinander.
→ **Freitext-Modus**: Extrahiere die Informationen direkt aus `$ARGUMENTS` und frage nur nach, was fehlt.

### Strukturierte Abfrage

Erfasse folgende Informationen (im Interview-Modus als Fragen, im Freitext-Modus durch Extraktion):

1. **Tätigkeit**: Was wird genau gemacht? (Beschreibung des Arbeitsvorgangs)
2. **Arbeitsort**: Wo findet die Tätigkeit statt? (Innen/Außen, Gebäude, besondere Umgebung)
3. **Betroffene Personen**: Wer führt die Tätigkeit aus? (Anzahl, Qualifikation, Besonderheiten wie Schwangere, Azubis, Fremdfirmen)
4. **Arbeitsmittel**: Welche Geräte, Maschinen, Werkzeuge werden eingesetzt?
5. **Arbeitsstoffe**: Welche Gefahrstoffe, Materialien oder Energieformen sind beteiligt?
6. **Häufigkeit und Dauer**: Wie oft und wie lange wird die Tätigkeit ausgeführt?
7. **Besondere Bedingungen**: Zeitdruck, Alleinarbeit, Nachtschicht, Witterung, o.ä.?

### Ausgabe

Erstelle einen strukturierten **Situations-Steckbrief**:

```
## Situations-Steckbrief
- Tätigkeit: ...
- Arbeitsort: ...
- Betroffene Personen: ...
- Arbeitsmittel: ...
- Arbeitsstoffe: ...
- Häufigkeit/Dauer: ...
- Besondere Bedingungen: ...
```

Dieser Steckbrief wird an den nächsten Schritt `/sifa:regelwerk-recherche` übergeben.
