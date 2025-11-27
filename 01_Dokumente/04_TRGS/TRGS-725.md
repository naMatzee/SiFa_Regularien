

<!-- Seite 1 -->

TRGS 725 (Fassung 5.6.2023) Seite 1 von 36
Ausgabe April 2023
GMBl 2023, S. 727-742 [Nr. 33-34] (v. 5.6.2023)
Gefährliche explosionsfähige
Technische Regeln
Gemische – Mess-, Steuer- und Regelein-
für TRGS 725
richtungen im Rahmen von Explosions-
Gefahrstoffe
schutzmaßnahmen
Die Technischen Regeln für Gefahrstoffe (TRGS) geben den Stand der Technik, Arbeitsmedi-
zin und Arbeitshygiene sowie sonstige gesicherte arbeitswissenschaftliche Erkenntnisse für
Tätigkeiten mit Gefahrstoffen, einschließlich deren Einstufung und Kennzeichnung wieder.
Sie werden vom
Ausschuss für Gefahrstoffe (AGS)
ermittelt bzw. angepasst und vom Bundesministerium für Arbeit und Soziales im Gemeinsa-
men Ministerialblatt bekannt gegeben.
Diese TRGS konkretisiert im Rahmen des Anwendungsbereichs die Anforderungen der Ge-
fahrstoffverordnung (GefStoffV). Bei Einhaltung der Technischen Regel kann der Arbeitgeber
insoweit davon ausgehen, dass die entsprechenden Anforderungen der Verordnungen erfüllt
sind. Wählt der Arbeitgeber eine andere Lösung, muss er damit mindestens die gleiche Si-
cherheit und den gleichen Gesundheitsschutz für die Beschäftigten erreichen.
Inhalt
1 Anwendungsbereich
2 Begriffsbestimmungen
3 Ermittlung der Anforderungen an Ex-Einrichtungen
4 Technische Ausführung der Ex-Einrichtung
5 Prüfung und Kontrolle der Ex-Einrichtung
Anhang 1 Erläuterung der Vorgehensweise an Beispielen zur Zonenreduzierung
Anhang 2 Maßnahmen zur Erkennung, Vermeidung oder Beherrschung des Ausfalls von
Ex-Einrichtungen
Anhang 3 Anforderungen an MSR-Einrichtungen, welche nach dem Stand der Technik be-
triebsbewährt sind
Literaturhinweise
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 2 -->

TRGS 725 (Fassung 5.6.2023) Seite 2 von 36
Inhaltsverzeichnis
1 Anwendungsbereich 3
2 Begriffsbestimmungen 3
2.1 Betriebsbewährte Technik 3
2.2 Betriebskonzept 4
2.3 Bewährte Technik 4
2.4 Ex-Einrichtungen 4
2.5 Funktionseinheit 5
2.6 Funktionseinheit, einfach 5
2.7 Funktionseinheit, komplex 5
2.8 Funktionseinheit, abhängig 6
2.9 Funktionseinheit, unabhängig 6
2.10 Hardwarefehlertoleranz (HFT) 6
2.11 MSR-Einrichtungen 6
2.12 Redundanz 6
2.13 Klassifizierungsstufe 6
2.14 Sicherheitsfunktion 6
2.15 Verfügbarkeit der Explosionsschutzmaßnahmen 6
2.16 Zuverlässigkeit der Ex-Einrichtung 7
3 Ermittlung der Anforderungen an Ex-Einrichtungen 7
3.1 Grundsätze 7
3.2 Gefährdungsbeurteilung 8
3.3 Bewertung der Ex-Einrichtung 12
3.4 Ermittlung der erreichbaren Zonenreduzierung durch Ex-Einrichtungen 12
3.5 Ermittlung der erreichbaren Zündquellenvermeidung durch Ex-Einrichtungen 14
3.6 Ex-Einrichtungen zur Reduzierung der Auswirkungen einer Explosion 15
4 Technische Ausführung der Ex-Einrichtung 17
4.1 Technische Ausführung der Ex-Einrichtung mit Methoden der funktionalen
Sicherheit 17
4.2 Technische Ausführungen von Ex-Einrichtungen, die im Sinne dieser TRGS
bewertet werden 19
4.2.1 Allgemeines 19
4.2.2 Technische Ausführung von Ex-Einrichtungen mit einer Klassifizierungsstufe K1 19
4.2.3 Technische Ausführung von Ex-Einrichtungen zur Erfüllung der Klassifizierungs-
stufen K2 oder K3 21
4.2.4 Technische Ausführung von Ex-Einrichtungen, die in Teilen abhängig sind 25
5 Prüfung und Kontrollen der Ex-Einrichtung 26
Anhang 1 Erläuterung der Vorgehensweise an Beispielen zur Zonenreduzierung 27
A1.1 Lüftung 27
A1.2 Inertisierung 28
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 3 -->

TRGS 725 (Fassung 5.6.2023) Seite 3 von 36
A1.3 Flüssigkeitsverschluss 30
A1.4 Taumeltrockner 30
A1.5 Förderung von Feststoff mit Stickstoff 31
Anhang 2 Maßnahmen zur Erkennung, Vermeidung oder Beherrschung des Ausfalls von
Ex-Einrichtungen 33
Anhang 3 Anforderungen an die Betriebsbewährung der Funktionseinheiten von Ex-
Einrichtungen 35
Literaturhinweise 36
1 Anwendungsbereich
(1) Diese TRGS beschreibt die Vorgehensweise zur Ermittlung der erforderlichen Zuverläs-
sigkeit von sicherheitsrelevanten Mess-, Steuer-, und Regeleinrichtungen (Ex-Einrichtungen)
als Bestandteil von Explosionsschutzmaßnahmen nach TRGS 722 „Vermeidung oder Ein-
schränkung gefährlicher explosionsfähiger Gemische“, TRGS 723 „Gefährliche explosionsfä-
hige Gemische – Vermeidung der Entzündung gefährlicher explosionsfähiger Gemische“ und
TRGS 724 „Gefährliche explosionsfähige Gemische - Maßnahmen des konstruktiven Explosi-
onsschutzes, welche die Auswirkung einer Explosion auf ein unbedenkliches Maß beschrän-
ken“ sowie die Anforderungen zur Erreichung der erforderlichen Explosionssicherheit von An-
lagen in explosionsgefährdeten Bereichen (Ex-Anlagen).
(2) Diese TRGS beinhaltet die Betrachtung verschiedener Methoden zur Bewertung der Zu-
verlässigkeit der Ex-Einrichtung.
(3) Diese TRGS gilt sowohl für einfache als auch für komplexe Mess-, Steuer-, und Re-
geleinrichtungen (d.h. z.B. mechanische, pneumatische, hydraulische, elektrische, elektroni-
sche oder auch programmierbare elektronische MSR-Einrichtungen).
(4) Die Bewertung der Eignung und Funktionsfähigkeit technischer Maßnahmen sowie die
Eignung organisatorischer Maßnahmen erfolgt nach TRGS 722 bis TRGS 724 und ist nicht
Bestandteil dieser TRGS.
(5) Macht der Arbeitgeber von der Möglichkeit Gebrauch, gemäß Anhang I Nummer 1.6
Absatz 3 GefStoffV von einer Zoneneinteilung abzusehen, sind grundsätzlich die gemäß die-
ser technischen Regel für die Zone 0 bzw. 20 angegebenen Schutzmaßnahmen zu treffen.
Abweichungen hiervon sind zulässig, wenn diese in der Dokumentation der Gefährdungsbe-
urteilung nach § 6 Absatz 9 GefStoffV begründet festgelegt werden.
2 Begriffsbestimmungen
2.1 Betriebsbewährte Technik
Betriebsbewährte Technik liegt vor, wenn die Eignung der Mess-, Steuer- und Regeleinrich-
tungen (MSR-Einrichtung) für den Anwendungsfall gemäß Anhang 3 nachgewiesen ist. Bei
betriebsbewährten Funktionseinheiten hat sich in der Bewährungsphase gezeigt, dass weder
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 4 -->

TRGS 725 (Fassung 5.6.2023) Seite 4 von 36
in der Hardware noch in der Betriebssoftware eventuell vorhandene systematische Fehler die
sicherheitstechnische Funktion der Funktionseinheit beeinträchtigen.
2.2 Betriebskonzept
Zum Betriebskonzept zählen alle Einrichtungen sowie Prozess- und Betriebsbedingungen, die
für den bestimmungsgemäßen Betrieb der Anlage einschließlich prozessnotwendiger Zu-
stände, z. B. An- oder Abfahren, oder die ordnungsgemäße Durchführung einer Tätigkeit er-
forderlich sind (s.a. TRGS 722). Auch MSR-Einrichtungen können Teil des Betriebskonzeptes
sein. Diese gelten aber nicht als Ex-Einrichtung im Sinne dieser TRGS, da mit ihrer Hilfe zwar
Betriebsparameter beobachtet werden, die Hinweise auf explosionsschutzrelevante Abwei-
chungen geben können, ohne dass die MSR-Einrichtung für diesen Zweck konzipiert ist.
2.3 Bewährte Technik
(1) Bewährte Technik liegt vor, wenn grundlegende und bewährte Sicherheitsprinzipien er-
füllt sind, durch:
1. Verwendung für den Anwendungsfall bewährter und zuverlässiger Installationstechnik
und
2. geeignete Auswahl, Kombination, Anordnung, Zusammenbau und Einbau von Funkti-
onseinheiten unter Berücksichtigung der Anwendungshinweise der Hersteller sowie von
Erfahrungen mit ähnlichen Bauteilen
um ein angemessenes Maß an Sicherheit nach dem Stand der Technik zu erreichen. Im Hin-
blick auf die geeignete Auswahl nach Nummer 2 ist auch der Betrieb der verwendeten Bauteile
innerhalb der Einsatzparameter sowie die Betriebsanleitung der Hersteller (insbesondere Hin-
weise zu dauerhaftem Betrieb und Wartung und Instandhaltung) zu berücksichtigen.
(2) Dies gilt z. B. als erfüllt, wenn die Vorgehensweisen und Bedingungen gemäß DIN EN
ISO 13849-2:2013-02 Tabellen 1 und 2 berücksichtigt sind. Als hinsichtlich ihrer Zuverlässig-
keit geeignet können auch Funktionseinheiten angesehen werden, für die der Hersteller der
Funktionseinheit eine entsprechende SIL capability nach DIN EN 61508 bzw. ein SIL claim
limit nach DIN EN 62061 oder einen Protection Level nach DIN EN ISO 13849 bescheinigt hat.
2.4 Ex-Einrichtungen
(1) Ex- Einrichtungen sind sicherheitsrelevante MSR-Einrichtungen im Sinne der Explosi-
onssicherheit. Ex-Einrichtungen führen die in der Gefährdungsbeurteilung festgelegten Sicher-
heitsfunktionen von Explosionsschutzmaßnahmen nach TRGS 722, TRGS 723 oder TRGS
724 aus.
(2) Ex- Einrichtungen dienen zur Erreichung der Explosionssicherheit im Zusammenhang
mit:
1. Reduzierung der Eintrittswahrscheinlichkeit oder der Dauer des Vorhandenseins gefähr-
licher explosionsfähiger Gemische, z. B.
a) Volumenstrommessung einer technischen Lüftung mit Alarmierung und nachfol-
genden organisatorischen Maßnahmen,
b) Druckmessung einer Inertisierung mit Abschaltung der Entnahmepumpe,
c) Gaswarngeräte mit Zuschaltung einer zusätzlichen Lüftung,
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 5 -->

