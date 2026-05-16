# STOP-Prinzip

Leitet Maßnahmen für eine Gefährdung in der vorgeschriebenen STOP-Reihenfolge ab.

## Argument

`$ARGUMENTS` — Beschreibung der Gefährdung und des Arbeitsablaufs.

## Ablauf

### STOP-Hierarchie anwenden

Gehe die vier Stufen der Reihe nach durch. Erst wenn eine Stufe keine vollständige Beseitigung ermöglicht, wird die nächste Stufe herangezogen.

**S — Substitution** (höchste Priorität)
Kann die Gefährdung vollständig beseitigt werden, indem der Stoff, das Verfahren oder das Arbeitsmittel ersetzt wird?
→ Beispiel: Lösungsmittelhaltigen Lack durch wasserbasiertes Produkt ersetzen.

**T — Technische Maßnahmen**
Kann die Gefährdung durch technische Einrichtungen auf ein vertretbares Maß reduziert werden?
→ Beispiel: Schutzabdeckung, Absauganlage, Lärmdämmkapselung, trennende Schutzeinrichtung.

**O — Organisatorische Maßnahmen**
Kann durch Arbeitsorganisation die Exposition reduziert werden?
→ Beispiel: Arbeitszeiten begrenzen, Zugang beschränken, Vier-Augen-Prinzip, Anweisungen.

**P — Persönliche Schutzmaßnahmen** (niedrigste Priorität)
PSA nur als letzte Maßnahme oder ergänzend zu T und O.
→ Beispiel: Schutzhandschuhe, Gehörschutz, Atemschutz, Schutzbrille.

### Begründungspflicht

Für jede Stufe, die keine vollständige Beseitigung ermöglicht: kurze Begründung warum.

### Ausgabe

```
## Maßnahmen nach STOP

**Gefährdung:** ...

| Stufe | Maßnahme | Wirkung | Begründung falls nicht ausreichend |
|-------|----------|---------|-----------------------------------|
| S | ... | vollständig / teilweise | ... |
| T | ... | vollständig / teilweise | ... |
| O | ... | vollständig / teilweise | ... |
| P | ... | ergänzend | — |

**Restrisiko nach Maßnahmen:** [Risikostufe aus /utils:risikomatrix]
```
