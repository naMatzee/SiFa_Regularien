# Gefährdungsbeurteilung

Erstellt eine vollständige GBU auf Basis der Situationsaufnahme und der Regelwerksrecherche.

## Eingabe

- Situations-Steckbrief aus `/sifa:situationsaufnahme`
- Regelwerksliste aus `/sifa:regelwerk-recherche`

## Ablauf

### 1. Gefährdungen systematisch ermitteln

Gehe alle Gefährdungsfaktoren-Kategorien durch und identifiziere zutreffende Gefährdungen:

| Kategorie | Typische Gefährdungen |
|-----------|----------------------|
| Mechanisch | Quetsch-, Scher-, Schnitt-, Stoßgefahr, bewegte Teile, herabfallende Gegenstände |
| Elektrisch | Stromschlag, Lichtbogen, statische Entladung |
| Chemisch | Einatmen, Hautkontakt, Verschlucken von Gefahrstoffen |
| Biologisch | Infektionserreger, Allergene, Schimmelpilze |
| Physikalisch | Lärm, Vibration, Strahlung, Hitze/Kälte, Beleuchtung |
| Brand/Explosion | Zündquellen, brennbare Stoffe, explosionsfähige Atmosphären |
| Ergonomisch | Heben/Tragen, Zwangshaltungen, repetitive Bewegungen |
| Psychisch | Zeitdruck, Monotonie, Gewalt, emotionale Belastung |
| Sonstige | Absturz, Ertrinken, Verkehr, Tier- und Pflanzengefährdungen |

### 2. Risiken bewerten

Rufe `/utils:risikomatrix` auf, um jede identifizierte Gefährdung zu bewerten.
Ergebnis: Risikostufe (gering / mittel / hoch / sehr hoch) für jede Gefährdung.

### 3. Maßnahmen ableiten

Rufe `/utils:stop-prinzip` auf, um Maßnahmen in STOP-Reihenfolge abzuleiten.
Prüfe dabei: Entsprechen die Maßnahmen den Anforderungen der gefundenen Regelwerke?

### 4. Maßnahmen dokumentieren

Für jede Maßnahme: Verantwortliche Person, Umsetzungstermin, Wirksamkeitsprüfung (wann/wie).

### Ausgabe

```
## Gefährdungsbeurteilung
**Tätigkeit:** ...
**Datum:** ...
**Erstellt durch:** ...

### Gefährdungen und Maßnahmen

| Nr | Gefährdung | Kategorie | Risiko (ohne M.) | Maßnahmen (STOP) | Risiko (mit M.) | Verantwortlich | Termin |
|----|-----------|-----------|-----------------|-----------------|-----------------|----------------|--------|
| 1  | ...       | ...       | hoch            | S: ... T: ...   | gering          | ...            | ...    |

### Gesamtbewertung
- Offene Maßnahmen: ...
- Nächste Überprüfung: ...
```

Diese GBU wird an `/sifa:betriebsanweisung` und `/sifa:unterweisung` übergeben.