TRGS 725 (Fassung 5.6.2023) Seite 5 von 36
2. Reduzierung der Wahrscheinlichkeit für das Wirksamwerden von Zündquellen, z.
B.
a) Temperaturmessung mit Abschaltung der Geräte
b) Durchflussmessung mit Abschaltung einer Pumpe (Trockenlaufschutz)
c) Füllstandsmessung mit Alarmierung und nachfolgenden organisatorischen Maß-
nahmen,
3. Verringerung der Auswirkungen einer Explosion auf ein unbedenkliches Maß. z. B. Tem-
peraturmessung an einer Rückzündsicherung (Vermeidung von Dauerbrand) mit Unterbre-
chung der Abgaszufuhr
2.5 Funktionseinheit
Eine Funktionseinheit ist ein Teil einer Ex-Einrichtung. Eine Ex-Einrichtung kann aus mehreren
Funktionseinheiten bestehen, die funktional miteinander in Beziehung stehen. Funktionsein-
heiten können einfach oder komplex sein.
2.6 Funktionseinheit, einfach
Eine einfache Funktionseinheit ist eine Funktionseinheit, deren Fehlerverhalten (z.B. in wel-
cher Richtung ein Ausfall erfolgt oder mit welcher Häufigkeit und Dauer) in einer Fehleranalyse
eindeutig beschreibbar ist, wie z. B. mechanische, pneumatische, elektrische Bauelemente
oder festverdrahtete Logiksysteme aus elektromechanischen Bauteilen. Die Ursache-Wir-
kungskette ist bei diesen Funktionseinheiten eindeutig bestimmbar. Beispiele für einfache
Funktionseinheiten sind:
1. Schmelzeinsätze (wie in Flüssigkeitskupplungen benutzt),
2. Fliehkraftregler,
3. thermostatische Ventile,
4. Überdruckventile,
5. Druck-, Temperatur-, Durchfluss-, Füllstandsüberwachungseinrichtungen ohne elektro-
nische Komponenten, die unmittelbar eine Abschaltung generieren.
2.7 Funktionseinheit, komplex
(1) Bei diesen Funktionseinheiten wird die Sicherheitsfunktion der Ex-Einrichtung durch
komplexe Technologien umgesetzt. Das Fehlerverhalten solcher Funktionseinheiten, wie z. B.
einer parametrierbaren oder programmierbaren elektronischen Schaltung, kann nicht durch
einfache Fehlerbetrachtungen untersucht werden.
(2) Komplexe Funktionseinheiten sind beispielsweise
1. Gaswarngeräte,
2. Temperatur-,
3. Durchfluss-,
4. Füllstandsmessungen,
die über eine elektronische Schaltung, eine programmierte Steuerung oder ein Prozessleit-
system eine vorgesehene Sicherheitsfunktion ausführen.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 6 -->

TRGS 725 (Fassung 5.6.2023) Seite 6 von 36
2.8 Funktionseinheit, abhängig
Funktionseinheiten in einer Sicherheitsfunktion sind als abhängig zu bewerten, wenn bei Aus-
fall einer Funktionseinheit die Sicherheitsfunktion insgesamt ausfällt (Reihenschaltung).
2.9 Funktionseinheit, unabhängig
Eine Funktionseinheit in einer Sicherheitsfunktion ist als unabhängig zu bewerten, wenn bei
ihrem Ausfall die Sicherheitsfunktion erhalten bleibt (Parallelschaltung).
2.10 Hardwarefehlertoleranz (HFT)
Die Hardwarefehlertoleranz gibt an, mit wie vielen Fehlern die Ex-Einrichtung noch sicher be-
trieben werden kann.
2.11 MSR-Einrichtungen
MSR-Einrichtungen sind Einrichtungen der Mess-, Steuer- und Regeltechnik. Im Sinne dieser
TRGS gehören auch die Einrichtungen der Prozessleittechnik (PLT-Einrichtungen) zu den
MSR-Einrichtungen.
2.12 Redundanz
Redundanz bedeutet, dass durch das mehrfache Vorhandensein von Funktionseinheiten, die
für den störungsfreien Normalbetrieb nicht benötigt werden, die Verfügbarkeit erhöht wird.
2.13 Klassifizierungsstufe
Die Klassifizierungsstufe beschreibt den Grad der erforderlichen Zuverlässigkeit einer Ex-Ein-
richtung oder Funktionseinheit.
2.14 Sicherheitsfunktion
Die Sicherheitsfunktion einer Ex-Einrichtung besteht darin, die in der Gefährdungsbeurteilung
festgelegte Explosionsschutzmaßnahme nach TRGS 722, TRGS 723 oder TRGS 724 sicher-
zustellen oder aufrecht zu erhalten.
2.15 Verfügbarkeit der Explosionsschutzmaßnahmen
Die Verfügbarkeit beschreibt wie robust eine Explosionsschutzmaßnahme ist. In die Bewer-
tung der Verfügbarkeit gehen sowohl zeitliche Aspekte als auch Redundanzen ein. Die Ver-
fügbarkeit einer Explosionsschutzmaßnahme ist
1. ausreichend, wenn die Explosionsschutzmaßnahme während des Normalbetriebs zur
Verfügung steht. Ausfälle können auftreten, dürfen aber nicht häufig vorkommen.
2. hoch, wenn mit dem Ausfall der Explosionsschutzmaßnahme während des Normalbe-
triebs und bei vorhersehbaren Störungen nicht zu rechnen ist. Ein Ausfall bei seltenen
Störungen ist zulässig.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 7 -->

TRGS 725 (Fassung 5.6.2023) Seite 7 von 36
3. sehr hoch, wenn mit dem Ausfall der Explosionsschutzmaßnahme während des Nor-
malbetriebs, bei vorhersehbaren Störungen und auch bei seltenen Störungen nicht zu
rechnen ist.
Die Bewertung der Verfügbarkeit der Explosionsschutzmaßnahme nach TRGS 722, TRGS
723 oder TRGS 724 erfolgt qualitativ im Rahmen der Gefährdungsbeurteilung.
2.16 Zuverlässigkeit der Ex-Einrichtung
Die Zuverlässigkeit der Ex-Einrichtung ist die Fähigkeit eine geforderte Sicherheitsfunktion un-
ter vorgegebenen Bedingungen im Anforderungsfall auszuführen. Die Zuverlässigkeit im
Sinne dieser TRGS kann qualitativ oder quantitativ bewertet werden (s.a. Abschnitt 3.3).
3 Ermittlung der Anforderungen an Ex-Einrichtungen
3.1 Grundsätze
(1) In der Gefährdungsbeurteilung zum Explosionsschutz nach § 6 GefStoffV werden unter
Berücksichtigung von TRGS 720 „Gefährliche explosionsfähige Gemische – Allgemeines“ und
TRGS 721 „Gefährliche explosionsfähige Gemische – Beurteilung der Explosionsgefährdung“
Explosionsschutzmaßnahmen entsprechend den Anforderungen der GefStoffV unter Berück-
sichtigung TRGS 722, TRGS 723 und TRGS 724 festgelegt.
Abbildung 1: Explosionsschutzkonzept.
(2) Ausgehend von der TRGS 721 werden bei der Entwicklung des Explosionsschutzkon-
zeptes die Explosionsschutzmaßnahmen zur Vermeidung der Bildung gefährlicher explosions-
fähiger Gemische, zur Vermeidung wirksamer Zündquellen und zur Auswirkungsbegrenzung
festgelegt. Dabei kann von Teilen des Betriebskonzepts Gebrauch gemacht werden, soweit
diese einen Beitrag zum Explosionsschutzkonzept beinhalten (weißer Pfeil in Abbildung 1).
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 8 -->

TRGS 725 (Fassung 5.6.2023) Seite 8 von 36
Die für die Entwicklung des Explosionsschutzkonzeptes verwendeten Teile des Betriebskon-
zeptes müssen in der Gefährdungsbeurteilung nachvollziehbar dokumentiert werden.
(3) Die Bewertung, inwieweit im Rahmen des geplanten Explosionsschutzkonzepts zur Er-
reichung der Explosionssicherheit (Sollzustand) Ex-Einrichtungen erforderlich sind, ergibt sich
durch den Vergleich der bereits getroffenen Explosionsschutzmaßnahmen (grauer Bereich:
Explosionsschutzmaßnahme ohne Ex-Einrichtung in Abbildung 1) mit dem erforderlichen Soll-
zustand.
(4) Sind Ex-Einrichtungen (schraffierter Bereich) vorhanden, sind sie Teil des Explosions-
schutzkonzeptes. Sie dienen dazu, Abweichungen vom Soll-Zustand zu erkennen und weitere
Explosionsschutzmaßnahmen einzuleiten. Diese weiteren Explosionsschutzmaßnahmen kön-
nen technisch oder organisatorisch sein, z. B. Erkennung des Ausfalls der Lüftung mit Ergrei-
fen zusätzlicher Maßnahmen oder Erkennen heißer Oberflächen mit Ergreifen zusätzlicher
Maßnahmen.
(5) Die im Explosionsschutzkonzept definierten Explosionsschutzmaßnahmen können eine
oder mehrere Ex-Einrichtungen enthalten.
(6) Für die Festlegung der Anforderungen an die Ex-Einrichtung ist zunächst die Verfügbar-
keit der Explosionsschutzmaßnahme nach TRGS 722 bis TRGS 724 ((grauer Bereich in Ab-
bildung 1), ohne Berücksichtigung der Ex-Einrichtungen) zu bewerten. Organisatorische Maß-
nahmen als Teil der Explosionsschutzmaßnahmen sind hinsichtlich ihres Beitrags und ihrer
Eignung im Rahmen der Gefährdungsbeurteilung zu bewerten. Für technische Maßnahmen
kann bei Verwendung bewährter Technik ohne weitere Festlegungen zunächst von einer aus-
reichenden Verfügbarkeit der Explosionsschutzmaßnahme ausgegangen werden. Wird von
einer hohen oder sehr hohen Verfügbarkeit der Explosionsschutzmaßnahme ausgegangen,
ist dies in der Gefährdungsbeurteilung zu dokumentieren.
(7) Erreicht die Explosionsschutzmaßnahme ohne Ex-Einrichtung (grauer Pfeil in Abbildung
1) nicht die erforderliche Reduzierung der Explosionsgefährdung, z. B. weil der Ausfall der
Explosionsschutzmaßnahme nicht rechtzeitig erkannt wird, kann eine zusätzliche Reduzie-
rung durch Ex-Einrichtungen (schraffierter Pfeil in Abbildung 1) nach dieser TRGS erreicht
werden.
(8) Die geforderte Reduzierung der Explosionsgefährdung kann auch ausschließlich mit
Hilfe von Ex-Einrichtungen erreicht werden (Anteilsgröße des schraffierten Pfeils in Abbildung
1).
(9) Der Beitrag zur Reduzierung der Explosionsgefährdung, den die Ex-Einrichtungen
(schraffierter Pfeil in Abbildung 1) liefern, wird als Klassifizierungsstufe beschrieben (gestri-
chelter Strich in Abbildung 1) und ist in der Gefährdungsbeurteilung in geeigneter Form zu
dokumentieren.
(10) Die Vorgehensweise wird, ausgehend von einer vorliegenden Gefährdungsbeurteilung,
an Beispielen zur Zonenreduzierung in Anhang 1 erläutert.
3.2 Gefährdungsbeurteilung
(1) Aus der Gefährdungsbeurteilung nach § 6 GefStoffV geht hervor, ob ein Betriebskonzept
im Sinne dieser TRGS vorliegt und welche Explosionsschutzmaßnahmen ergriffen werden
müssen, um die Wahrscheinlichkeit für das Auftreten von gefährlicher explosionsfähiger At-
mosphäre (Zoneneinteilung) und von wirksamen Zündquellen (Zündquellenvermeidung) auf
ein angemessenes Maß zu reduzieren oder, soweit dies nicht allein ausreichend möglich ist,
um die Auswirkungen von Explosionen auf ein unbedenkliches Maß zu verringern.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 9 -->

