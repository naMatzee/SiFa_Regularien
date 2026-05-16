# Risikomatrix

Bewertet eine Gefährdung nach Eintrittswahrscheinlichkeit und Schadensausmaß und gibt die Risikostufe zurück.

## Argument

`$ARGUMENTS` — Beschreibung der Gefährdung, ggf. mit Kontext zur Häufigkeit und Schwere.

## Ablauf

### 1. Einstufung abfragen / ableiten

**Eintrittswahrscheinlichkeit (W)**
| Stufe | Bezeichnung | Beschreibung |
|-------|-------------|-------------|
| 1 | Sehr unwahrscheinlich | Tritt praktisch nie auf |
| 2 | Unwahrscheinlich | Selten, unter besonderen Umständen |
| 3 | Möglich | Gelegentlich, vorstellbar |
| 4 | Wahrscheinlich | Häufig, regelmäßig zu erwarten |
| 5 | Sehr wahrscheinlich | Fast sicher, bei jeder Durchführung |

**Schadensausmaß (S)**
| Stufe | Bezeichnung | Beschreibung |
|-------|-------------|-------------|
| 1 | Vernachlässigbar | Keine oder minimale Verletzung |
| 2 | Leicht | Erste-Hilfe-Maßnahme, kein Ausfall |
| 3 | Mittel | Behandlungsbedürftig, kurzer Ausfall |
| 4 | Schwer | Dauerhafte Einschränkung, langer Ausfall |
| 5 | Katastrophal | Tod, irreversibler Schaden, viele Betroffene |

### 2. Risikozahl berechnen

**R = W × S**

### 3. Risikostufe bestimmen

| R | Risikostufe | Handlungsbedarf |
|---|-------------|-----------------|
| 1–4 | **Gering** | Beobachten, bei nächster GBU-Revision prüfen |
| 5–9 | **Mittel** | Maßnahmen mittelfristig umsetzen |
| 10–16 | **Hoch** | Maßnahmen kurzfristig umsetzen |
| 17–25 | **Sehr hoch** | Sofortmaßnahme, ggf. Tätigkeit einstellen |

### Ausgabe

```
## Risikobewertung

**Gefährdung:** ...
**Eintrittswahrscheinlichkeit:** W = [1–5] ([Bezeichnung])
**Schadensausmaß:** S = [1–5] ([Bezeichnung])
**Risikozahl:** R = W × S = [Zahl]
**Risikostufe:** [Gering / Mittel / Hoch / Sehr hoch]
**Handlungsbedarf:** ...
```
