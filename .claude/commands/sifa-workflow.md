# SiFa-Workflow

Orchestriert den vollständigen SiFa-Prozess von der Situationsaufnahme bis zum Tagesbericht.

## Argument

`$ARGUMENTS` — Freitext-Beschreibung der Tätigkeit/Situation **oder** `--interview` für geführten Modus.

## Ablauf

Führe die folgenden Schritte nacheinander aus. Jeder Schritt baut auf den Ergebnissen des vorherigen auf. Fasse nach jedem Schritt die Kernergebnisse in einem **Kontext-Block** zusammen, der an den nächsten Schritt übergeben wird.

---

### Schritt 1 — Situationsaufnahme
Führe `/sifa:situationsaufnahme` mit dem Argument `$ARGUMENTS` aus.
Ergebnis: Strukturiertes Bild der Situation (Tätigkeit, Ort, Personen, Arbeitsmittel, Stoffe).

### Schritt 2 — Regelwerksrecherche
Führe `/sifa:regelwerk-recherche` mit den Ergebnissen aus Schritt 1 aus.
Ergebnis: Liste der relevanten Regelwerke (TRBS, TRGS, DGUV, etc.) mit Fundstellen.

### Schritt 3 — Gefährdungsbeurteilung
Führe `/sifa:gefaehrdungsbeurteilung` mit den Ergebnissen aus Schritt 1 und 2 aus.
Ergebnis: Vollständige GBU mit Gefährdungen, Risikobewertung und Maßnahmen nach STOP.

### Schritt 4 — Betriebsanweisung
Führe `/sifa:betriebsanweisung` mit den Ergebnissen aus Schritt 2 und 3 aus.
Ergebnis: Fertige Betriebsanweisung(en) nach GHS/TRGS-Standard.

### Schritt 5 — Unterweisung
Führe `/sifa:unterweisung` mit den Ergebnissen aus Schritt 3 und 4 aus.
Ergebnis: Unterweisungsplan und -inhalte für die betroffenen Beschäftigten.

### Schritt 6 — Wirksamkeitskontrolle
Führe `/sifa:wirksamkeitskontrolle` mit den Maßnahmen aus Schritt 3 aus.
Ergebnis: Checkliste und Termine zur Überprüfung der Maßnahmen-Wirksamkeit.

### Schritt 7 — Dokumentation
Führe `/sifa:dokumentation` mit allen bisherigen Ergebnissen aus.
Ergebnis: Strukturierte Dokumentationsmappe mit allen Nachweisen.

### Schritt 8 — Begehung
Führe `/sifa:begehung` mit den Ergebnissen aus Schritt 3 und 6 aus.
Ergebnis: Begehungsprotokoll-Vorlage und Begehungsplan.

### Schritt 9 — Tagesbericht
Führe `/sifa:tagesbericht` mit einer Zusammenfassung der heutigen SiFa-Tätigkeiten aus.
Ergebnis: Strukturierter Tagesbericht mit Mängeln, Maßnahmen und offenen Punkten.
Offene Punkte fließen bei Bedarf als Anlassaktualisierung zurück in Schritt 3 (GBU) oder Schritt 6 (Wirksamkeitskontrolle).

---

## Hinweis

Jeder Schritt kann auch einzeln aufgerufen werden, wenn nur ein Teil des Prozesses benötigt wird.
