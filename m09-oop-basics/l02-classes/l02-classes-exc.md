# Lab 9.2 – Übung: Eine Runde als Game-Objekt

**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `logic.py` bekommt die Klasse `Game`, `ui.play_round(game)` spielt mit einem Objekt; die Ausgabe des Spiels bleibt gleich. Lab 9.3 schützt die Geheimzahl.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `logic.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m09-l02-guess_game/` mit `__main__.py`, `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, einmal `cd playground` (Start dann mit `python -m guess_game`).
- Das eigene Spiel aus Lab 8.3 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m08-files/l03-csv/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m09-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- Die Stellen zum Ändern sind im Starter mit `# TODO Lab 9.2` markiert.

## Aufgaben

1. Verschiebe in `logic.py` die Importe `import time` und `from datetime import datetime` aus `ui.py` nach oben in `logic.py`. Lösche `is_guess_correct` und `is_game_over`. Schreibe unten die Klasse `Game` mit `__init__(self, name, level="leicht")`. Sie legt diese Attribute an: `name`, `level`, `low`, `high` und `max_tries` (aus `LEVELS[level]` entpacken), `secret` (mit `draw_secret`), `attempts_left` (Start: `max_tries`), `guesses` (leere Liste), `won` (`False`), `started` (`datetime.now()`), `start_time` (`time.perf_counter()`), `seconds` (`0.0`).
2. Schreibe die Methode `is_over(self)`: `True`, wenn gewonnen oder keine Versuche mehr übrig sind. Schreibe `result(self)`: gibt dasselbe Dictionary zurück wie bisher `play_round` (Schlüssel `name`, `level`, `tries`, `seconds`, `won`, `date`); `tries` ist die Länge von `self.guesses`.
3. Schreibe die Methode `guess(self, number)`, die einen Hinweistext zurückgibt: zuerst `check_guess(number, self.low, self.high)` aufrufen; steht `number` schon in `self.guesses`, `"schon getippt"` zurückgeben. Sonst Tipp anhängen, einen Versuch abziehen, bei Treffer `self.won = True` setzen. Ist das Spiel danach vorbei, `self.seconds` aus der Stoppuhr berechnen (`round(..., 1)`). Zum Schluss `"richtig"`, `"zu hoch"` oder `"zu niedrig"` zurückgeben.
4. Ändere in `ui.py` die Funktion `show_hint(hint)` so, dass sie am Text `"zu hoch"` entscheidet. Schreibe `play_round(game)` um: Kopfzeilen aus `game.level`, `game.name`, `game.low`, `game.high`, `game.started`; Schleife `while not game.is_over():` mit `hint = game.guess(guess)` im `try`-Block; bei `"schon getippt"` die bekannte Meldung, sonst (außer bei `"richtig"`) `show_hint(hint)` und, falls nicht vorbei, `Verbleibende Versuche: …`. Nach der Schleife Gewinnzeile oder `Keine Versuche mehr. Die Zahl war …`, dann `Bisherige Tipps`, `return game.result()`.
5. Ändere in `__main__.py` den Import zu `from guess_game import logic, storage, ui` und erzeuge pro Runde `game = logic.Game(name, level)`, dann `result = ui.play_round(game)`. Spiele eine gewonnene und eine verlorene Runde, gib dabei einmal `500`, einmal `abc` und einmal einen doppelten Tipp ein.

## Checkpoint

- Das Spiel läuft wie vorher: gleiche Meldungen, Bestenliste, `history.csv`.
- Im Ordner `playground/` liefert `python` und dann:

  ```text
  >>> from guess_game import logic
  >>> game = logic.Game("Anna")
  >>> game.guess(5)
  ```

  einen Hinweis wie `'zu niedrig'`; danach zeigt `game.attempts_left` den Wert `4`. `exit()` beendet die Python-Konsole.

## Abschlusskriterien

- `logic.py` enthält die Klasse `Game` mit `__init__`, `guess`, `is_over` und `result`; `is_guess_correct` und `is_game_over` gibt es nicht mehr.
- `ui.play_round` bekommt ein `Game`-Objekt und enthält keine eigenen Variablen für Geheimzahl oder Versuche.

## Erweiterung

Lege `playground/piggy_bank.py` an: eine Klasse `PiggyBank` (Sparschwein) mit den Attributen `owner` und `coins` (Liste der eingeworfenen Beträge), der Methode `insert(amount)` und der Methode `total()`, die die Summe zurückgibt. Erzeuge zwei Sparschweine, wirf verschiedene Beträge ein und gib `Sparschwein von Anna: 3.5 €` aus. Start im Ordner `playground/` mit `python piggy_bank.py`.