TRGS 725 (Fassung 5.6.2023) Seite 9 von 36
(2) Explosionsschutzmaßnahmen nach TRGS 722 bis 724 können z.B. sein:
1. Zonenreduzierung (Auftrittswahrscheinlichkeit und räumliche Ausdehnung einer
gefährlichen explosionsfähigen Atmosphäre),
2. Zündquellenvermeidung (z.B. bei atmosphärischen Bedingungen durch Installa-
tion von geeigneten Geräten gemäß der Richtlinie 2014/34/EU),
3. Begrenzung der Explosionsauswirkungen auf ein unbedenkliches Maß (z.B. bei
atmosphärischen Bedingungen durch Schutzsysteme gemäß der Richtlinie
2014/34/EU).
(3) Maßnahmen gegen Explosionen sind als ausreichend sicher zu bewerten, wenn entwe-
der das Explosionsereignis als sehr selten einzustufen ist oder wenn die Auswirkungen einer
Explosion auf ein unbedenkliches Maß reduziert sind.
(4) Das Explosionsschutzkonzept wird entsprechend TRGS 722, TRGS 723 und TRGS 724
entwickelt. Die einzelnen Explosionsschutzmaßnahmen werden hinsichtlich ihrer erforderli-
chen Verfügbarkeit bewertet. Eine geeignete Ausführung der technischen Maßnahmen zum
Explosionsschutz wird vorausgesetzt. Ergibt die Bewertung, dass zur Erreichung der benötig-
ten Verfügbarkeit der Ex-Schutzmaßnahme zusätzliche Ex-Einrichtungen erforderlich sind,
z.B. um den Ausfall der Explosionsschutzmaßnahme zu identifizieren, wird der erforderliche
Beitrag der Ex-Einrichtung ermittelt (s.a. Abbildung 2).
(5) Soweit erforderlich, hat der Arbeitgeber die Ex-Einrichtung (räumlich und funktional) dar-
zustellen sowie deren Beitrag zur Reduzierung der Explosionsgefährdung qualitativ zu be-
schreiben.
(6) Werden Ex-Einrichtungen benötigt, sind die Anforderungen an die Klassifizierungsstufen
in der Gefährdungsbeurteilung festzulegen.
(7) Die in Tabelle 1 dargestellten Anforderungen an die Verfügbarkeit der Explosionsschutz-
maßnahmen sind nur anwendbar, wenn das Auftreten gefährlicher explosionsfähiger Atmo-
sphären und das Wirksamwerden von Zündquellen voneinander unabhängig sind.
(8) Die Fälle, in denen keine Unabhängigkeit zwischen dem Auftreten der gefährlichen ex-
plosionsfähigen Atmosphäre und der Zündquelle gegeben ist, erfordern eine gesonderte Be-
trachtung in der Gefährdungsbeurteilung.
(9) Das Explosionsschutzkonzept kann aus Maßnahmen zur Zonenreduzierung, zur Zünd-
quellenvermeidung, zur Begrenzung der Explosionsauswirkungen oder aus Kombinationen
bestehen. Durch unabhängige, redundante Ausführung kann die Verfügbarkeit einer Explosi-
onsschutzmaßnahme erhöht werden.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 10 -->

TRGS 725 (Fassung 5.6.2023) Seite 10 von 36
Tabelle 1: Erforderliche Verfügbarkeit von Explosionsschutzmaßnahmen in Abhän-
gigkeit der Wahrscheinlichkeit des Auftretens einer gefährlichen explosi-
onsfähigen Atmosphäre und einer wirksamen Zündquelle
Zone auf Basis des Be- Zone 0/20 Zone 1/21 Zone 2/22 keine Zone
triebskonzepts
Zündquellen-
Erforderliche Verfügbarkeit einer Explosionsschutzmaßnahme
bewertung auf Basis
des Betriebskonzeptes
Zündquelle im Normalbetrieb Keine weiteren
(betriebsmäßig) vorhanden sehr hoch hoch ausreichend Maßnahmen
erforderlich
Zündquelle im vorhersehbaren Keine weiteren Keine weiteren
Fehlerfall oder bei gelegentli- Maßnahmen Maßnahmen
hoch ausreichend
chen Betriebsstörungen vorhan- erforderlich erforderlich
den
Zündquelle im seltenen Fehler- Keine weiteren Keine weiteren Keine weiteren
fall oder bei seltenen Betriebs- ausreichend Maßnahmen Maßnahmen Maßnahmen
störungen vorhanden erforderlich erforderlich erforderlich
Keine weiteren Keine weiteren Keine weiteren Keine weiteren
Zündquelle im sehr seltenen Maßnahmen Maßnahmen Maßnahmen Maßnahmen
Fehlerfall vorhanden erforderlich erforderlich erforderlich erforderlich
(10) Die erforderliche Verfügbarkeit einer Explosionsschutzmaßnahme ist abhängig von der
Wahrscheinlichkeit des Auftretens einer gefährlichen explosionsfähigen Atmosphäre und der
Wahrscheinlichkeit des Auftretens einer wirksamen Zündquelle (siehe Tabelle 1). Dabei ist
entsprechend TRGS 721 ein hohes Schadensausmaß zugrunde gelegt. Hinsichtlich der An-
forderungen an die Zuverlässigkeit von Ex-Einrichtungen zur Reduzierung der Auswirkungen
einer Explosion siehe Abschnitt 3.6.
(11) Ergibt die Bewertung der Explosionsschutzmaßnahme, dass die erforderliche Verfüg-
barkeit ohne Ex-Einrichtung nicht erreicht wird, kann durch Einsatz von geeigneten Ex-Einrich-
tungen die erforderliche Explosionssicherheit erreicht werden. Der erforderliche Beitrag der
Ex-Einrichtungen (der erforderliche Grad der Zuverlässigkeit) kann Abbildung 3 bis Abbildung
8 entnommen werden.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 11 -->

TRGS 725 (Fassung 5.6.2023) Seite 11 von 36
Abbildung 2: Vorgehensweise der Gefährdungsbeurteilung im Anwendungsbereich
der TRGS 725.
Vermeidung
explosionsfähiger Vermeidung der Entzündung
Beschränkung der
Auswirkungen
Gemische
(TRGS 723)
(TRGS 722) (TRGS 724)
Bewertung der Explosionssicherheit
durch Betriebskonzept bzwE. xplosionsschutzmaßnahme
(ohne Ex-Einrichtung)
Ja
Erforderliche
Ende
Explosionssicherheit
erreicht?
Nein
Bestimmung der notwendigen Klassifizierungsstufe Anwendungs-
der Ex- E inrichtung bereich
TRGS 725
Umsetzung der Ex - Einrichtung
Abschnitt 4.2 Funktionale Sicherheit Abschnitt 4.1
Methodik
SafetyIntegrity Level (SIL)
der
TRGS 725
Performance Level (PL)
Zündquellenüberwachung (Typ b1/b2)
Ende
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 12 -->

TRGS 725 (Fassung 5.6.2023) Seite 12 von 36
(12) Zur Einteilung von explosionsgefährdeten Bereichen in Zonen siehe Anhang I Nummer
1.6 Absatz 3 GefStoffV und TRGS 720. Bei explosionsfähigen Gemischen unter nicht atmo-
sphärischen Bedingungen kann diese Betrachtung analog angewendet werden.
3.3 Bewertung der Ex-Einrichtung
(1) Die Anforderungen an die Zuverlässigkeit einer Ex-Einrichtung werden für diese TRGS
im Folgenden definiert. Die Kontrolle der sicheren Funktion ist hinsichtlich Umfang und Fristen
in der Gefährdungsbeurteilung festzulegen, um Ausfälle der Sicherheitsfunktion zu erkennen.
In der Gefährdungsbeurteilung ist festzulegen, ob bei Ausfall Folgemaßnahmen erforderlich
sind. Die Zuverlässigkeit ist
1. ausreichend, wenn die Ex-Einrichtung normalerweise zur Verfügung steht. Ausfälle kön-
nen auftreten, dürfen aber nicht häufig vorkommen. Dies ist zum Beispiel durch den Ein-
satz bewährter Technik gewährleistet,
2. hoch, wenn die Ex-Einrichtung während des Normalbetriebs zur Verfügung steht und bei
einem vorhersehbaren Fehler ein Ausfall der von der Ex-Einrichtung ausgeführten Si-
cherheitsfunktion nicht unterstellt werden muss. Unterbrechungen sind zulässig, sofern
sie nicht häufig vorkommen. Dies ist z.B. der Fall bei Bruch einer Feder/Membran am
Druckminderer,
3. sehr hoch, wenn die Ex-Einrichtung ständig verfügbar ist, dies ist z.B. dann der Fall,
wenn weder ein seltener noch ein vorhersehbarer Fehler zu einem Ausfall der von der
Ex- Einrichtung ausgeführten Sicherheitsfunktion führt. Ein Fehler gilt als selten, wenn
z. B. zwei voneinander unabhängige vorhersehbare Fehler, die nur in Kombination mit-
einander die Funktion beeinträchtigen, gemeinsam auftreten. Die Zuverlässigkeit ist in
diesem Fall dauerhaft sichergestellt. Ein Ausfall ist nach Maßgabe der technischen Ver-
nunft nicht zu erwarten.
(2) Die Zuverlässigkeit von Ex-Einrichtungen kann durch Klassifizierungsstufen ausgedrückt
werden. Die folgende Tabelle 2 beschreibt den Zusammenhang zwischen der Zuverlässigkeit
der Ex-Einrichtung und den erreichbaren Klassifizierungsstufen qualitativ.
Tabelle 2: Erzielbare Klassifizierungsstufen für Ex-Einrichtungen (Zuverlässigkeit der
Ex-Einrichtung)
Zuverlässigkeit der
sehr hoch hoch ausreichend
Ex-Einrichtung
erzielbare Klassifizierungsstufe der
K3 K2 K1
Ex-Einrichtung
3.4 Ermittlung der erreichbaren Zonenreduzierung durch Ex-Einrichtungen
(1) Die erforderliche Klassifizierungsstufe der Ex-Einrichtungen zur Erreichung der Zielzone
kann in Abhängigkeit von Ausgangssituation und Verfügbarkeit der Explosionsschutzmaß-
nahme (ohne Ex-Einrichtung) Abbildung 3 bis Abbildung 5 entnommen werden.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 13 -->

