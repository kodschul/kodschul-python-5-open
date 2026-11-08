# Lab 11.2 – Übung: Score als Dataclass

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `Score` wird zur Dataclass, `storage.py` speichert per `asdict`; Ausgabe und `highscores.json` bleiben gleich. Lab 11.3 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `storage.py`)
**Starter:** `starters/m11-l02-guess_game/` mit `logic.py`, `storage.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 11.1 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m11-advanced-oop/l01-magic-methods/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m11-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen. Die Stellen zum Ändern tragen `# TODO Lab 11.2`.
- `playground/highscores.json` mit mindestens einem Eintrag liegt vor (sonst erst eine Runde gewinnen).

## Aufgaben

1. Ergänze oben in `logic.py` `from dataclasses import dataclass` und setze `@dataclass` direkt über `class Score:`.
2. Ersetze `__init__` von `Score` durch sechs Felder mit Type Hint, in derselben Reihenfolge wie die bisherigen Parameter: `name`, `level`, `date` als Text, `tries` als ganze Zahl, `seconds` als Kommazahl, `won` als Wahrheitswert. `__str__` und `__lt__` bleiben.
3. Lösche `to_dict()`. Ergänze in `storage.py` `from dataclasses import asdict` und nutze in `save()` `asdict(score)` statt `score.to_dict()`.
4. Prüfe im REPL (`python` im Ordner `playground/`): `from guess_game import logic, storage`, dann `score = storage.Scoreboard().scores[0]` und nacheinander `print(score)`, `score` (ohne `print`) und `score == logic.Score(...)` mit denselben sechs Werten.
5. Starte `python -m guess_game`, gewinne eine Runde und öffne `playground/highscores.json`.

## Checkpoint

- `print(score)` zeigt `Anna – 3 Versuche – 0,0 s`, die Eingabe `score` im REPL zeigt `Score(name='Anna', level='leicht', …)`.
- Der Vergleich mit einem neuen `Score` mit gleichen Werten ergibt `True`.
- Bestenliste und `highscores.json` sehen aus wie nach Lab 11.1.

## Abschlusskriterien

- `Score` hat `@dataclass`, sechs Felder mit Type Hint, `__str__` und `__lt__`, aber kein `__init__` und kein `to_dict`.
- `storage.py` importiert `asdict` und nutzt es in `save()`.

## Erweiterung

Lege `playground/books.py` an: eine Dataclass `Book` mit `order=True` und den Feldern `title`, `author`, `year`. Sortiere drei Bücher mit `sorted` und gib sie aus. Stelle danach das Feld `year` an den Anfang der Klasse (die Erzeugung entsprechend anpassen) und vergleiche die neue Reihenfolge.
