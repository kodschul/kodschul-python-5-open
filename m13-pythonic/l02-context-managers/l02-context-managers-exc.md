# Lab 13.2 – Übung: Bestenliste als Context Manager

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `Scoreboard` lädt in `__enter__` und speichert in `__exit__`; `__main__.py` nutzt `with storage.Scoreboard("highscores.json") as board:`. Lab 13.3 baut darauf auf.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `storage.py`, `__main__.py`)
**Starter:** `starters/m13-l02-guess_game/` mit `__main__.py`, `storage.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 13.1 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m13-pythonic/l01-decorators/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m13-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Eine alte `playground/highscores.json` löschen, damit der Test bei einer leeren Bestenliste beginnt.

## Aufgaben

1. Ändere in `storage.py` den Konstruktor von `Scoreboard`: `self.path = Path(path)` und `self.scores = []`; er lädt die Datei nicht mehr.
2. Schreibe die Methode `__enter__(self)`: Sie lädt die Scores mit `self.load()` in `self.scores` und gibt `self` zurück.
3. Schreibe die Methode `__exit__(self, exc_type, exc_value, traceback)`: Sie speichert mit `self.save()` und gibt `False` zurück. Entferne den Aufruf `self.save()` aus `add()`.
4. Ersetze in `__main__.py` die Zeile `scoreboard = storage.Scoreboard()` durch `with storage.Scoreboard("highscores.json") as board:`. Rücke die `for`-Schleife und `ui.show_statistics(...)` in diesen Block ein und ersetze dort `scoreboard` durch `board`.
5. Starte `python -m guess_game`, gewinne eine Runde und drücke bei der Frage `Bestenliste nach (versuche/zeit/punkte):` die Tasten Strg+C. Öffne danach `playground/highscores.json` in VS Code.

## Checkpoint

- Ohne Strg+C läuft das Spiel wie in Lab 13.1.
- Nach Strg+C erscheint `Spiel abgebrochen. Bis zum nächsten Mal!` ohne Traceback.
- `highscores.json` enthält den Gewinn der abgebrochenen Sitzung, obwohl `add()` nicht mehr speichert.

## Abschlusskriterien

- `Scoreboard` hat `__enter__` und `__exit__`; `add()` enthält kein `save()`.
- In `__main__.py` steht der ganze Rundenablauf im `with`-Block.

## Erweiterung

Lege `playground/section.py` an und schreibe mit `@contextmanager` einen Context Manager `section(title)`: Beim Betreten gibt er `=== Einkauf ===` aus, beim Verlassen `--- Ende Einkauf ---`, auch wenn im Block ein Fehler passiert. Teste ihn einmal mit zwei `print`-Zeilen im Block und einmal mit `print("Summe:", 10 / 0)` in einem `try`/`except ZeroDivisionError`.
