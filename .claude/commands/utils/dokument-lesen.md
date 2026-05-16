# Dokument lesen

Liest ein spezifisches Regelwerksdokument aus dem lokalen Repository.

## Argument

`$ARGUMENTS` — Dokumentname, z.B. `TRBS-1001`, `TRGS-510`, oder Suchbegriff.

## Ablauf

### 1. Dokument lokalisieren

Suche die Datei in den folgenden Verzeichnissen (relativ zum Repo-Root):

| Regelwerkstyp | Verzeichnis |
|--------------|-------------|
| TRBS | `01_Dokumente/03_TRBS/` |
| TRGS | `01_Dokumente/04_TRGS/` |
| DGUV Vorschriften | `01_Dokumente/05_DGUV Vorschriften/` |
| DGUV Regeln | `01_Dokumente/06_DGUV Regeln/` |
| DGUV Informationen | `01_Dokumente/07_DGUV_Informationen/` |
| GDA | `01_Dokumente/08_GDA/` |
| Normen | `01_Dokumente/09_Normen/` |
| Interne Regelungen (Stapcon) | `01_Dokumente/10_Interne Regelungen Stapcon/` |
| Interne Regelungen (Auftraggeber) | `01_Dokumente/11_Interne Regelungen Auftraggeber/` |

Ist kein exakter Match → suche nach dem nächstähnlichen Dateinamen.
Ist die Datei nicht vorhanden → melde klar: "Nicht im lokalen Regelwerk vorhanden."

### 2. Inhalt ausgeben

Lies die Datei und gib den Inhalt zurück. Bei sehr langen Dokumenten:
- Gib zuerst Titel, Datum, Anwendungsbereich aus
- Dann die für den Kontext relevanten Abschnitte

### Ausgabe

```
## [Dokumentname]
**Quelle:** [Dateipfad]
**Ausgabe/Stand:** [aus Dokument]

[Relevanter Inhalt]
```