TRGS 725 (Fassung 5.6.2023) Seite 13 von 36
Abbildung 3: Bestimmung der erforderlichen Klassifizierungsstufe in Abhängigkeit
von der Ausgangssituation („Zone 0/20“) und der Verfügbarkeit der
Explosionsschutzmaßnahme ohne Ex-Einrichtung
Abbildung 4: Bestimmung der erforderlichen Klassifizierungsstufe in Abhängigkeit
von der Ausgangssituation („Zone 1/21“) und der Verfügbarkeit der
Explosionsschutzmaßnahme ohne Ex-Einrichtung
Abbildung 5: Bestimmung der erforderlichen Klassifizierungsstufe in Abhängigkeit
von der Ausgangssituation („Zone 2/22“) und der Verfügbarkeit der
Explosionsschutzmaßnahme ohne Ex-Einrichtung
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 14 -->

TRGS 725 (Fassung 5.6.2023) Seite 14 von 36
3.5 Ermittlung der erreichbaren Zündquellenvermeidung durch Ex-Einrichtungen
(1) Die erforderliche Klassifizierungsstufe der Ex-Einrichtungen zur Erreichung der gefor-
derten Zündquellenvermeidung kann in Abhängigkeit von der vorliegenden Zone, der Verfüg-
barkeit der Explosionsschutzmaßnahme (ohne Ex-Einrichtung) und dem Auftreten von Zünd-
quellen den Abbildungen Abbildung 6 bis Abbildung 8 entnommen werden.
Abbildung 6: Bestimmung der erforderlichen Klassifizierungsstufe der Ex-Einrich-
tung zur Zündquellenüberwachung in Abhängigkeit der vorliegenden
Zündquelle für Zone 0/20
Abbildung 7: Bestimmung der erforderlichen Klassifizierungsstufe der Ex-Einrich-
tung zur Zündquellenüberwachung in Abhängigkeit der vorliegenden
Zündquelle für Zone 1/21
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 15 -->

TRGS 725 (Fassung 5.6.2023) Seite 15 von 36
Abbildung 8: Bestimmung der erforderlichen Klassifizierungsstufe der Ex-Einrich-
tung zur Zündquellenüberwachung in Abhängigkeit der vorliegenden
Zündquelle für Zone 2/22
(2) Wird für den Einsatz von Geräten nach Richtlinie 2014/34/EU vom Hersteller in der Be-
triebsanleitung die Einhaltung bestimmter Prozessbedingungen gefordert, kann die Bewertung
in Abhängigkeit vom Explosionsschutzkonzept mit der Systematik dieser TRGS durch den Be-
treiber erfolgen, sofern Ex-Einrichtungen erforderlich sind.
(3) Sofern Geräte nach RL 2014/34/EU nicht verfügbar sind, nicht der geforderten Kategorie
entsprechen oder nicht entsprechend eingesetzt werden können, ist bei der Gefährdungsbe-
urteilung zu ermitteln, welche Verfügbarkeit erforderliche Explosionsschutzmaßnahmen (ohne
Ex-Einrichtungen) besitzen müssen oder welche Ex-Einrichtungen zusätzlich benötigt werden,
um die erforderliche Verfügbarkeit der Explosionsschutzmaßnahmen zu erreichen.
3.6 Ex-Einrichtungen zur Reduzierung der Auswirkungen einer Explosion
(1) Explosionsschutzmaßnahmen zur Reduzierung der Auswirkungen einer Explosion kön-
nen z. B. Schutzsysteme im Sinne der TRGS 724 sein. Damit diese Explosionsschutzmaß-
nahmen ausreichend verfügbar sind, können Ex-Einrichtungen erforderlich sein.
(2) Basis für diese Betrachtung ist, dass das Explosionsschutzkonzept für eine Anlage nicht
nur auf konstruktiven (siehe TRGS 724) Explosionsschutzmaßnahmen beruht, sondern immer
zusätzlich technische oder organisatorische Explosionsschutzmaßnahmen des vorbeugenden
Explosionsschutzes (siehe TRGS 722 oder TRGS 723) zur Reduzierung der Gefährdung er-
griffen werden, die bereits einen wesentlichen Beitrag zur Risikominderung darstellen.
(3) Autonome Schutzsysteme, die nach Richtlinie 2014/34/EU auf dem Markt bereitgestellt
werden, wurden im Rahmen des Konformitätsbewertungsverfahrens durch den Hersteller be-
wertet. Diese Bewertung umfasst auch MSR-Einrichtungen, die für die sichere Funktion erfor-
derlich sind. Dies können z.B. Detektoren von Explosionsunterdrückungsanlagen oder Lösch-
mittelsperren sein. Daher ist eine Bewertung nach TRGS 725 nicht erforderlich.
(4) Autonome Schutzsysteme können jedoch auch Signale an andere Steuerungssysteme
weitergeben, die zusätzliche Explosionsschutzmaßnahmen auslösen. Die Klassifizierungs-
stufe dieser Ex-Einrichtung wird bestimmt durch den Beitrag, den diese Maßnahmen im Ex-
plosionsschutzkonzept liefern, um die Explosionssicherheit zu erreichen.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 16 -->

TRGS 725 (Fassung 5.6.2023) Seite 16 von 36
(5) Wenn die Verfügbarkeit einer Explosionsschutzmaßnahme ohne Ex-Einrichtungen nicht
ausreichend ist, muss im Rahmen der Gefährdungsbeurteilung ermittelt werden, welche Zu-
verlässigkeit die erforderliche Ex-Einrichtung aufweisen muss.
(6) Beispiele für derartige Explosionsschutzkonzepte können sein:
1. Statische Flammendurchschlagsicherungen, die mit zusätzlichen Detektoren ausgestat-
tet sind.
Beispiel: Temperaturüberwachungen bei kurzbrandsicheren Einrichtungen
Bei Ansprechen werden die Abgasströme umgeleitet, um innerhalb der vom Hersteller
beschriebenen Zeit den Brennstoffnachschub und damit das Anstehen der Flamme an
der Flammendurchschlagsicherung zu stoppen. Die Funktion der Flammendurchschlag-
sicherung hängt von der Einhaltung dieser Randbedingung ab. Die erforderliche Anzahl
der Schutzsysteme wurde auf Grundlage der TRGS 724 festgelegt. Die erforderlichen
Flammendurchschlagsicherungen werden im Rahmen des Explosionsschutzkonzeptes
jeweils mit einer Temperaturüberwachung in Klassifizierungsstufe K1 ausgeführt.
2. Strömungsüberwachte, rückzündsichere Einrichtungen sind in der Regel keine autono-
men Schutzsysteme, die nach RL 2014/34/EU in Verkehr gebracht wurden. In dem vor-
liegenden Fall stellt diese Rückzündsicherung eine Barriere im Sinne der TRGS 724
dar. Daher ist die Strömungsüberwachung hinsichtlich ihrer Zuverlässigkeitsanforderung
in Klassifizierungsstufe K1 auszuführen.
3. Zellenradschleusen werden als autonome Schutzsysteme nach RL 2014/34/EU in Ver-
kehr gebracht und sind für den zu erwartenden Explosionsdruck explosionsfest und
zünddurchschlagsicher ausgeführt. Da jedoch nach einer Explosion brennendes Mate-
rial in nachgelagerte Prozessschritte gefördert werden kann, muss die Zellenrad-
schleuse im Explosionsfall gestoppt werden. Erfolgt das Erkennen der Explosion und
das Stoppen der Zellenradschleuse über einen Detektor, so ist die Ausführung in Klas-
sifizierungsstufe K1 in der Regel ausreichend.
4. In einem Prozess werden zwei zünddurchschlagsichere Schieber als Taktschleuse ge-
nutzt. Dabei sind die Schieber wechselweise geschlossen und gewährleisten damit eine
sichere Entkopplung. In dem vorliegenden Fall ist die Auftretenswahrscheinlichkeit einer
Explosion unter Berücksichtigung der vorliegenden Explosionsschutzmaßnahmen sel-
ten, so dass eine Ausführung der Verriegelung in Klassifizierungsstufe 1 ausreichend ist.
Kann es gelegentlich zu einer Explosion kommen, wäre die Ausführung in Klassifizie-
rungsstufe K2 erforderlich.
5. In einem Prozess wird die explosionstechnische Entkopplung durch Produktüberde-
ckung realisiert. Für erforderliche Ex-Einrichtungen zur Gewährleistung der Produktüber-
deckung gelten die gleichen Überlegungen wie bei der Taktschleuse.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 17 -->

TRGS 725 (Fassung 5.6.2023) Seite 17 von 36
4 Technische Ausführung der Ex-Einrichtung
(1) Die anhand der erforderlichen Klassifizierungsstufen festgelegte Zuverlässigkeit kann
auf unterschiedliche Weise realisiert werden. Bei der Bewertung der Klassifizierungsstufe ei-
ner Ex-Einrichtung ist immer die gesamte Kette (Sensor / Signalverarbeitung / Aktor) zu be-
trachten.
(2) Werden Methoden der funktionalen Sicherheit eingesetzt, sind die in Abschnitt 4.1 dar-
gestellten Anforderungen entsprechend der angegebenen technischen Standards der funktio-
nalen Sicherheit umzusetzen. Die Anforderungen an die Zuverlässigkeit von Ex-Einrichtungen
werden durch diese Umsetzung erfüllt.
(3) Die Umsetzung kann alternativ auch nach der in Abschnitt 4.2 beschriebenen Vorge-
hensweise dieser TRGS erfolgen.
4.1 Technische Ausführung der Ex-Einrichtung mit Methoden der funktionalen Si-
cherheit
(1) Erfolgt die Bewertungen der Ex-Einrichtung nach den Methoden der funktionalen Sicher-
heit, z.B. entsprechend der DIN EN 61511-1:2019, der DIN EN 62061 (VDE 0113-50):2016,
der DIN EN ISO 13849-1:2016 oder der DIN EN ISO 80079-37:2016, können den Ex-Einrich-
tungen entsprechend Tabelle 3 die folgenden Klassifizierungsstufen zugeordnet werden:
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 18 -->

