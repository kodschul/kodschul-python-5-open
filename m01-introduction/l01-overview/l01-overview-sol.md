# Lab 1.1 – Lösung: Was ich mit Python automatisieren will

Die Lösung zeigt eine ausgefüllte Beispieltabelle. Eigene Tabellen sehen anders aus; entscheidend ist, dass jede Zeile eine konkrete, regelmäßige Aufgabe mit Eingabe, Verarbeitung und Ausgabe beschreibt.

## Aufgabe 1: Drei wiederkehrende Aufgaben

- Fotos und Scans nach dem Herunterladen umbenennen
- Punkte aus Übungsblättern zu einer Gesamtnote zusammenrechnen
- Wohnungsangebote von mehreren Webseiten vergleichen

## Aufgabe 2 bis 4: Ausgefüllte Tabelle

| Aufgabe | Wie oft? | Einsatzgebiet | Was Python übernehmen würde |
| --- | --- | --- | --- |
| Fotos und Scans umbenennen | wöchentlich, ca. 30 Dateien | Automatisierung | liest alle Dateien eines Ordners, benennt sie nach Datum um (`2026-11-08_scan_01.pdf`), meldet die Anzahl |
| Punkte zu einer Gesamtnote zusammenrechnen | nach jedem Übungsblatt | Datenanalyse | liest die Punkte aus einer CSV-Tabelle, berechnet Summe und Durchschnitt, gibt die voraussichtliche Note aus |
| Wohnungsangebote vergleichen | täglich in der Suchphase | Web | ruft Angebote ab, filtert nach Preis und Lage, schreibt die passenden in eine Liste |

Grund für die Zuordnung: Das Einsatzgebiet richtet sich danach, was das Skript hauptsächlich tut. Dateien bewegen ist Automatisierung, mit Zahlen rechnen ist Datenanalyse, Daten aus dem Netz holen ist Web.

Weitere passende Beispiele:

| Aufgabe | Einsatzgebiet | Was Python übernehmen würde |
| --- | --- | --- |
| Downloads-Ordner aufräumen | Automatisierung | sortiert Dateien nach Endung in Unterordner (`pdf/`, `bilder/`) |
| Abschlussarbeit sichern | Administration und DevOps | kopiert den Projektordner täglich mit Datum in einen Sicherungsordner |
| Umfrageergebnisse auswerten | Datenanalyse | liest eine Excel-Datei, zählt Antworten, zeichnet ein Balkendiagramm |
| Texte nach Stichworten durchsuchen | Automatisierung | durchsucht alle `.txt`-Dateien nach einem Begriff und listet die Fundstellen |

## Aufgabe 5: Größte Zeitersparnis

Markiert: **Fotos und Scans umbenennen.** 30 Dateien pro Woche von Hand umzubenennen dauert etwa 10 Minuten; ein Skript erledigt es in unter einer Sekunde und macht keine Tippfehler. Dateien und Ordner bearbeiten ist Thema in Modul 14.

## Erweiterung

| Aufgabe | Grenze |
| --- | --- |
| Fotos und Scans umbenennen | Das Skript kann den Inhalt eines Scans nicht verstehen, solange der Dateiname keinen Hinweis enthält; ein sinnvoller Titel braucht weiterhin einen Menschen. |
