# Betriebsanweisung

Erstellt eine fertige Betriebsanweisung auf Basis der GBU und der relevanten Regelwerke.

## Eingabe

- Regelwerksliste aus `/sifa:regelwerk-recherche`
- GBU-Ergebnisse aus `/sifa:gefaehrdungsbeurteilung`

## Ablauf

### 1. Typ bestimmen

Handelt es sich um:
- **Gefahrstoff** → Betriebsanweisung nach § 14 GefStoffV / TRGS 555 (GHS-Struktur)
- **Arbeitsmittel/Maschine** → Betriebsanweisung nach § 12 BetrSichV
- **Tätigkeit allgemein** → Verfahrensanweisung

### 2. Inhalte aus GBU übernehmen

Übernimm aus der GBU direkt:
- Identifizierte Gefährdungen → Abschnitt "Gefahren"
- STOP-Maßnahmen → Abschnitt "Schutzmaßnahmen"
- Persönliche Schutzausrüstung → Abschnitt "PSA"

Füge hinzu (aus den Regelwerken):
- Grenzwerte (AGW, BGW) für Gefahrstoffe
- Prüffristen für Arbeitsmittel
- Notfallmaßnahmen

### 3. Regelkonformität prüfen

Vergleiche den Entwurf mit den relevanten Abschnitten der Regelwerksliste. Sind alle Pflichtinhalte abgedeckt?

### Ausgabe

Erstelle die Betriebsanweisung in der Standardstruktur:

```
## BETRIEBSANWEISUNG Nr. [BA-XXXX]

**Tätigkeit/Stoff:** ...          **Arbeitsbereich:** ...
**Gültig ab:** ...                 **Erstellt von:** ...

---
### 1. Anwendungsbereich
...

### 2. Gefahren für Mensch und Umwelt
...

### 3. Schutzmaßnahmen und Verhaltensregeln
...

### 4. Verhalten bei Störungen und Unfällen
...

### 5. Erste Hilfe
...

### 6. Instandhaltung / Entsorgung
...

### 7. Rechtliche Grundlagen
...
---
Unterschrift Ersteller: ___________    Datum: ___________
```

Diese Betriebsanweisung wird an `/sifa:unterweisung` übergeben.
