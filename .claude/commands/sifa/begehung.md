# Begehung

Erstellt ein Begehungsprotokoll und einen strukturierten Begehungsplan für den Arbeitsbereich.

## Eingabe

- GBU-Ergebnisse aus `/sifa:gefaehrdungsbeurteilung`
- Wirksamkeitskontrolle aus `/sifa:wirksamkeitskontrolle`

## Ablauf

### 1. Begehungsschwerpunkte festlegen

Leite aus der GBU ab, worauf bei der Begehung besonders zu achten ist:
- Maßnahmen mit hohem/sehr hohem Restrisiko → priorisiert prüfen
- Technische Schutzmaßnahmen → augenscheinlich vorhanden und funktionsfähig?
- Ordnung und Sauberkeit als Basiskontrolle

### 2. Begehungsplan erstellen

Empfohlener Turnus (gesetzliche Mindestanforderung beachten):
- ASA-pflichtige Betriebe: gemäß § 11 ASiG (Betriebsärztlicher Dienst + SiFa)
- Allgemein: mindestens 1× jährlich, bei Risiko häufiger

### 3. Begehungsprotokoll-Vorlage

Strukturiere das Protokoll nach den Prüfpunkten aus der GBU.

### Ausgabe

```
## Begehungsplan

**Bereich/Tätigkeit:** ...
**Turnus:** ...
**Teilnehmer:** SiFa, Vorgesetzte/r, ggf. Betriebsarzt, Betriebsrat

---
## Begehungsprotokoll

**Datum:** ___________
**Bereich:** ___________
**Anwesende:** ___________

### Prüfpunkte

| Nr | Prüfpunkt (aus GBU) | Befund | Maßnahme | Termin | Erledigt |
|----|---------------------|--------|----------|--------|----------|
| 1  | ...                 | o.B. / Mangel | ... | ... | [ ] |

### Positive Feststellungen
...

### Mängel und Sofortmaßnahmen
...

### Unterschriften
SiFa: _______________    Vorgesetzte/r: _______________    Datum: ___________
```

**Hinweis:** Erkannte Mängel fließen als Anlassaktualisierung zurück in die GBU (`/sifa:gefaehrdungsbeurteilung`).
Der Kreislauf beginnt neu.
