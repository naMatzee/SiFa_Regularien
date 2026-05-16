# Tagesbericht

Erstellt einen strukturierten SiFa-Tagesbericht über Beobachtungen, Tätigkeiten und offene Punkte.

## Argument

`$ARGUMENTS` — Freitext-Beschreibung des Tages **oder** `--interview` für geführten Modus.

## Ablauf

### Modus erkennen

Enthält `$ARGUMENTS` den Flag `--interview` oder ist die Eingabe sehr kurz?
→ **Interview-Modus**: Stelle die Fragen aus "Strukturierte Abfrage" nacheinander.
→ **Freitext-Modus**: Extrahiere direkt, frage nur nach was fehlt.

### Strukturierte Abfrage

1. **Datum und Einsatzort**: Wann und wo war der Einsatz?
2. **Durchgeführte Tätigkeiten**: Was wurde heute gemacht? (Begehungen, Beratungen, Unterweisungen, Prüfungen, …)
3. **Festgestellte Mängel**: Welche Sicherheitsmängel oder Verstöße wurden beobachtet?
4. **Sofortmaßnahmen**: Was wurde direkt veranlasst oder korrigiert?
5. **Offene Punkte**: Was muss nachverfolgt werden (mit Termin und Verantwortlichem)?
6. **Besondere Vorkommnisse**: Unfälle, Beinahe-Unfälle, Behördenbesuche, …?

### Offene Punkte einordnen

Für jeden offenen Punkt: Gehört er in die GBU (`/sifa:gefaehrdungsbeurteilung`) oder die Wirksamkeitskontrolle (`/sifa:wirksamkeitskontrolle`)?
Markiere entsprechend, damit die Rückkopplung in den Workflow klar ist.

### Ausgabe

Nutze `/utils:bericht-vorlage` um den Bericht zu formatieren.

```
## SiFa-Tagesbericht

**Datum:** ___________     **Einsatzort:** ___________
**SiFa:** ___________

---
### Durchgeführte Tätigkeiten
...

### Festgestellte Mängel
| Nr | Bereich | Mangel | Risiko | Sofortmaßnahme |
|----|---------|--------|--------|----------------|
| 1  | ...     | ...    | ...    | ...            |

### Offene Punkte / Nachverfolgung
| Nr | Punkt | Verantwortlich | Termin | Rückfluss in |
|----|-------|----------------|--------|--------------|
| 1  | ...   | ...            | ...    | GBU / Wirksamkeitskontrolle |

### Besondere Vorkommnisse
...

### Unterschrift
_______________    Datum: ___________
```
