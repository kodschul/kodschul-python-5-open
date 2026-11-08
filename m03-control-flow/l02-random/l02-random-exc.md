# Lab 3.2 – Übung: Geheimzahl per Zufall

**Dauer:** ca. 8 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — jedes Spiel hat eine neue Geheimzahl von 1 bis 10; Lab 3.3 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m03-l02-guess_game.py`

## Vorbereitung

- Terminal im Ordner `project/`, `.venv` aktiv.
- Das eigene Spiel aus Lab 3.1 liegt in `playground/guess_game.py`. Ohne eigenen Stand: Inhalt von `starters/m03-l02-guess_game.py` nach `playground/guess_game.py` kopieren.

## Aufgaben

1. Schreibe `import random` in die erste Zeile unter dem Kopfkommentar von `playground/guess_game.py`.
2. Ersetze `secret = 7` durch eine Zufallszahl von 1 bis 10 mit `random.randint`.
3. Ergänze direkt darunter vorübergehend eine Kontrollausgabe `print("Geheimzahl:", secret)` und starte das Spiel dreimal. Notiere die drei Geheimzahlen.
4. Ergänze unter `import random` die Zeile `random.seed(1)`, starte das Spiel zweimal und vergleiche die Geheimzahlen.
5. Entferne `random.seed(1)` und die Kontrollausgabe wieder und starte das Spiel ein letztes Mal.

## Checkpoint

- Ohne Seed zeigen die drei Starts in Aufgabe 3 meist unterschiedliche Geheimzahlen.
- Mit `random.seed(1)` zeigen beide Starts dieselbe Geheimzahl.
- Am Ende verrät das Spiel die Geheimzahl nicht mehr.

## Abschlusskriterien

- `playground/guess_game.py` beginnt mit `import random` und zieht die Geheimzahl mit `random.randint(1, 10)`.
- Weder `random.seed(...)` noch eine Ausgabe der Geheimzahl steht noch im Code.

## Erweiterung

Erweitere den Würfel aus der Theorie auf drei Würfe in `playground/three_dice.py`: Ausgabe `Würfe: a, b, c` und die Summe; bei drei gleichen Augenzahlen zusätzlich `Dreierpasch!`, bei genau zwei gleichen `Pasch!`.