TRGS 725 (Fassung 5.6.2023) Seite 18 von 36
Tabelle 3: Anforderungen an die funktionale Sicherheit in Abhängigkeit von der Klas-
sifizierungsstufe.
(2) Für Ex-Einrichtungen, die nach den Methoden der funktionalen Sicherheit ausgeführt
werden, sind die Vorgaben der funktionalen Sicherheit der einschlägigen Normen (vgl. Litera-
turverzeichnis TRBS 1115) für die jeweilige Ex-Einrichtung einzuhalten. Kommen unterschied-
liche Normen bei der Auslegung in einer Ex-Einrichtung zur Anwendung, ist die Zusammen-
schaltung der Funktionseinheiten im Rahmen der Gefährdungsbeurteilung zu bewerten.
(3) Innerhalb einer Ex-Anlage können auch unterschiedlichen Methoden der funktionalen
Sicherheit zur Umsetzung unterschiedlicher Ex-Einrichtungen verwendet werden.
(4) Ex-Einrichtungen sind vor erstmaliger Inbetriebnahme sowie vor Wiederinbetriebnahme
nach prüfpflichtigen Änderungen im Rahmen der Prüfung der Explosionssicherheit und wie-
derkehrend nach Anhang 2 Abschnitt 3 BetrSichV zu prüfen. Nähere Information hierzu siehe
auch TRBS 1115.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 19 -->

TRGS 725 (Fassung 5.6.2023) Seite 19 von 36
4.2 Technische Ausführungen von Ex-Einrichtungen, die im Sinne dieser TRGS be-
wertet werden
4.2.1 Allgemeines
(1) Eine Ex-Einrichtung setzt sich aus einer oder mehreren Funktionseinheiten zusammen,
die in der Gesamtheit die festgelegte Klassifizierungsstufe erfüllen müssen. Funktionseinhei-
ten können einfach oder komplex sein.
(2) In Abhängigkeit der nach Abschnitt 3 ermittelten Zuverlässigkeit werden an die techni-
sche Ausführung der Ex-Einrichtung unterschiedliche Anforderungen gestellt (s. Tabelle 4).
Als hinsichtlich ihrer Zuverlässigkeit geeignet können auch Funktionseinheiten angesehen
werden, für die der Hersteller der Funktionseinheit eine entsprechende SIL capability nach DIN
EN 61508 bzw. ein SIL claim limit nach DIN EN 62061 oder einen Performance Level (PL)
nach DIN EN ISO 13849-1 bescheinigt hat. Die Anforderungen an die Ex-Einrichtung nach
Tabelle 4 bleiben hiervon unberührt.
(3) Die Zuverlässigkeit der Funktionseinheiten ist durch geeignete Maßnahmen zur Fehler-
vermeidung oder Fehlerbeherrschung sicherzustellen. Dabei sind die Betriebsbedingungen
und vorgesehenen Wartungen oder Kontrollen zu beachten. Dies wird durch die Berücksichti-
gung der allgemeinen Anforderungen nach Anhang 2 erreicht.
(4) Die Anforderungen an die Umsetzung von Klassifizierungsstufen sind in Tabelle 4 fest-
gelegt.
Tabelle 4: Anforderungen an die Ex-Einrichtung bzw. Funktionseinheit.
Klassifizierungsstufe K3 K2 K1
erforderliche Fehlersicher- Zweifehlersicherheit Einfehlersicherheit Im Normalbetrieb si-
heit (HFT = 2; 1oo3)1 (HFT = 1; 1oo2 oder cher
2oo3)1 (HFT = 0; 1oo1)
Hardwarefehlertoleranz
(HFT)
1 Bei Nachweis der Betriebsbewährtheit/Betriebsbewährte Technik (siehe Anhang 3) kann hier
die HFT um eine Stufe reduziert werden (HFT = 1; 1oo2 oder 2oo3 statt HFT = 2 bzw. HFT =
0; 1oo1 statt HFT = 1).
4.2.2 Technische Ausführung von Ex-Einrichtungen mit einer Klassifizierungsstufe K1
(1) Bei Verwendung einfacher Funktionseinheiten kann von einer ausreichenden Zuverläs-
sigkeit der Ex-Einrichtung ausgegangen werden, wenn
1. bewährte und zuverlässige Installationstechnik verwendet wird,
2. Auswahl, Kombination, Anordnung, Zusammenbau und Einbau von Bauteilen unter Be-
rücksichtigung der Anwendungshinweise der Hersteller erfolgt und
3. Erfahrungen mit gleichen oder ähnlichen Bauteilen vorliegen.
(2) Beim Einsatz komplexer Funktionseinheiten kann von einer ausreichenden Zuverlässig-
keit der Ex-Einrichtung ausgegangen werden, wenn die nachfolgenden Anforderungen einge-
halten sind:
1. Erfüllung einschlägiger MSR-Industriestandards für den Zusammenbau der Bauteile,
2. Eignung für den Einsatzfall (z.B. umgebungs- und stoffbedingte Einflussgrößen, appli-
kative Eignung, branchenbewährte Technik),
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 20 -->

TRGS 725 (Fassung 5.6.2023) Seite 20 von 36
3. Positive Erfahrung im Betriebseinsatz, z.B. durch Verwendung bewährter Technik oder
durch Einsatz betriebsbewährter Geräte,
4. Wartung und Inspektion im Rahmen eines Prüfkonzeptes durch Fachpersonal im Sinne
von § 10 Absatz 2 BetrSichV und
5. Verfolgung von Fehlern und Störungen der Ex-Einrichtung und soweit erforderlich Ab-
leitung von Korrekturmaßnahmen.
Ein quantitativer Nachweis der Zuverlässigkeit (z. B. rechnerischer Nachweis) solcher Instal-
lationen ist nicht erforderlich. Eine einkanalige Ausführung ist ausreichend.
(3) Sofern Prozessleitsysteme (PLS) oder speicherprogrammierbare Steuerungen (SPS)
Teil einer Ex-Einrichtungen sind, müssen mindestens nachfolgende Aspekte berücksichtigt
werden:
1. Es sind PLS/SPS und Feldgeräte einzusetzen, die die für betriebliche Aufgaben der
Prozessindustrie erforderliche Eignung besitzen.
2. Beim PLS/SPS werden zentrale Risiken und PLT-Stellen-spezifische Risiken betrach-
tet.
3. Zentrale Risiken betreffen das gesamte PLS/SPS oder wesentliche Teile davon. Die
möglichen Auswirkungen dieser Risiken können mehrere PLT-Stellen gleichzeitig be-
treffen. Zu diesen Risiken gehören beispielsweise:
a) Ausfall zentraler Hardwarekomponenten (Prozessoren, Kommunikationsschnitt-
stellen),
b) Spannungsausfall,
c) Programmierfehler,
d) Cyberbedrohung.
(4) Für PLS/SPS sind die zentralen Risiken zu betrachten und, soweit erforderlich, durch
Festlegung von technischen und organisatorischen Maßnahmen zu minimieren. Für eine aus-
reichende Zuverlässigkeit ist es hinreichend, wenn insbesondere folgende Randbedingungen
gegeben sind:
1. Betreuung und Überwachung des PLS/SPS durch gemäß BetrSichV (vgl. auch TRBS
1115 3.3.1 Absatz 1 Satz 2) fachkundige und durch den Arbeitgeber für die Aufgabe
beauftragte Personen,
2. Zugriffsschutz, d.h. Änderungsmöglichkeit nur für durch den Arbeitgeber für die Auf-
gabe beauftragte Personen,
3. Maßnahmen der Informationssicherheit für das PLS liegen vor,
4. Management zur Durchführung und Prüfung von Änderungen (Management of
Change) liegt vor,
5. Ständige betriebliche Verwendung des PLS, wodurch die Beobachtung des PLS ge-
währleistet ist,
6. Geräte gehen bei Energieausfall in einen vordefiniert sicheren Zustand.
(5) PLT-Stellen-spezifische Risiken betreffen Hardware- bzw. Softwarefehler einzelner PLT-
Stellen. Das Auftreten von Hardwarefehlern wird auf Grund der Verwendung von im Betrieb
eingesetzter Komponenten und der vorliegenden Betriebserfahrung als ausreichend selten
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 21 -->

TRGS 725 (Fassung 5.6.2023) Seite 21 von 36
eingestuft. Fehler bei der Herstellung oder Änderung der Anwendersoftware werden ausrei-
chend vermieden, wenn insbesondere folgende Randbedingungen gegeben sind:
1. dokumentierte Spezifikation der Ex-Einrichtungen im Sinne des Explosionsschutzes,
z.B. im Explosionsschutzdokument oder einer Verriegelungsmatrix,
2. dokumentierte Prüfungen vor Inbetriebnahme und wiederkehrende Prüfungen oder
Kontrollen von MSR-Einrichtungen im Sinne des Explosionsschutzes,
3. festgelegte Vorgehensweise zur Autorisierung und Durchführung von Änderungen und
Erstellung der Software (“Management of Change“) mit Aktualisierung der Dokumenta-
tion und Durchführung geeigneter Tests. (z.B. innerhalb des Anlagenänderungsprozes-
ses).
(6) Anwendungsbeispiel zur Realisierung der Klassifizierungsstufe K1:
1. Der Aufbau der Ex-Einrichtung aus mehreren Funktionseinheiten muss einfach und
nachvollziehbar sein. Die unter Abschnitt 4.2.2 Absatz 1 und 2 aufgeführten Anforde-
rungen sind durch den Arbeitgeber bei der Auswahl zu gewährleisten.
2. Die Funktionseinheiten Sensor, Signalverarbeitung und Aktor haben die in den Blöcken
eingetragene Klassifizierungsstufe (s. Abbildung 9) und sind funktional voneinander ab-
hängig (jedes Element ist notwendig, damit die Sicherheitsfunktion ausgeführt wird).
Die Ex-Einrichtung hat eine Klassifizierungsstufe von K1.
Abbildung 9: Ex-Einrichtung in der Klassifizierungsstufe K1; Reihenschaltung der
Funktionseinheiten Sensor (K2), Verarbeitung (K1) und Aktor (K1).
4.2.3 Technische Ausführung von Ex-Einrichtungen zur Erfüllung der Klassifizierungs-
stufen K2 oder K3
(1) Für einfache Funktionseinheiten in Ex-Einrichtungen mit erhöhter Zuverlässigkeit (hoch
oder dauerhaft sichergestellt) gelten die Anforderung von Abschnitt 4.2.2 analog.
Beispiel: Ex-Einrichtung der Klassifizierungsstufe K2 mit betriebsbewährten Komponenten
Abbildung 10: Ex-Einrichtung in der Klassifizierungsstufe K2 - Reihenschaltung der
Funktionseinheiten Sensor (K2), Verarbeitung (K2) und Aktor (K2).
Wenn die Ex-Einrichtung der Abbildung 10: Ex-Einrichtung in der Klassifizie-
rungsstufe K2 - Reihenschaltung der Funktionseinheiten Sensor (K2), Verarbei-
tung (K2) und Aktor (K2). die Klassifizierungsstufe K2 erfüllen soll, müssen die Funkti-
onseinheiten Sensor, Verarbeitung und Aktor jedes für sich die Klassifizierungsstufe K2
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 22 -->

