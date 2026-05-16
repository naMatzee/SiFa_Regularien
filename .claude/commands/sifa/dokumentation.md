# Dokumentation

Bündelt alle Ergebnisse des SiFa-Prozesses in eine strukturierte Dokumentationsmappe und prüft die Nachweispflichten.

## Eingabe

Alle vorherigen Ergebnisse:
- Situations-Steckbrief (`/sifa:situationsaufnahme`)
- Regelwerksliste (`/sifa:regelwerk-recherche`)
- GBU (`/sifa:gefaehrdungsbeurteilung`)
- Betriebsanweisung(en) (`/sifa:betriebsanweisung`)
- Unterweisungsplan + Nachweis (`/sifa:unterweisung`)
- Wirksamkeitskontrolle (`/sifa:wirksamkeitskontrolle`)

## Ablauf

### 1. Nachweispflichten prüfen

| Dokument | Rechtsgrundlage | Aufbewahrungsfrist | Vorhanden? |
|----------|-----------------|--------------------|------------|
| GBU | § 6 ArbSchG | Beschäftigungsdauer + 2 Jahre | [ ] |
| Unterweisungsnachweis | § 12 ArbSchG | mind. 2 Jahre | [ ] |
| Betriebsanweisung | § 14 GefStoffV / § 12 BetrSichV | aktuell halten | [ ] |
| Prüfprotokolle Arbeitsmittel | § 14 BetrSichV | bis zur nächsten Prüfung | [ ] |
| Gefahrstoffverzeichnis | § 6 GefStoffV | aktuell halten | [ ] |

### 2. Dokumentenmappe strukturieren

Schlage eine sinnvolle Ablagestruktur vor, passend zur Situation. Standard-Gliederung:

```
[Tätigkeit/Bereich]/
  01_Situationsaufnahme.md
  02_Regelwerke.md
  03_GBU.md
  04_Betriebsanweisungen/
  05_Unterweisungen/
  06_Wirksamkeitskontrolle.md
  07_Änderungshistorie.md
```

### 3. Änderungshistorie anlegen

| Version | Datum | Änderung | Erstellt von |
|---------|-------|----------|-------------|
| 1.0     | ...   | Erstfassung | ...       |

### Ausgabe

```
## Dokumentationsübersicht

**Tätigkeit/Bereich:** ...
**Letzte Aktualisierung:** ...

### Nachweispflichten-Check
[Tabelle aus Schritt 1 mit Status]

### Ablagestruktur
[Vorschlag aus Schritt 2]

### Nächste Fristen
- GBU-Überprüfung: ...
- Unterweisung (jährlich): ...
- Prüfung Arbeitsmittel: ...
```

Die Dokumentationsmappe ist die Grundlage für `/sifa:begehung`.
