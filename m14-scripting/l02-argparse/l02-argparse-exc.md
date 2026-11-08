# Lab 14.2 – Übung: Das Spiel mit Optionen starten

**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — das Spiel liest `--name`, `--level` und `--player` aus der Kommandozeile und fragt nur noch, was fehlt; Lab 14.3 ergänzt weitere Optionen.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `__main__.py`, `ui.py`)
**Starter:** `starters/m14-l02-guess_game/` mit `__main__.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 14.1 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m14-scripting/l01-collections-itertools/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m14-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.

## Aufgaben

1. Importiere in `__main__.py` das Modul `argparse` und schreibe an der Stelle `# TODO Lab 14.2` die Funktion `parse_args()`: ein `ArgumentParser` mit `prog="python -m guess_game"`, einer `description` und einem `epilog` mit Beispielaufruf, dazu die Option `--name` mit `help`. Die Funktion gibt `parser.parse_args()` zurück.
2. Ergänze die Optionen `--level` (erlaubt: `list(logic.LEVELS)`) und `--player` (erlaubt: `"mensch"`, `"computer"`), beide mit `choices` und `help`.
3. Rufe in `main()` als Erstes `args = parse_args()` auf. Frage den Namen nur noch, wenn `args.name is None`; sonst gilt `args.name.strip().title()`. Frage den Spielertyp nur, wenn `args.player is None`.
4. Gib `ui.rounds` einen dritten Parameter `level=None`: `ask_level()` läuft nur noch, wenn `level` `None` ist. Übergib in `__main__.py` `args.level` an `ui.rounds`.
5. Teste im Ordner `playground/`:
   - `python -m guess_game --help`
   - `python -m guess_game --name Anna --level schwer --player mensch`, eine Runde spielen, dann `n`
   - `python -m guess_game --level extrem`, danach `echo $?` (macOS/Linux) bzw. `$LASTEXITCODE` (PowerShell)
   - `python -m guess_game` ohne Optionen

## Checkpoint

- `--help` zeigt `usage: python -m guess_game`, die drei Optionen mit ihren Werten in `{…}` und den Beispielaufruf.
- Mit allen drei Optionen erscheint nach dem Banner direkt `Stufe schwer, Anna: Rate eine Zahl zwischen 1 und 100.` ohne Frage nach Name, Spielertyp oder Stufe.
- `--level extrem` endet mit `invalid choice: 'extrem' (choose from leicht, mittel, schwer)`; der Exit-Code ist `2`.
- Ohne Optionen fragt das Spiel wie in Lab 14.1 nach Name, Spielertyp und Stufe.

## Abschlusskriterien

- `__main__.py` enthält `parse_args()` mit drei `add_argument`-Aufrufen; `main()` prüft mit `is None`.
- `ui.rounds` hat den Parameter `level=None`.

## Erweiterung

Lege `playground/count_files.py` an: Das Skript bekommt einen Ordner als Positionsargument und die Option `--ext` (Standard `txt`). Es zählt die Dateien im Ordner mit dieser Endung und gibt `Dateien mit .csv: 2` aus. Existiert der Ordner nicht, meldet es das und endet mit `sys.exit(1)`. Test im Ordner `playground/`: `python count_files.py ../data/messy_downloads --ext csv`, `python count_files.py ../data/nichtda` und `python count_files.py --help`.