TRGS 725 (Fassung 5.6.2023) Seite 22 von 36
erfüllen. Dies ist möglich durch Verwendung von Funktionseinheiten, deren Zuverlässig-
keit mindestens als „hoch“ festgelegt wurde.
(2) Komplexe Funktionseinheiten der Klassifizierungsstufen K2 und K3 können nur verwen-
det werden, wenn diese durch den Hersteller oder durch den Arbeitgeber hinsichtlich ihrer
Zuverlässigkeit bewertet sind. Informationen zur Bewertung der Signalverarbeitung können
Anhang 2 entnommen werden, Hinweise zur Betriebsbewährung von Sensoren und Aktoren
finden sich in Anhang 3.
(3) Wird bei komplexen Ex-Einrichtungen die geforderte Zuverlässigkeit durch die Ex-Ein-
richtung in Gänze oder in Teilen nicht unmittelbar erreicht, kann die Zuverlässigkeit durch zu-
sätzliche Ex-Einrichtungen, wie beispielsweise vollständige oder teilweise Redundanz, erhöht
werden (s. Abbildung 11).
Abbildung 11: Zwei Ex-Einrichtungen der Klassifizierungsstufe K1 (unabhängige Re-
dundanz) und einer resultierenden Klassifizierungsstufe 2.
(4) Erfüllen nicht alle Funktionseinheiten die Klassifizierungsstufe K2, kann durch Redun-
danz dieser Funktionseinheiten die Zuverlässigkeit verbessert werden. Indem zu den Elemen-
ten „Verarbeitung“ und „Aktor“ jeweils ein redundantes funktionsidentisches Element geschal-
tet wird oder indem zu den Elementen „Verarbeitung“ und „Aktor“ ein gemeinsames Element
parallelgeschaltet wird, welches die Funktion der Elemente Verarbeitung und Aktor übernimmt.
Letzterer Fall ist in der Abbildung 12 dargestellt und kann wie in Abbildung 13 und Abbildung
14 zusammengefasst werden. Die Zusammenfassungen von Funktionseinheiten verdeutli-
chen die Anwendung der Tabelle 5 (die Ex-Einrichtung erfüllt die Klassifizierungsstufe K2).
Eine Ex-Einrichtung (K2)
Sensor 1 Signalverarbeitung 1 Aktor 1
K2 a K1 b K1 c
Signalverarbeitung 2 Aktor 2
K1 d K1 e
Abbildung 12: Ex-Einrichtung der Klassifizierungsstufe K2
- Reihenschaltung der Funktionseinheit Sensor (a: K2) mit Parallel-
schaltung von Funktionseinheiten Verarbeitung (b/d: K1) und Aktor
(c/e: K1) in einer aktiven Redundanz.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 23 -->

TRGS 725 (Fassung 5.6.2023) Seite 23 von 36
Eine Ex-Einrichtung (K2)
Signalverarbeitung 1 & Aktor 1
Sensor 1
K2 a K1 b + c
Signalverarbeitung 2 & Aktor 2
d + e
Abbildung 13: Ex-Einrichtung der Abbildung 12 mit der Zusammenfassung der Funk-
tionseinheiten Verarbeitung (K1) und Aktor (K1) zu einer gemeinsa-
men Funktionseinheit (Verarbeitung + Aktor: b+c bzw. d+e).
Eine Ex-Einrichtung (K2)
Signalverarbeitung & Aktorik
Sensor
K2 a K2 (b + c)//(d + e)
Abbildung 14: Ex-Einrichtung der Abbildung 13 mit der Zusammenfassung der Funk-
tionseinheiten (Verarbeitung + Aktor: b/c und d/e) nach Tabelle 5 zu
einer gemeinsamen Funktionseinheit (b + c)//(d+e) mit der Klassifizie-
rungsstufe K2.
Beispiele für derartige Fälle finden sich in Abbildung 15 und Abbildung 16.
Abbildung 15: Ex-Einrichtung mit Klassifizierungsstufe K2 (bei Realisierung in einem
gemeinsamen Prozessleitsystem unter Berücksichtigung von Ab-
schnitt 4.2.3 Absatz 6).
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 24 -->

TRGS 725 (Fassung 5.6.2023) Seite 24 von 36
Abbildung 16: Ex-Einrichtung mit Klassifizierungsstufe K2 (bei Realisierung in einem
gemeinsam Prozessleitsystem unter Berücksichtigung von Abschnitt
4.2.3 Absatz 6).
(5) Erfolgt die Umsetzung von zwei oder drei Klassifizierungsstufen durch redundante Ex-
Einrichtungen, müssen diese grundsätzlich unabhängig sein. Abweichungen hiervon sind nur
dann zulässig, wenn dies in der Gefährdungsbeurteilung nach § 6 Absatz 9 GefStoffV (Explo-
sionsschutzdokument) begründet wird.
Tabelle 5: Resultierende Klassifizierungsstufe bei redundanten Ex-Einrichtungen.
Klassifizierungsstufe einer Klassifizierungsstufe der zweiten Resultierende Klassifizierungs-
Ex-Einrichtung Ex-Einrichtung stufe
K11 K11 K22
K2 K11 K33,4
1 Eine Ausführung in bewährter Technik nach Anhang 2 ist ausreichend.
2 Mit zwei Ex-Einrichtungen kann unter Verwendung eines gemeinsamen Prozessleit-
systems (PLS) die Klassifizierungsstufe K2 erreicht werden, wenn die unter 4.2.3
Absatz 6 beschriebenen Anforderungen erfüllt sind.
3 Klassifizierungsstufe K3 ist durch Bildung einer Kombination von einer Ex-Einrich-
tung mit maximal einer weiteren Ex-Einrichtung in Ausführung in bewährter Technik
nach Anhang 2 zulässig.
4 Klassifizierungsstufe K3 ist allein durch eine Kombination von Maßnahmen im Pro-
zessleitsystem (PLS) nicht möglich.
(6) Bei der Umsetzung einer Ex-Einrichtung mit der Klassifizierungsstufe K2 in einem Pro-
zessleitsystem (PLS) muss das Leitsystem nicht redundant ausgeführt sein (s.a. Abbildung 17
bis 17), wenn die Gefährdungsbeurteilung nach Abschnitt 3.2 unter Verwendung der TRGS
720 bis TRGS 724 ergeben hat, dass
1. die Wahrscheinlichkeit eines Ausfalls gemeinsamer Komponenten als ausreichend sel-
ten eingestuft wurde,
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 25 -->

TRGS 725 (Fassung 5.6.2023) Seite 25 von 36
2. eine Explosion nicht unmittelbar durch einen undefinierten Zustand des PLS ausgelöst
werden kann (das bedeutet, dass das Fehlverhalten des PLS eine Explosion nicht kau-
sal nach sich zieht),
3. der sichere Zustand bei zentralem Ausfall des PLS in ausreichend kurzer Zeit durch
technische oder organisatorische Eingriffe wiederherzustellen ist und
4. betriebsmäßige Zündquellen (Zündquellen im Normalbetrieb) nach dem Stand der
Technik ausgeschlossen sind.
(7) Zusätzlich zu den Anforderungen nach Anhang 2 Absatz 7 muss für das PLS hierzu in
der Gefährdungsbeurteilung festgestellt worden sein, dass
1. ein zentraler Ausfall des PLS entsprechend 4.2.2. Absatz 4 bewertet und die dort be-
schriebenen Maßnahmen zur Entdeckung umzusetzen sind,
2. der Ausfall gemeinsam genutzter Komponenten des PLS erkannt wird und Korrektur-
maßnahmen ergriffen werden und
3. ein unbeabsichtigtes Ändern der Ex-Einrichtungen nach dem Stand der Technik verhin-
dert wird.
Abbildung 17: Ex-Einrichtung der Klassifizierungsstufe K2 bei Realisierung als re-
dundante Einrichtungen in einem gemeinsamen Prozessleitsystem.
4.2.4 Technische Ausführung von Ex-Einrichtungen, die in Teilen abhängig sind
(1) Eine abhängige Ex-Einrichtung nutzt Elemente der redundanten Ex-Einrichtung (z. B.
Mehrfachbenutzung von Sensor 1 in Abbildung 15).
(2) Im Falle der abhängigen Funktionseinheiten sind höhere Anforderungen an die Zuver-
lässigkeit der abhängigen Funktionseinheiten (in Abbildung 18: an den Sensor 1) oder an die
Prüffrist zu stellen. Abhängige Funktionseinheiten müssen in eine Zuverlässigkeitsstufe höher
ausgeführt sein, als dies bei unabhängigen Funktionseinheiten erforderlich wäre (s. Tabelle
4). Alternativ ist die Prüffrist so zu wählen, dass der Ausfall der Ex-Einrichtung so rechtzeitig
erkannt wird, dass Maßnahmen zur Aufrechterhaltung der Sicherheit getroffen werden können.
Die Anforderungen an eine veränderte Prüffrist ist in der Gefährdungsbeurteilung zu dokumen-
tieren. Anforderungen für erhöhte Anforderungen an Leitsysteme sind in 4.2.3 Absatz 6 be-
schrieben.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 26 -->

TRGS 725 (Fassung 5.6.2023) Seite 26 von 36
Eine Ex-Einrichtung (K1)
Sensor 1 Signalverarbeitung 1 Aktor 1
K2 K1 K1
Abbildung 18: Ex-Einrichtung mit einem abhängigen Sensor.
(3) Für Funktionseinheiten, die im Betriebskonzept auch hinsichtlich des Explosionsschut-
zes verwendet werden, sind keine erhöhten Anforderungen notwendig. Satz 1 gilt nur dann,
wenn der Prozess bei Ausfall der Funktionseinheiten nicht in einen unsicheren Zustand über-
geht. Dies ist z.B. der Fall, wenn ein Ausfall erkannt wird, bevor gefahrbringende, explosions-
schutzrelevante Abweichungen auftreten.
5 Prüfung und Kontrollen der Ex-Einrichtung
Für die Durchführung der Prüfung von Ex- Einrichtungen nach Betriebssicherheitsverord-
nung sind die TRBS 1201 Teil 1 und TRBS 1115 Anhang A zu beachten.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 27 -->

