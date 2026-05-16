# Regelwerksrecherche

Findet alle relevanten Regelwerke für eine erfasste Situation und gibt konkrete Fundstellen zurück.

## Eingabe

Situations-Steckbrief aus `/sifa:situationsaufnahme`.

## Ablauf

### 1. Regelwerkskategorien ableiten

Leite aus dem Situations-Steckbrief ab, welche Regelwerkskategorien relevant sind:

- **Arbeitsmittel/Maschinen** → TRBS (Technische Regeln Betriebssicherheit)
- **Gefahrstoffe/Chemikalien** → TRGS (Technische Regeln Gefahrstoffe)
- **Unfallverhütung allgemein** → DGUV Vorschriften und Regeln
- **Branchenspezifisches** → DGUV Informationen, GDA-Empfehlungen
- **Normen** → DIN/EN-Normen (Hinweis: nicht im lokalen Regelwerk, extern recherchieren)

### 2. Lokale Dokumente durchsuchen

Nutze `/utils:dokument-lesen` für jedes relevante Dokument aus den folgenden Verzeichnissen:

- TRBS: `01_Dokumente/03_TRBS/`
- TRGS: `01_Dokumente/04_TRGS/`
- DGUV Vorschriften: `01_Dokumente/05_DGUV Vorschriften/`
- DGUV Regeln: `01_Dokumente/06_DGUV Regeln/`
- DGUV Informationen: `01_Dokumente/07_DGUV_Informationen/`
- GDA: `01_Dokumente/08_GDA/`

Suche gezielt nach Dokumenten, deren Nummer oder Inhalt zur Situation passt.

### 3. Relevanz bewerten

Für jedes gefundene Dokument: Ist es **direkt anwendbar** (Pflicht-Grundlage) oder nur **ergänzend** (Best Practice)?

### Ausgabe

Erstelle eine **Regelwerksliste**:

```
## Relevante Regelwerke

### Direkt anwendbar (Pflicht-Grundlage)
| Dokument | Titel | Relevante Abschnitte | Begründung |
|----------|-------|----------------------|------------|
| ...      | ...   | ...                  | ...        |

### Ergänzend (Best Practice)
| Dokument | Titel | Relevante Abschnitte | Hinweis |
|----------|-------|----------------------|---------|
| ...      | ...   | ...                  | ...     |

### Nicht im lokalen Regelwerk — extern recherchieren
- ...
```

Diese Liste wird an `/sifa:gefaehrdungsbeurteilung` übergeben.
