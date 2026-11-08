# Lab 11.4 – Übung: Review des Spiels

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — das Review liest nur; Ergebnis sind ein Klassendiagramm und zwei Verbesserungsvorschläge.
**Arbeitsdatei:** Papier oder neue Datei `playground/review.md`
**Review-Objekt:** eigener Stand `playground/guess_game/` oder das Beispiel `examples/m11-advanced-oop/l03-abstraction/guess_game/`
**Checkliste:** [l04-review-checklist.md](l04-review-checklist.md)

## Vorbereitung

- Den Ordner des Review-Objekts im VS Code Explorer aufklappen.
- Die Checkliste daneben öffnen (Rechtsklick auf den Tab → **Split Right**) oder ausdrucken.

## Aufgaben

1. Lies den Kopfkommentar und die Klassen-Docstrings jeder Datei und notiere je Datei ihre Aufgabe in einem Satz (Checkliste Punkt 1–2).
2. Zeichne das Klassendiagramm: alle Klassen mit Attributen und Methoden, dazu Vererbung (leeres Dreieck), Komposition (gefüllte Raute) und „erzeugt“ (gestrichelter Pfeil). Markiere die abstrakte Klasse mit `<<abstract>>`.
3. Prüfe mit **Edit → Find in Files** die Punkte 3–7: Suche `input(`, `print(`, `open(` und `import` im Review-Objekt und bewerte jeden Treffer.
4. Gehe die Punkte 8–14 durch und trage in jede Zeile `ok` oder eine Notiz ein.
5. Formuliere zwei Verbesserungsvorschläge als Zeilen `Datei | Stelle | Beobachtung | Vorschlag` und beantworte: Welche Klasse ändert sich beim Wechsel von JSON zu einer Datenbank?

## Checkpoint

- Das Diagramm enthält sieben Klassen: drei Spieler-Klassen, `Game`, `Scoreboard`, `Score`, `InvalidGuessError` (mit `ValueError` als Basisklasse).
- Jeder Treffer der Suche nach `print(` ist einer Datei und einer Bewertung zugeordnet.
- Zwei Vorschläge mit Datei und Stelle liegen vor.

## Abschlusskriterien

- Klassendiagramm und zwei Verbesserungsvorschläge auf Papier oder in `playground/review.md`.
- Die Antwort auf die Datenbank-Frage nennt eine Klasse und eine Datei.

## Erweiterung

Tausche das Ergebnis mit einer zweiten Person, die das Review am eigenen Spiel gemacht hat: Jede prüft das Diagramm der anderen gegen deren Code und markiert fehlende Beziehungen. Ohne Partner: Belege jede Linie des eigenen Diagramms mit der Code-Zeile, die sie erzeugt (z. B. `class HumanPlayer(Player):` für die Vererbung, `self.scoreboard = scoreboard` für die Komposition), und ergänze Linien, für die eine Code-Zeile ohne Linie übrig bleibt.