TRGS 725 (Fassung 5.6.2023) Seite 27 von 36
Anhang 1 Erläuterung der Vorgehensweise an Beispielen zur Zo-
nenreduzierung
Die folgenden Beispiele dienen der Erläuterung einer möglichen Bewertung und sind in der
Gefährdungsbeurteilung auf die jeweilige Situation anzupassen.
A1.1 Lüftung
A1.1.1 Fall 1:
(1) Ein Bereich ist mit einer technischen Lüftung versehen, die zu einer Zonenreduzierung
um eine Stufe (von Zone 1 nach Zone 2) verwendet werden soll. Die gesamte Lüftung verfügt
über eine Vielzahl von Abnehmerstellen und Verstellmöglichkeiten, die den Volumenstrom in
dem betroffenen Bereich unbemerkt beeinflussen können. Es wird daher zusätzlich eine Ex-
Einrichtung (Abbildung 19: schraffiert) zur Überwachung des Volumenstroms eingesetzt, die
eine Klassifizierungsstufe erfüllen muss.
Abbildung 19: Erreichen der Zonenreduzierung durch die Ex-Einrichtung.
(2) Vorhandene Explosionsschutzmaßnahme ohne Ex-Einrichtung: Querlüftung, Volumen-
strom richtig dimensioniert, so dass die gewünschte Konzentrationsminderung im Normalbe-
trieb erreicht wird. Der Volumenstrom kann unentdeckt zu klein oder nicht vorhanden sein, so
dass die erforderliche Anforderung an Zielzone (hier: Explosionsgefahr nur selten und kurz-
zeitig) nicht erreicht wird. Die Verfügbarkeit der vorhandenen Explosionsschutzmaßnahme al-
lein wird als nicht ausreichend bewertet.
(3) Konzept: Ex-Einrichtung überwacht den Mindestvolumenstrom und löst im Anforde-
rungsfall die Einleitung von Gegenmaßnahmen aus (technisch oder organisatorisch), so dass
der Ausfall erkannt und der sichere Zustand hergestellt wird.
A1.1.2 Fall 2:
(1) Ein Bereich ist mit einer technischen Lüftung versehen, die zu einer Zonenreduzierung
um eine Stufe (von Zone 1 nach Zone 2) verwendet werden soll. Die Lüftung wirkt ausschließ-
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 28 -->

TRGS 725 (Fassung 5.6.2023) Seite 28 von 36
lich in dem betroffenen Bereich. Der Lüfter ist starr gekoppelt. Ein Ausfall ist nur bei Motorver-
sagen oder zentralem Stromausfall denkbar. Die Lüftung wird als ausreichend verfügbar ein-
gestuft (Abbildung 2020: grau), daher ist keine zusätzliche Ex-Einrichtung erforderlich.
Zone 2
Zone 1
Verfügbarkeit der Explosionsschutzmaßnahme
Abbildung 20: Erreichen der Zonenreduzierung durch Explosionsschutzmaßnahme
(hier: durch technische Lüftung ohne zusätzliche Ex-Einrichtung).
(2) Konzept: Technische Lüftung - Querlüftung, Volumenstrom richtig dimensioniert, so dass
die gewünschte Konzentrationsminderung erreicht wird. Ein Ausfall wird nur selten erwartet
und wird im Rahmen der Betriebsroutine erkannt.
Die Verfügbarkeit der Explosionsschutzmaßnahme wird als ausreichend für die Reduzierung
der Explosionsgefahr um eine Stufe definiert.
A1.2 Inertisierung
A1.2.1 Fall 1:
(1) Ein Lagerbehälter für entzündbare Flüssigkeiten ist an ein Stickstoffnetz angeschlossen
und wird nach erfolgreicher Erstinertisierung über einen (mechanischen) Druckregler mit Stick-
stoff beaufschlagt und mittels eines mechanischen Druckhalteventils im Überdruck gehalten.
Der Lagerbehälter ist mit einer Unterdrucksicherung ausgerüstet. Die Inertisierung im Lager-
behälter wird mittels einer für die Prozessbedingungen geeigneten Druckmessung überwacht.
Es wird eine Druckmessung als Ex-Einrichtung definiert, die bei Versagen der Druckregelung
(Überdruck wird nicht gehalten) alarmiert. Die Ex-Einrichtung (Abbildung 21) muss eine Klas-
sifizierungsstufe erfüllen. Im Lagertank wird durch die Inertisierung eine Zonenreduzierung um
eine Stufe erreicht.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 29 -->

TRGS 725 (Fassung 5.6.2023) Seite 29 von 36
Klassifizierungsstufe der Ex-Einrichtung
Abbildung 21: Durch Ex-Einrichtung abgesicherter Überdruck (eine Klassifizierungs-
stufe).
(2) Vorhandene Explosionsschutzmaßnahme ohne Ex-Einrichtung: Inertisierung: Erst-Iner-
tisierung und richtige Auslegung der Überdruckhaltung erforderlich, trotzdem kann es dazu
kommen, dass störungsbedingt (z.B. bei Ansprechen der Unterdrucksicherung) der Sauer-
stoffgehalt unerkannt steigt, die vorhandene Explosionsschutzmaßnahme reicht nicht zur Er-
reichung der angestrebten Zone.
(3) Konzept: Ex-Einrichtung misst den Überdruck, so dass ein Fehler bei der mechanischen
Überdruckhaltung erkannt wird und das Ansprechen der Unterdrucksicherung (Eintrag von
Luftsauerstoff) durch weitere Maßnahmen verhindert wird.
A1.2.2 Fall 2:
(1) In einem Tank wird durch eine Erst-Inertisierung die Sauerstoffgrenzkonzentration un-
terschritten. Der Tank wird im leichten Überdruck betrieben und ist vakuumfest. Der Tank ist
an ein Abluftsystem angeschlossen, das der Zone 1 zugeordnet ist (sauerstoffarm). Die Druck-
regelung wird als betriebliche MSR-Einrichtung definiert.
Zone 1
Zone 0
Ausreichende Verfügbarkeit (Explosionsschutzmaßnahme Dichtigkeit)
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 30 -->

TRGS 725 (Fassung 5.6.2023) Seite 30 von 36
Abbildung 22: Zonenreduzierung durch Explosionsschutzmaßnahme (hier: Inertisie-
rung ohne zusätzliche Ex-Einrichtung).
(2) Konzept: Inertisierung - Erstinertisierung und verfahrenstechnische Randbedingungen
(Dichtigkeit, Vakuumfestigkeit, Anschluss an Zone 1 (sauerstoffarm)) sind so ausgeführt, dass
ein Sauerstoffeintrag im Störungsfall nicht auftritt. Die Explosionsschutzmaßnahme (Abbildung
2) ist ausreichend, es ist keine zusätzliche Ex-Einrichtung erforderlich
A1.3 Flüssigkeitsverschluss
Durch einen Flüssigkeitsverschluss wird eine Zonenreduzierung erreicht, ein Abhebern des
Flüssigkeitsverschlusses ist ausgeschlossen. Da kontinuierlich Flüssigkeit nachläuft, wird der
Explosionsschutzmaßnahme eine hohe Verfügbarkeit (entspricht 2 Klassifizierungsstufen) in
der Gefährdungsbeurteilung zugewiesen (Abbildung ). Um bei ausgefallenem Zulauf langfristig
ein Austrocknen zu vermeiden, kann durch eine zusätzliche Standmessung (Ex-Einrichtung)
die Verfügbarkeit der Explosionsschutzmaßnahme erhöht werden (Standabnahme wird er-
kannt, Gegenmaßnahmen werden rechtzeitig eingeleitet).
Zone 2
eine Klassifizierungsstufe
der Ex-Einrichtung
Abbildung 23: Erreichen der Explosionssicherheit durch Explosionsschutzmaß-
nahme (Siphon) in Verbindung mit einer Ex-Einrichtung (K1).
A1.4 Taumeltrockner
(1) In einem Taumeltrockner wird ein mit Lösemittel verunreinigtes, nicht brennbares Gra-
nulat, getrocknet. Die Bildung eines explosionsfähigen Gemisches kann nur im Ablaufschritt
Heizen, d.h. bei Temperaturen > 65 °C, erfolgen.
Betriebskonzept: Der Trocknungsvorgang wird mehrmals täglich, automatisiert durch eine
Schrittkette, gestartet. Das Aufheizen erfolgt erst, wenn das Endvakuum erreicht ist (kleiner
50 mbar , Zündgrenzdruck ist unterschritten). Am Ende der Trocknung wird im Rahmen
,absolut
der Schrittkette das Vakuum mit Stickstoff gebrochen.
(2) Die Bildung eines gefährlichen explosionsfähigen Gemisches ist möglich durch
1. Versagen eines Dichtungssystems und Eintrag von Luftsauerstoff während des Trock-
nens oder
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 31 -->

TRGS 725 (Fassung 5.6.2023) Seite 31 von 36
2. Versagen der druckabhängigen Heizungssteuerung.
(3) Bewertung: Da ein Versagen der Schrittkette durch Qualitätssicherungsmaßnahmen
aufgedeckt wird, wird das Innere des Taumeltrockners der Zone 1 zugeordnet.
Abbildung 24: Zonenreduzierung um eine Stufe durch die Ex-Einrichtung (K1).
(4) Konzept: In der Gefährdungsbeurteilung wird festgelegt, dass zur Erreichung der ge-
wünschten Zone 2 eine zusätzliche Ex-Einrichtung installiert werden soll. Dazu soll die Hei-
zung erst freigegeben werden, wenn ein Druck von 50 mbar unterschritten wird. Bei Über-
schreitung des Grenzwertes soll die Heizung ausgeschaltet und Stickstoff zugegeben werden.
Dazu wird die Stickstoffzufuhr und die Verriegelung der Heizung über die Druckmessung als
Ex-Einrichtung definiert, die eine Klassifizierungsstufe beitragen muss (Abbildung 24).
A1.5 Förderung von Feststoff mit Stickstoff
(1) Ein Vorratssilo zur Lagerung eines explosionsfähigen, hoch aufladbaren Pulvers wird
aus einem Silofahrzeug befüllt. Die Entleerung des Fahrzeuges erfolgt mit Hilfe von Stickstoff
im Überdruck.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 32 -->

TRGS 725 (Fassung 5.6.2023) Seite 32 von 36
Zone 20 Zone 22
Betriebskonzept
Abbildung 25: Erreichen der Zonenreduzierung um zwei Stufen durch das Betriebs-
konzept (Förderung mit Stickstoff).
(2) Konzept: Bei Stickstoffausfall kann der Entleervorgang nicht fortgeführt werden. Da
Staubablagerungen nicht ausgeschlossen werden können, wird das Innere der Förderleitung
in die Zone 22 eingeteilt. Elektrostatische Entladungen können nur während des Fördervor-
gangs mit Stickstoff auftreten. Nach Beendigung des Fördervorgangs sind keine zündwirksa-
men Entladungen innerhalb der Rohrleitung zu erwarten. Daher ist keine zusätzliche Ex-Ein-
richtung für das Explosionsschutzkonzept der pneumatischen Förderung erforderlich (Abbil-
dung 25).
(3) Anmerkung: Für das nachgeschaltete Silo zur Lagerung des Feststoffs kann durch die
Art der Befüllung als alleinige Explosionsschutzmaßnahme eine Inertisierung nicht sicherge-
stellt werden, da ohne weitere Explosionsschutzmaßnahmen ein Eintrag von Sauerstoff bei
Entnahme- oder Atmungsvorgängen nicht ausgeschlossen ist. Für das Explosionsschutzkon-
zept des Silos, insbesondere wegen der Möglichkeit einer Schüttkegelentladung, ist daher eine
separate Beurteilung zur Explosionssicherheit erforderlich.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 33 -->

