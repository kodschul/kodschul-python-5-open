# Lab 9.3 – Übung: Geheimzahl schützen

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `Game` hält die Geheimzahl privat, `attempts_left` und `is_won` werden nur lesbare Properties; die Ausgabe des Spiels bleibt gleich. Lab 10.1 baut die Spieler-Klassen darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `ui.py`)
**Starter:** `starters/m09-l03-guess_game/` mit `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 9.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m09-oop-basics/l02-classes/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m09-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Die Stellen zum Ändern sind im Starter mit `# TODO Lab 9.3` markiert.

## Aufgaben

1. Benenne in `Game.__init__` das Attribut `max_tries` in `_max_tries` und `secret` in `__secret` um. Passe in `guess()` jede Stelle an, die die Geheimzahl liest.
2. Lösche in `__init__` die Attribute `attempts_left` und `won` und in `guess()` die Zeilen, die sie ändern. Schreibe stattdessen zwei Properties mit `@property`: `attempts_left` (Versuche minus Anzahl der Tipps) und `is_won` (`True`, wenn die Geheimzahl unter den Tipps ist). Ersetze in `guess()`, `is_over()` und `result()` jedes `self.won` durch `self.is_won`.
3. Schreibe die Methode `reveal_secret(self)`: Sie gibt die Geheimzahl zurück, wenn das Spiel vorbei ist, sonst `None`.
4. Ersetze in `ui.play_round` den Zugriff `game.won` durch `game.is_won` und `game.secret` durch `game.reveal_secret()`.
5. Spiele eine gewonnene und eine verlorene Runde. Starte danach im Ordner `playground/` die Python-Konsole mit `python`, erzeuge `game = logic.Game("Anna")` (nach `from guess_game import logic`) und probiere `game.attempts_left`, `game.reveal_secret()`, `game.attempts_left = 99` und `game.__secret`.

## Checkpoint

- Das Spiel läuft wie vorher; nach einer verlorenen Runde nennt es die Geheimzahl.
- `game.attempts_left` zeigt bei einem neuen Spiel auf Stufe leicht `5`, `game.reveal_secret()` zeigt `None`.
- `game.attempts_left = 99` endet mit `AttributeError: property 'attempts_left' of 'Game' object has no setter`.
- `game.__secret` endet mit `AttributeError: 'Game' object has no attribute '__secret'`.

## Abschlusskriterien

- In `logic.py` steht die Geheimzahl nur noch als `self.__secret`; `attempts_left` und `is_won` sind Properties ohne Setter.
- `ui.py` greift weder auf `secret` noch auf `won` zu.

## Erweiterung

Kopiere `code/m09-oop-basics/classes.py` nach `playground/student.py` und kapsle die Noten: Die Liste heißt `__grades`, `add_grade` löst `ValueError` aus, wenn die Note nicht zwischen 1.0 und 5.0 liegt, und `average` wird eine nur lesbare Property. Teste `anna.add_grade(6.0)` in einem `try`-Block und gib `anna.average` ohne Klammern aus. Start im Ordner `playground/` mit `python student.py`.
