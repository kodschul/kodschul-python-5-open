# Lab 17.2 – Übung: Bestenliste als Excel-Datei

**Dauer:** ca. 15 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `export.py` bekommt `export_excel`, `--export` die Auswahl `excel`. Lab 17.3 ändert danach `logic.py`, `storage.py`, `ui.py` und `__main__.py`.
**Arbeitsdatei:** `playground/guess_game/export.py` und `playground/guess_game/__main__.py`
**Starter:** `starters/m17-l02-guess_game/` mit `__main__.py`, `export.py` (Spielstand nach Lab 17.1)

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel aus Lab 17.1 liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m17-data-formats/l01-xml-html/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m17-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen.
- `playground/highscores.json` braucht mindestens einen Eintrag (sonst wie in Lab 17.1 zwei Computer-Runden spielen).
- Die Stellen zum Ändern tragen den Kommentar `# TODO Lab 17.2`.

## Aufgaben

1. Importiere in `export.py` `Workbook` aus `openpyxl` und `Font` aus `openpyxl.styles`. Lege die Konstanten `EXCEL_FILE = Path("highscores.xlsx")` und `COLUMN_WIDTHS = {"A": 8, "B": 14, "C": 10, "D": 10, "E": 10, "F": 8, "G": 12}` an.
2. Schreibe `export_excel(scores, path=EXCEL_FILE)`: neue Arbeitsmappe, erstes Blatt in `Bestenliste` umbenennen, Kopfzeile `Platz, Name, Stufe, Versuche, Dauer (s), Punkte, Datum` anhängen und fett setzen, Datei speichern und `path` zurückgeben.
3. Hänge in `export_excel` vor dem Speichern pro Score eine Zeile an: Platz (gezählt wie in `export_html`), Name, Stufe, Versuche, Sekunden, Punkte, Datum. Zahlen bleiben Zahlen.
4. Setze die Spaltenbreiten aus `COLUMN_WIDTHS` mit einer `for`-Schleife über `.items()`.
5. Ergänze in `__main__.py` bei `--export` die Auswahl `"excel"` und rufe in `run_export` bei `args.export == "excel"` `export.export_excel(scores)` auf, sonst wie bisher `export_html`. Starte `python -m guess_game --export excel` und prüfe die Datei mit `python ../code/m17-data-formats/excel_peek.py highscores.xlsx`.

## Checkpoint

- `python -m guess_game --export excel` meldet `Bestenliste exportiert: highscores.xlsx (…)`; `--export html` funktioniert weiter.
- `excel_peek.py` zeigt `Blatt „Bestenliste“, Bereich A1:G…`, die Kopfzeile als `('Platz', 'Name', …)`, `Kopfzeile fett: [True, True, True, True, True, True, True]` und die Spaltenbreiten `A 8.0 … G 12.0`.
- In den Datenzeilen stehen Platz, Versuche und Punkte ohne Anführungszeichen, also als Zahlen.
- Wer Excel, LibreOffice oder Numbers installiert hat, öffnet `highscores.xlsx` mit Doppelklick: fette Kopfzeile, lesbare Spalten.

## Abschlusskriterien

- `highscores.xlsx` hat ein Blatt „Bestenliste“ mit fetter Kopfzeile, einer Zeile pro Eintrag und gesetzten Spaltenbreiten.
- `--export` akzeptiert genau `html` und `excel`.

## Erweiterung

Schreibe `playground/expensive_items.py`: Es liest `../data/shopping_items.xlsx` und schreibt alle Artikel mit einem Einzelpreis ab 2 € in die neue Datei `expensive_items.xlsx` (gleiche Kopfzeile, fett). Die Kursdatei bleibt unverändert.
