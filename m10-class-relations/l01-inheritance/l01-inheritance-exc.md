# Lab 10.1 – Übung: Vererbung

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — neue Datei `players.py` mit `Player` und `HumanPlayer`, eigener Spielfehler `InvalidGuessError`. Lab 10.2 ergänzt den Computer-Spieler.
**Arbeitsdatei:** `playground/guess_game/` (neu: `players.py`; geändert: `logic.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m10-l01-guess_game/` mit `__main__.py`, `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 9.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m09-oop-basics/l03-encapsulation/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m10-l01-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Die Stellen für die Änderungen sind im Starter mit `# TODO Lab 10.1` markiert.

## Aufgaben

1. Lege in `logic.py` über `check_guess` die Klasse `InvalidGuessError` an, die von `ValueError` erbt; ein Docstring genügt als Körper. Lass `check_guess` diese Klasse statt `ValueError` auslösen (Meldung unverändert).
2. Lege die Datei `guess_game/players.py` an: `from guess_game import ui` und die Klasse `Player` mit `__init__(self, name)` (speichert `self.name`) und `next_guess(self)`, die `NotImplementedError("Diese Methode muss eine Unterklasse festlegen.")` auslöst.
3. Schreibe darunter `HumanPlayer(Player)`: kein eigenes `__init__`, nur `next_guess` überschreiben, sodass es `ui.ask_number("Tipp: ")` zurückgibt.
4. Ändere in `ui.py` die Funktion zu `play_round(game, player)`: Der Tipp kommt aus `player.next_guess()`, der `except`-Block fängt `logic.InvalidGuessError`.
5. Importiere in `__main__.py` zusätzlich `players`, erzeuge nach der Namensabfrage `player = players.HumanPlayer(name)` und übergib `player.name` an `logic.Game` und `player` an `ui.play_round`. Starte das Spiel mit `python -m guess_game` und tippe einmal `500` und einmal `abc`.

## Checkpoint

- Das Spiel läuft wie vorher: `500` → „Der Tipp muss zwischen 1 und 10 liegen.“, `abc` → „Bitte eine ganze Zahl eingeben, z. B. 7.“, kein Versuch wird verbraucht.
- Im REPL (`python` im Ordner `playground/`, dann `from guess_game import logic, players`):
  - `isinstance(players.HumanPlayer("Anna"), players.Player)` → `True`
  - `issubclass(logic.InvalidGuessError, ValueError)` → `True`
  - `players.Player("Test").next_guess()` → `NotImplementedError: Diese Methode muss eine Unterklasse festlegen.`

## Abschlusskriterien

- `players.py` enthält `Player` und `HumanPlayer(Player)`; `HumanPlayer` überschreibt nur `next_guess`.
- `ui.py` ruft nirgends mehr direkt `ask_number("Tipp: ")` in `play_round` auf und fängt `logic.InvalidGuessError`.

## Erweiterung

Kopiere `code/m10-class-relations/shape.py` nach `playground/shapes.py` und ergänze eine Klasse `Square(Rectangle)`: Ein Quadrat ist ein Rechteck mit gleicher Breite und Höhe, bekommt also nur `side` und heißt „Quadrat“. Gib `Square(4).describe()` aus und prüfe mit `isinstance`, ob ein Quadrat ein `Shape` ist. Start im Ordner `playground/` mit `python shapes.py`.