TRGS 725 (Fassung 5.6.2023) Seite 33 von 36
Anhang 2 Maßnahmen zur Erkennung, Vermeidung oder Beherr-
schung des Ausfalls von Ex-Einrichtungen
(1) Falls für die ordnungsgemäße Funktion der Ex-Einrichtung das Vorhandensein oder die
Vorhaltung von Hilfsenergien (z. B. elektrische Energie) oder Hilfsmedien (z. B. Inert-
gase oder Druckluft) erforderlich sind, so ist bei Ausfall derselben die dafür festgelegte
Sicherheitsfunktion auszuführen.
(2) Grundsätzlich sind bei der Realisierung der Ex-Einrichtung bewährte Sicherheitsprinzi-
pien anzuwenden, wie:
1. Verwendung bewährter und zuverlässiger Installationstechnik,
2. geeignete Auswahl, Kombination, Anordnungen, Zusammenbau und Einbau der Bau-
teile durch Berücksichtigung der Anwendungshinweise der Hersteller sowie von Erfah-
rungen mit ähnlichen Bauteilen,
3. übersichtlicher und einfacher Aufbau der Ex-Einrichtung, geringere Anzahl von Bautei-
len,
4. Begrenzung von Fehlerauswirkungen durch z. B.
a) hochohmige Entkopplung oder
b) Kurzschlussfestigkeit oder
c) galvanische Trennung,
5. Anwendung des Ruhestrom- bzw. Ruhesignalprinzips für Signalleitungen,
6. Grenzwertveränderungen oder Änderungen an der Logik erfolgen nur durch autori-
sierte Personen,
7. Toleranz der Ex-Einrichtung gegen Abweichungen der Hilfsenergieversorgung (z. B.
Steuerluft, elektrische Versorgung usw.); Abweichungen über die für die Versorgung
der Geräte zulässigen Grenzwerte hinaus, dürfen keinen Fehler in der Ex-Einrichtung
zur Folge haben z.B. durch
a) entsprechende Eigenschaften der Geräte selbst oder
b) Sicherstellung der Hilfsenergieversorgung durch z. B. Redundanzen oder
c) automatische Überwachung der Hilfsenergieversorgung mit Melden und Auslö-
sen der Schutzfunktion,
8. Vermeidung von Fehlern gemeinsamer Ursache in redundanten Ex-Einrichtungen,
(3) Ex-Einrichtungen dürfen nach Auslösung nicht automatisch zurückgesetzt werden, es
sei denn in der Gefährdungsbeurteilung ist etwas Anderes festgelegt.
(4) Sofern manuelle Absperreinrichtungen an Prozessanschlüssen von Ex-Einrichtungen
vorhanden sind, muss deren Fehlstellung erkannt werden und zu Maßnahmen führen oder der
Stellungszustand muss leicht erkennbar und gegen unbeabsichtigtes Schließen (z. B. durch
Sperrhülsen, Kette und Schloss oder durch Entfernen von Handrädern) gesichert sein.
(5) Ex-Einrichtungen müssen grundsätzlich unabhängig von betrieblichen Mess-, Steuer-
und Regeleinrichtungen sein, wenn diese als Teil des Betriebskonzeptes zur Festlegung von
Anforderungen an diese Ex-Einrichtung verwendet werden. Dies betrifft in der Regel einzelne
Funktionseinheiten, im Einzelfall auch ganze Ex-Einrichtungen.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 34 -->

TRGS 725 (Fassung 5.6.2023) Seite 34 von 36
(6) Das Signal zur Auslösung der Sicherheitsfunktion muss stets Vorrang vor den Signalen
der Betriebseinrichtung haben.
(7) Steuerungen und Prozessleitsysteme (PLS) können als komplexe Systeme für die Klas-
sifizierungsstufe K1 eingesetzt werden, wenn für diese die folgenden Bedingungen erfüllt sind:
1. Es dürfen nur Steuerungen oder PLS von Herstellern eingesetzt werden, die ein geeig-
netes Qualitätssicherungssystem betreiben (z.B. inkl. Änderungsmanagement des Her-
stellers für Hard- und Systemsoftware).
2. Die Systeme haben sich in Standardanwendungen des Arbeitgebers oder vergleichba-
ren Anwendungen bewährt und entsprechen dem Stand der Technik.
3. Das System hat eine dokumentierte Spezifikation, in der die grundlegenden System-
komponenten und Bibliotheken beschrieben sind.
4. Für die Erstellung oder Änderung der Anwendersoftware ist geeignet qualifiziertes Per-
sonal einzusetzen. Zur Ausführung der Ex-Einrichtung im PLS sind die Anforderungen
nach Abschnitt 4.2.2 zu berücksichtigen.
5. Ex-Einrichtungen sind grundsätzlich mit separaten Softwaremodulen übersichtlich zu
programmieren. Deren Funktionen müssen gegenüber Betriebseinrichtungen stets Vor-
rang haben und sind als solche in der Funktionsspezifikation festzulegen.
6. Funktional zusammenhängende Ex-Einrichtungen sollen nicht auf gleichen Eingangs-
und Ausgangskarten liegen. Vorhandene Diagnose-Eigenschaften, z.B. bei Feldgerä-
ten, sind grundsätzlich zu verwenden.
7. Funktionseinheiten der Ex-Einrichtung im Leitsystem müssen grundsätzlich unabhän-
gig von betrieblichen Mess-, Steuer- und Regeleinrichtungen sein, wenn diese als Teil
des Betriebskonzeptes zur Festlegung von Anforderungen an die Ex-Einrichtung ver-
wendet werden.
8. Die Anwendersoftware ist vom Betreiber mit ihrem Stand zu dokumentieren, soweit die
Änderung für die Ex-Einrichtung relevant ist.
9. Der Arbeitgeber verfügt über ein Änderungsmanagement für alle Änderungen in der
Hard- und Software mit Freigabe zur Änderung sowie genehmigter Spezifikation und
anschließender dokumentierter Prüfung, soweit sie die Ex-Einrichtungen betreffen.
10. Das für Änderungen und Instandhaltungen eingesetzte Personal hat eine geeignete
Qualifikation. Dieses beinhaltet technisches Wissen, Ausbildung und Erfahrung bezo-
gen auf
a) die verfahrenstechnische Anwendung,
b) die eingesetzte PLS-Technologie,
c) Sensoren und Aktoren.
(8) Für eine nicht redundante Funktionseinheit mit der Klassifizierungsstufe K2 gilt, dass ein
unentdeckter Fehler, der die Sicherheitsfunktion (des betreffenden Kanals) bei Aktivierung der
Funktion blockiert, innerhalb einer Zeitspanne erkannt und beseitigt werden muss (z.B. durch
Kontroll- oder Prüfzyklen), in der vernünftigerweise nicht mit einem weiteren Fehler gerechnet
werden muss, der in Kombination mit dem passiven Fehler zu einem unsicheren Zustand führt.
Grundsätzlich ist die Fehlerdiagnostik der Geräte zu aktivieren und auszuwerten.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 35 -->

TRGS 725 (Fassung 5.6.2023) Seite 35 von 36
(9) Bei softwaregesteuerten Geräten (z. B. Frequenzumrichter oder Stellungsregler) müs-
sen sicherheitstechnische Schalthandlungen grundsätzlich ohne deren Softwaresteuerung di-
rekt auf das entsprechende Stellglied einwirken, es sei denn, es liegt der Nachweis der erfor-
derlichen funktionalen Sicherheit vor.
Anhang 3 Anforderungen an die Betriebsbewährung der Funktions-
einheiten von Ex-Einrichtungen
(1) Wenn der Nachweis der Betriebsbewährung für Geräte mit Prozessanschluss (Senso-
ren, Aktoren) geführt werden soll, wird vorausgesetzt, dass für das eingesetzte Gerät Erfah-
rungen im Betrieb vorliegen. Mögliche systematische Fehler haben bei solchen Geräten keine
sicherheitsrelevanten Auswirkungen gezeigt und zufällige Fehler sind hinreichend selten, so
dass die nach Abschnitt 2.15 festgelegten Verfügbarkeiten erreicht werden können. Die Be-
triebsbewährung hängt von den Einsatzbedingungen (z. B. Prozessgrößen und Stoffeigen-
schaften) ab, denen die Geräte ausgesetzt sind. Der Nachweis der Betriebsbewährung kann
dabei allgemein für mehrere Applikationen oder als Einzelfallbetrachtung für einzelne Applika-
tionen geführt werden und ist in der Gefährdungsbeurteilung zu dokumentieren.
(2) Für die Beurteilung der Betriebsbewährung im Sinne dieser TRGS sind für die verwen-
deten Geräte nachfolgend beispielhaft aufgelistete Informationen erforderlich:
1. Nachweis über eine ausreichende Betriebserprobung
a) 10.000h in den gleichen speziellen Anwendungen oder
b) 100.000h in verschiedenen Applikationen für eine allgemeine Bewertung,
2. Bewertung der (sicherheitstechnischen Eigenschaften) der Geräte
a) Sensor: kann das Gerät eigene Fehler erkennen?
b) Aktor: bringt der Aktor das Gerät bei Energieverlust in den sicheren Zustand?
3. Bewertung der systematischen Eignung der Geräte
a) Ist das Gerät für die Prozessbedingungen geeignet?
b) Kann das Gerät den Alarm / Trippunkt hinreichend genau erkennen?
4. Abschätzung möglicher Fehlerraten aufgrund von Felderfahrungen durch Aus-
wertung der Ergebnisse aus Nummer 1,
5. Störstatistiken während der Verwendung, inklusive Fehleranalyse
Über die eigentliche erste Bewertung hinaus, muss bei den Geräten stetig darauf geachtet
werden, dass die angenommenen Fehlerraten noch gültig sind.
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags


<!-- Seite 36 -->

TRGS 725 (Fassung 5.6.2023) Seite 36 von 36
Literaturhinweise
In den folgenden Regelwerken und Normen sind applikations- und technologiespezifische
Vorgehensweisen und Methoden beschrieben und werden Anforderungen an die Zuverläs-
sigkeit von sicherheitsrelevanten MSR-Einrichtungen definiert:
[1] Technische Regeln wie TRBS 1115 „Sicherheitsrelevante Mess-, Steuer- und Regelein-
richtungen“
[2] die Normen der Reihe DIN EN ISO 13849 „Sicherheit von Maschinen – Sicherheitsbezo-
gene Teile von Steuerungen“
[3] DIN EN 62061 „Sicherheit von Maschinen – Funktionale Sicherheit sicherheitsbezogener
elektrischer, elektronischer und programmierbarer elektronischer Steuerungssysteme“
[4] die Normen der Reihe DIN EN 61508 „Funktionale Sicherheit sicherheitsbezogener
elektrischer/elektronischer/programmierbarer elektronischer Systeme“
[5] die Normen der Reihe DIN EN 61511 „Funktionale Sicherheit – Sicherheitstechnische
Systeme für die Prozessindustrie“
[6] die Norm DIN EN ISO 80079-37 „Explosionsfähige Atmosphären - Teil 37: Nichtelektri-
sche Geräte für den Einsatz in explosionsfähigen Atmosphären - Schutz durch konstruktive
Sicherheit "c", Zündquellenüberwachung "b", Flüssigkeitskapselung "k"“
[7] NAMUR Empfehlung NE 130: "Betriebsbewährte Geräte für PLT-Schutzeinrichtungen und
vereinfachte SIL-Berechnung"
Ausschuss für Gefahrstoffe – AGS-Geschäftsführung – www.baua.de/ags