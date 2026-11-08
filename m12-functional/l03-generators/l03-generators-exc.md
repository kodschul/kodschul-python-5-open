# Lab 12.3 – Übung: Runden aus einem Generator

**Dauer:** ca. 18 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — ein Generator `rounds()` liefert die Runden, die Hauptschleife lautet `for game in ui.rounds(...)`; das ist Spiel v3, der Endstand von Tag 3.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `ui.py`, `__main__.py`)
**Starter:** `starters/m12-l03-guess_game/` mit `__main__.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 12.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m12-functional/l02-lambda/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m12-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Schreibe in `ui.py` an der Stelle `# TODO Lab 12.3` die Generatorfunktion `rounds(player, scoreboard)`: In einer Schleife `while True:` fragt sie mit `ask_level()` die Stufe und gibt mit `yield` ein neues `logic.Game(player, scoreboard, level)` ab.
2. Ergänze direkt hinter dem `yield`: Antwortet `ask_play_again()` nicht mit `"j"`, beendet `return` den Generator.
3. Prüfe den Generator im interaktiven Modus: Starte im Ordner `playground/` `python` und gib ein:

   ```python
   from guess_game import players, storage, ui
   games = ui.rounds(players.ComputerPlayer(), storage.Scoreboard())
   game = next(games)
   game.level, game.attempts_left
   ```

   Beantworte die Stufenfrage mit `leicht`. Rufe danach noch einmal `next(games)` auf und antworte `n`. Beende mit `exit`.
4. Ersetze in `__main__.py` die Zeilen `play_again = "j"`, `while play_again == "j":`, die Stufenabfrage, das Erzeugen von `game` und das abschließende `play_again = ui.ask_play_again()` durch eine Zeile `for game in ui.rounds(player, scoreboard):`. Der übrige Rundenkörper bleibt unverändert.
5. Starte das Spiel mit `python -m guess_game`, spiele zwei Runden und beende mit `n`. Starte ein drittes Mal und brich bei `Tipp:` mit `Strg+C` ab.

## Checkpoint

- `games` ist ein `<generator object rounds at 0x…>`; erst `next(games)` stellt die Stufenfrage.
- `game.level, game.attempts_left` zeigt `('leicht', 5)`.
- Das zweite `next(games)` fragt `Nochmal spielen? (j/n):`; nach `n` erscheint `StopIteration`.
- Das Spiel läuft wie in Lab 12.2: Stufenfrage vor jeder Runde, `Nochmal spielen?` nach jeder Runde, danach Statistik und Abschied.
- `Strg+C` beendet mit `Spiel abgebrochen. Bis zum nächsten Mal!` ohne Traceback.

## Abschlusskriterien

- `ui.rounds` enthält `yield` und `return`; `__main__.py` enthält kein `play_again` und kein `while` mehr.

## Erweiterung

Lege `playground/warn_log.py` an: Eine Generatorfunktion `warn_times(path)` liest `../data/sample.log` Zeile für Zeile und gibt nur die Uhrzeit (zweites Wort) jeder Zeile mit der Stufe `WARN` ab. Eine `for`-Schleife gibt jede Uhrzeit als `Warnung um 08:03:51` aus. Start im Ordner `playground/` mit `python warn_log.py`.
