# Lab 14.3 – Übung: Backup der Spieldateien mit Trockenlauf

**Dauer:** ca. 27 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `python -m guess_game --backup` sichert `highscores.json` und `history.csv` in `backups/<Datum_Uhrzeit>/`, behält nur die neuesten Backups und kennt `--keep` und `--dry-run`.
**Arbeitsdatei:** `playground/guess_game/` (geändert: `storage.py`, `ui.py`, `__main__.py`)
**Starter:** `starters/m14-l03-guess_game/` mit `__main__.py`, `storage.py`, `ui.py`

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 14.2 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m14-scripting/l02-argparse/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m14-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- In `playground/` liegen `highscores.json` und `history.csv`. Fehlen sie: einmal `python -m guess_game --name Anna --level leicht --player computer` spielen und mit `n` beenden.

## Aufgaben

1. Ergänze in `storage.py` die Importe `shutil` und `from datetime import datetime` sowie `BACKUP_DIR = Path("backups")`. Schreibe an der Stelle `# TODO Lab 14.3` die Funktion `backup(keep=5, dry_run=False)`: Sie sammelt in `files` die vorhandenen Dateien aus `HIGHSCORES_FILE` und `HISTORY_FILE`, bildet `target = BACKUP_DIR / datetime.now().strftime("%Y-%m-%d_%H%M")`, legt `target` mit `mkdir(parents=True, exist_ok=True)` an, kopiert jede Datei mit `copy_into(target)` und gibt `target, files, old_folders` zurück (`old_folders` vorerst `[]`).
2. Schreibe in `ui.py` die Funktion `show_backup(target, files, old_folders, dry_run)`. Ausgabe im Trockenlauf zuerst `Trockenlauf: Es wird nichts kopiert und nichts gelöscht.`, dann pro Datei `Kopieren: highscores.json -> backups/…`, pro altem Ordner `Löschen:  backups/…` und, nur ohne Trockenlauf, `Backup fertig: 2 Dateien in backups/…`.
3. Ergänze in `__main__.py` (`import sys`) die Optionen `--backup` und `--dry-run` (beide `action="store_true"`) sowie `--keep` (`type=int`, `default=5`). Schreibe `run_backup(args)`: ruft `storage.backup(args.keep, args.dry_run)` auf; ist `files` leer, gibt sie `Keine Spieldateien gefunden, nichts zu sichern.` aus und endet mit `sys.exit(1)`, sonst ruft sie `ui.show_backup(...)` auf. In `main()` direkt nach `parse_args()`: Mit `--backup` läuft nur `run_backup(args)`, dann `return`.
4. Baue Rotation und Trockenlauf in `backup()` ein: Sammle vor dem Anlegen alle vorhandenen Ordner aus `BACKUP_DIR.iterdir()` (nur, wenn `BACKUP_DIR` existiert), hänge `target` an, falls er fehlt, und berechne `old_folders = sorted(folders)[:-keep]`. Mit `dry_run` oder ohne Dateien kehrt die Funktion **vor** `mkdir` zurück. Nach dem Kopieren löscht `shutil.rmtree` jeden Ordner aus `old_folders`.
5. Teste im Ordner `playground/`: Lege im Explorer von VS Code mit **New Folder** die leeren Ordner `backups/2026-11-01_0900` und `backups/2026-11-02_0900` an (der Name mit `/` legt beide Ebenen an). Starte `python -m guess_game --backup --keep 2 --dry-run`, prüfe im Explorer, dass sich nichts geändert hat, und starte dann `python -m guess_game --backup --keep 2`.

## Checkpoint

- Der Trockenlauf beginnt mit `Trockenlauf: …`, listet `Kopieren: highscores.json -> backups/…` und `Kopieren: history.csv -> backups/…` sowie `Löschen:  backups/2026-11-01_0900`; der Explorer zeigt danach noch dieselben zwei Ordner.
- Der echte Lauf endet mit `Backup fertig: 2 Dateien in backups/…`; in `backups/` stehen danach `2026-11-02_0900` und der neue Ordner mit beiden Dateien.
- `python -m guess_game --help` zeigt `--backup`, `--keep KEEP` und `--dry-run`.

## Abschlusskriterien

- `storage.backup()` enthält `copy_into`, `shutil.rmtree` und ein `return` vor dem ersten ändernden Befehl.
- `python -m guess_game` ohne `--backup` startet das Spiel wie in Lab 14.2.

## Erweiterung

Lege `playground/sort_by_letter.py` an: Das Skript bekommt einen Ordner als Positionsargument und die Option `--dry-run`. Es verschiebt jede Datei (nicht die Unterordner) in einen Unterordner mit ihrem großgeschriebenen Anfangsbuchstaben (`notizen.txt` → `N/`) und gibt pro Datei eine Zeile `notizen.txt -> N/` aus; im Trockenlauf verschiebt es nichts. Teste auf der Testkopie: im Ordner `project/` erst `python code/m14-scripting/make_sandbox.py`, dann im Ordner `playground/` `python sort_by_letter.py messy_downloads --dry-run` und ohne `--dry-run`.
