# Lab 4.1 – Übung: Listen

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel merkt sich alle Tipps einer Runde; Lab 4.2 baut darauf auf.

**Arbeitsdatei:** `playground/guess_game.py`
**Starter:** `starters/m04-l01-guess_game.py`

## Vorbereitung

- VS Code ist im Ordner `project/` geöffnet, das Terminal zeigt die aktive `.venv`.
- Das eigene Spiel aus Lab 3.4 liegt in `playground/guess_game.py`. Ohne eigenen Stand: Inhalt von `starters/m04-l01-guess_game.py` komplett nach `playground/guess_game.py` kopieren.
- Die Stellen zum Ändern sind im Starter mit `# TODO Lab 4.1` markiert.

## Aufgaben

1. Lege zu Beginn jeder Runde, direkt unter `tries = 0`, eine leere Liste `guesses` an.
2. Hänge nach `tries += 1` den aktuellen Tipp mit `append` an die Liste an.
3. Gib nach der inneren Schleife, vor der Frage „Nochmal spielen?“, die Liste mit dem Text `Bisherige Tipps:` aus.
4. Starte das Spiel mit `python playground/guess_game.py` und spiele eine Runde mit drei Tipps, z. B. 5, 8, 7.
5. Spiele mit `j` eine zweite Runde und prüfe, dass die Liste wieder nur die Tipps dieser Runde enthält.

## Checkpoint

- Nach jeder Runde erscheint eine Zeile wie `Bisherige Tipps: [5, 8, 7]`.
- Bei einem Treffer im ersten Versuch zeigt die Liste genau ein Element.
- Die zweite Runde beginnt mit einer leeren Liste.

## Abschlusskriterien

- `playground/guess_game.py` läuft ohne Fehlermeldung und gibt nach jeder Runde die Tipps der Runde in Eingabereihenfolge aus.

## Erweiterung

Schreibe in `playground/grades.py` ein kleines Skript wie `code/m04-collections/average_grades.py`: eine Liste mit fünf eigenen Noten, Ausgabe von Anzahl, Durchschnitt (auf zwei Stellen gerundet), bester und schlechtester Note und der sortierten Liste.
