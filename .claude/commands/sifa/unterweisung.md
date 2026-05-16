# Unterweisung

Erstellt Unterweisungsinhalte und einen Unterweisungsplan aus GBU und Betriebsanweisung.

## Eingabe

- GBU-Ergebnisse aus `/sifa:gefaehrdungsbeurteilung`
- Betriebsanweisung(en) aus `/sifa:betriebsanweisung`

## Ablauf

### 1. Unterweisungsbedarf ermitteln

- Wer muss unterwiesen werden? (aus Situations-Steckbrief: betroffene Personen)
- Wann? (vor Arbeitsaufnahme, nach Änderungen, mindestens jährlich gemäß § 12 ArbSchG)
- Welche Besonderheiten? (Sprache, Qualifikationsniveau, Schichtbetrieb)

### 2. Kerninhalte aus GBU ableiten

Übernimm direkt aus der GBU:
- Die **größten Risiken** (hoch/sehr hoch) → Hauptthemen der Unterweisung
- Die **kritischen Maßnahmen** → Was müssen Beschäftigte zwingend wissen und tun?
- Die **PSA** → Was muss getragen werden und warum?

### 3. Unterweisungsplan erstellen

Struktur: Thema → Lernziel → Methode → Dauer → Nachweis

### 4. Unterweisungsnachweis-Vorlage erstellen

Pflichtbestandteile nach § 12 ArbSchG.

### Ausgabe

```
## Unterweisungsplan

**Tätigkeit:** ...
**Zielgruppe:** ...
**Turnus:** jährlich (ggf. anlassbezogen bei Änderungen)

### Inhalte

| Nr | Thema | Lernziel | Methode | Dauer |
|----|-------|----------|---------|-------|
| 1  | ...   | ...      | Vortrag + Demonstration | ... min |

### Unterweisungsnachweis

Ich bestätige, am ___________ über folgende Themen unterwiesen worden zu sein:
[ ] ...
[ ] ...

Name: _______________  Unterschrift: _______________  Datum: ___________
```

Diese Unterlagen werden an `/sifa:wirksamkeitskontrolle` und `/sifa:dokumentation` übergeben.
