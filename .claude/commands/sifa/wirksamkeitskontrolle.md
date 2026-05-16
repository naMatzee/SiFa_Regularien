# Wirksamkeitskontrolle

Erstellt eine Checkliste und Termine zur Überprüfung, ob die Maßnahmen aus der GBU wirksam umgesetzt wurden.

## Eingabe

- GBU-Ergebnisse aus `/sifa:gefaehrdungsbeurteilung` (insbesondere: Maßnahmen mit Terminen und Verantwortlichen)

## Ablauf

### 1. Maßnahmen kategorisieren

Teile die Maßnahmen in drei Gruppen:

- **Sofortmaßnahmen** (Risiko sehr hoch): Wann umgesetzt? Von wem geprüft?
- **Fristgebundene Maßnahmen** (Risiko hoch/mittel): Termin, Verantwortlicher, Prüfmethode
- **Dauerhafte Maßnahmen** (laufend): Wie regelmäßig prüfen? In Begehung integrieren?

### 2. Prüfmethoden festlegen

Für jede Maßnahme: Wie lässt sich Wirksamkeit feststellen?
- Sichtprüfung (PSA vorhanden und getragen?)
- Messung (Lärmpegel, Gefahrstoffkonzentration)
- Dokumentenprüfung (Unterweisungsnachweis vorhanden?)
- Verhaltensbeobachtung (Arbeitsablauf wie festgelegt?)

### 3. Wiedervorlagetermine setzen

Wann ist die GBU zu aktualisieren?
- Nach Unfällen oder Beinahe-Unfällen
- Bei wesentlichen Änderungen der Tätigkeit
- Spätestens alle 2–3 Jahre (Empfehlung, branchenabhängig)

### Ausgabe

```
## Wirksamkeitskontrolle

**GBU für:** ...
**Erstellt:** ...

### Prüfplan

| Maßnahme | Kategorie | Prüfmethode | Prüftermin | Verantwortlich | Erledigt |
|----------|-----------|-------------|------------|----------------|----------|
| ...      | Sofort    | Sichtprüfung | ...       | ...            | [ ]      |

### Nächste GBU-Aktualisierung
- Planmäßig: ...
- Anlassbezogen bei: Unfall, Änderung der Tätigkeit, neue Erkenntnisse

### Offene Punkte nach Erstprüfung
(wird ausgefüllt nach tatsächlicher Prüfung)
```

Ergebnisse fließen in `/sifa:dokumentation` ein.
