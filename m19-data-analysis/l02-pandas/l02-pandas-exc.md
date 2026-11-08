# Lab 19.2 – Übung: Spielrunden mit pandas auswerten

**Dauer:** ca. 20 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — neben dem Paket entsteht `analyze.py`; das Paket `guess_game/` bleibt unverändert. Lab 19.3 nutzt dieselbe Ladefunktion für die Diagramme.
**Arbeitsdatei:** `playground/analyze.py` (neu, neben `playground/guess_game/`)
**Starter:** keiner; `analyze.py` entsteht ohne Vorlage, das Spiel bleibt auf dem Stand nach Lab 19.1

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/`.
- Ohne eigenen Spielstand: Ordner `playground/guess_game/` löschen oder umbenennen und `examples/m19-data-analysis/l01-multiline-regex/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren.
- `game.db` braucht einige Runden auf mindestens zwei Stufen und von zwei Spielern. Wer noch keine hat, spielt z. B. `python -m guess_game --level leicht --name Ben --player computer` und `python -m guess_game --level schwer --name Anna --player mensch` mit je zwei Runden. `python -m sqlite3 game.db "SELECT COUNT(*) FROM rounds"` zeigt die Zahl der Runden.

## Aufgaben

1. Lege `playground/analyze.py` an: Imports (`sqlite3`, `sys`, `Path`, `pandas as pd`), Konstante `DB_FILE = Path("game.db")` und eine Funktion `load_rounds(path=DB_FILE)`, die per `pd.read_sql` alle Zeilen der Tabelle `rounds` als DataFrame zurückgibt. In `main()`: Fehlt `game.db`, folgt die Meldung `game.db nicht gefunden. Erst spielen (SQLite ab Lab 18.2).` und `sys.exit(1)`; sonst `8 Runden aus game.db` (mit der echten Zahl) und die ersten fünf Zeilen.
2. Gib unter der Überschrift `Versuche (alle Runden):` die Kennzahlen der Spalte `tries` aus (`describe`, auf eine Nachkommastelle gerundet).
3. Schreibe `summary(rounds, column)`: Bündle die Zeilen mit `groupby(column)` und gib einen DataFrame mit den Spalten `Spiele`, `Gewinnquote %` (gerundet), `Median Versuche` und `Ø Versuche` (eine Nachkommastelle) zurück. Gib das Ergebnis für `"level"` unter `Pro Stufe (pandas):` aus.
4. Gib dieselbe Zusammenfassung für `"name"` unter `Pro Spieler (pandas):` aus, sortiert nach Gewinnquote, höchste zuerst.
5. Führe die `statistik`-Abfrage aus Lab 18.3 (ohne die Spalte `wins`) per `pd.read_sql` aus und gib sie unter `Pro Stufe (SQL wie in Lab 18.3, ohne Median):` aus. Vergleiche mit dem Befehl `statistik` im Spiel. Teste zum Schluss den Fehlerfall: Starte `python analyze.py` in einem Ordner ohne `game.db` (z. B. `cd ..`, `python playground/analyze.py`, danach `cd playground`).

## Checkpoint

- Nach Aufgabe 1: Die Zahl der Runden entspricht `SELECT COUNT(*) FROM rounds`; die Tabelle zeigt die Spalten `id name level tries seconds won date`.
- Gewinnquote und Ø Versuche pro Stufe aus pandas und aus SQL sind gleich; nur pandas hat den Median.
- Gewinnquote und Durchschnitt stimmen mit dem Spielbefehl `statistik` überein.
- Ohne `game.db`: Meldung und Exit-Code `1` (PowerShell `$LASTEXITCODE`, macOS/Linux `echo $?`), keine leere `game.db` im Ordner.

## Abschlusskriterien

- `python analyze.py` läuft ohne Rückfragen und gibt Runden, Kennzahlen, „Pro Stufe“, „Pro Spieler“ und den SQL-Vergleich aus.

## Erweiterung

Schreibe ohne Vorlage `playground/sales.py`, das [data/umsatz_pro_ort.csv](../../project/data/umsatz_pro_ort.csv) lädt (aus `playground/` gesehen: `../data/umsatz_pro_ort.csv`) und pro Region den größten und den kleinsten Umsatz sowie die Anzahl der Orte ausgibt, sortiert nach dem größten Umsatz.
