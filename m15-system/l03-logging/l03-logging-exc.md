# Lab 15.3 – Übung: game.log und --verbose

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel schreibt `game.log` und kennt `--verbose`; Lab 16.3 wertet die Ergebniszeilen aus `game.log` aus.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `__main__.py`, `ui.py`, `logic.py`)
**Starter:** `starters/m15-l03-guess_game/` mit `__main__.py`, `logic.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 15.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m15-system/l02-regex/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m15-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Ergänze in `__main__.py` `import logging`, die Konstante `LOG_FILE = "game.log"`, den Logger `logger = logging.getLogger("guess_game")` und die Funktion `setup_logging(verbose)` aus der Theorie. Lege in `parse_args()` die Option `--verbose` an (`store_true`, Hilfetext `Protokoll auch im Terminal zeigen`) und rufe `setup_logging(args.verbose)` direkt nach `parse_args()` auf.
2. Schreibe in `main()` INFO-Zeilen: `Programm gestartet mit {sys.argv[1:]}`, `Spiel gestartet: {name}, es rät {player.name}`, zu Beginn jeder Runde `Neue Runde: Stufe {game.level}`, nach jeder Runde `Gewonnen: {score} · {score.level}` bzw. `Verloren: {score} · {score.level}`, bei `quit` `Spiel mit quit beendet` und am Ende `Programm beendet`.
3. Lege in `ui.py` und `logic.py` je einen Logger mit `logging.getLogger(__name__)` an. In `ui.make_guess` kommt jeder Tipp als DEBUG ins Log (`Tipp 50: zu niedrig`, bei ungültigem Tipp `Tipp 500 ungültig: <Fehlertext>`), im Decorator `logic.timed` die Dauer (`play_round dauerte 0.0 s`).
4. Ergänze im Start-Block unter dem `except KeyboardInterrupt` (dort zusätzlich INFO `Mit Strg+C abgebrochen`) einen Zweig `except Exception:` mit `logger.exception("Unerwarteter Fehler")`, der Meldung `Ein Fehler ist aufgetreten. Details stehen in game.log.` und `sys.exit(1)`.
5. Teste: Spiele mit `python -m guess_game --level schwer --name Anna` zwei Runden und öffne danach `playground/game.log` in VS Code. Starte dann `python -m guess_game --level leicht --name Ben --player computer --verbose`. Ersetze zuletzt den Inhalt von `highscores.json` durch `[{"name": "Anna"`, starte das Spiel, lies den Fehler in `game.log` und lösche danach `highscores.json`.

## Checkpoint

- Ohne `--verbose` sieht das Spiel im Terminal aus wie in Lab 15.2.
- `game.log` enthält pro Runde eine Zeile `INFO guess_game: Neue Runde: …`, DEBUG-Zeilen von `guess_game.ui` für jeden Tipp, eine DEBUG-Zeile von `guess_game.logic` und eine Zeile `Gewonnen: …` oder `Verloren: …`.
- Mit `--verbose` stehen die Log-Zeilen mit Zeitstempel zwischen den Spielzeilen.
- Mit der kaputten `highscores.json` erscheint nur „Ein Fehler ist aufgetreten. Details stehen in game.log.“; `game.log` enthält `ERROR guess_game: Unerwarteter Fehler` und einen Traceback, der mit `json.decoder.JSONDecodeError` endet.

## Abschlusskriterien

- `python -c "from guess_game import logic; print(logic.parse_log_line(open('game.log', encoding='utf-8').readlines()[-2]))"` zeigt nach einem gewonnenen Spiel ein Dictionary (vorletzte Zeile = Ergebniszeile).

## Erweiterung

Lege `playground/grades_check.py` an: `basicConfig` schreibt alles ab INFO mit Zeitstempel nach `grades.log`. Das Skript geht die Liste `[1.7, 2.3, 6.0, 1.0]` durch, schreibt für jede Note zwischen 1.0 und 5.0 eine INFO-Zeile `Note 1.7 ok` und sonst eine WARNING-Zeile `Note 6.0 ungültig`, und gibt am Ende mit `print` nur `Fertig, Details in grades.log.` aus.
