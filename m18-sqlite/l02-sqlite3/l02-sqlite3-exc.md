# Lab 18.2 – Übung: SQLite in Python

**Dauer:** ca. 22 Minuten
**Ändert die Zahlenraten-Projektbasis?** Ja — `storage.py` bekommt `SqliteScoreboard`, `__main__.py` nutzt sie; das Spiel speichert ab jetzt in `game.db`. `logic.py`, `players.py` und `ui.py` bleiben unverändert.
**Arbeitsdatei:** `playground/guess_game/storage.py` und `playground/guess_game/__main__.py`
**Starter:** `starters/m18-l02-guess_game/` mit `__main__.py`, `storage.py` (Spielstand nach Lab 17.3)

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/` (sonst einmal `cd playground`).
- Das eigene Spiel liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m17-data-formats/l03-pickle/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m18-l02-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen. Die `TODO`-Kommentare im Starter zeigen die Stellen.
- Vorlage für Tabellen, SQL-Konstanten und Methoden: Abschnitt „Im Spiel: SqliteScoreboard“ der Theorie und die Klasse `Scoreboard` direkt darüber in `storage.py`.

## Aufgaben

1. Ergänze in `storage.py` `import sqlite3`, die Konstante `DB_FILE = Path("game.db")`, die vier SQL-Konstanten `CREATE_SCORES`, `CREATE_ROUNDS`, `INSERT_SCORE`, `INSERT_ROUND` (gleiche Spalten in beiden Tabellen, Werte nur über `?`) und eine Funktion `score_values(score)`, die die sechs Werte als Tupel in Spaltenreihenfolge zurückgibt.
2. Schreibe unter `Scoreboard` die Klasse `SqliteScoreboard`: `__init__(self, path=DB_FILE)` merkt sich den Pfad, setzt `connection` auf `None` und `scores` auf `[]`; `__enter__` verbindet, setzt `row_factory = sqlite3.Row`, legt beide Tabellen an, committet, lädt `scores` und gibt `self` zurück; `__exit__` schließt die Verbindung und gibt `False` zurück.
3. Ergänze die Methoden `load()` (alle Zeilen aus `scores` als `Score`-Objekte, `won` mit `bool(...)`), `add(score)` (an `scores` anhängen, `INSERT_SCORE`, `commit`), `add_round(score)` (`INSERT_ROUND`, `commit`) und `top()` (aus `Scoreboard` übernehmen). Nimm `DB_FILE` in die Dateiliste von `backup()` auf.
4. Ersetze in `__main__.py` beide `storage.Scoreboard("highscores.json")` durch `storage.SqliteScoreboard("game.db")` und speichere direkt nach `storage.append_history(score)` jede Runde mit `board.add_round(score)`.
5. Spiele `python -m guess_game --level schwer --name Anna --player mensch` eine gewonnene und eine verlorene Runde. Prüfe danach `python -m sqlite3 game.db "SELECT * FROM scores"` und `python -m sqlite3 game.db "SELECT * FROM rounds"`, starte das Spiel neu und tippe `bestenliste`.

## Checkpoint

- Nach dem Spiel liegt `game.db` in `playground/`; `scores` enthält eine Zeile mit `won` = `1`, `rounds` zwei Zeilen (`1` und `0`).
- Nach dem Neustart zeigt `bestenliste` den Gewinn aus dem ersten Lauf.

## Abschlusskriterien

- `logic.py`, `players.py` und `ui.py` sind unverändert (Vergleich in VS Code: Rechtsklick auf die eigene Datei → **Select for Compare**, auf die Datei im Starter → **Compare with Selected**).
- In `storage.py` steht kein f-String in einem SQL-Befehl.

## Erweiterung

Schreibe `playground/products_db.py`: eine Datenbank `":memory:"` mit Tabelle `products` (`name TEXT`, `price REAL`, `qty INTEGER`), gefüllt mit allen Zeilen aus `../data/products.csv` (`csv.DictReader`, `executemany`); danach Ausgabe aller Produkte unter 2 Euro, billigste zuerst (`WHERE price < ?`).
