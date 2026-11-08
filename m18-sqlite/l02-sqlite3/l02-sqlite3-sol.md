# Lab 18.2 – Lösung: SQLite in Python

Fertiger Stand: [project/examples/m18-sqlite/l02-sqlite3/](../../project/examples/m18-sqlite/l02-sqlite3/) mit geänderter [storage.py](../../project/examples/m18-sqlite/l02-sqlite3/guess_game/storage.py) und [\_\_main\_\_.py](../../project/examples/m18-sqlite/l02-sqlite3/guess_game/__main__.py); alle anderen Dateien wie Lab 17.3.

## Aufgabe 1: Import, Konstanten, score_values

```python
import sqlite3
...
DB_FILE = Path("game.db")  # SQLite: Bestenliste und alle Runden in einer Datei
```

```python
# Tabelle scores = Bestenliste (wie highscores.json), nur Gewinne
# Tabelle rounds = jede Runde (wie history.csv), auch verlorene
# IF NOT EXISTS: beim ersten Start anlegen, danach nichts tun
CREATE_SCORES = """
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    level TEXT NOT NULL,
    tries INTEGER NOT NULL,
    seconds REAL NOT NULL,
    won INTEGER NOT NULL,
    date TEXT NOT NULL
)
"""
CREATE_ROUNDS = """
CREATE TABLE IF NOT EXISTS rounds (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    level TEXT NOT NULL,
    tries INTEGER NOT NULL,
    seconds REAL NOT NULL,
    won INTEGER NOT NULL,
    date TEXT NOT NULL
)
"""

# ? = Platzhalter: sqlite3 setzt die Werte sicher ein (nie f-Strings in SQL)
INSERT_SCORE = """
INSERT INTO scores (name, level, tries, seconds, won, date)
VALUES (?, ?, ?, ?, ?, ?)
"""
INSERT_ROUND = """
INSERT INTO rounds (name, level, tries, seconds, won, date)
VALUES (?, ?, ?, ?, ?, ?)
"""


def score_values(score):
    """Gibt die Werte eines Scores als Tupel in der Reihenfolge der Spalten zurück."""
    return (score.name, score.level, score.tries, score.seconds, score.won, score.date)
```

`id` fehlt im `INSERT`: SQLite vergibt die Nummer selbst. Die Reihenfolge im Tupel muss zur Spaltenliste im `INSERT` passen.

## Aufgabe 2: Klasse mit __init__, __enter__, __exit__

```python
class SqliteScoreboard:
    """Bestenliste in SQLite, gleiche Schnittstelle wie Scoreboard.

    with lädt, add() speichert, top() sortiert, scores enthält alle Gewinne.
    Neu: add_round() speichert jede Runde in der Tabelle rounds.
    """

    def __init__(self, path=DB_FILE):
        self.path = Path(path)
        self.connection = None  # Verbindung entsteht erst in __enter__
        self.scores = []

    def __enter__(self):
        """Beginn des with-Blocks: Datenbank öffnen, Tabellen anlegen, laden."""
        self.connection = sqlite3.connect(self.path)  # legt game.db notfalls an
        self.connection.row_factory = sqlite3.Row  # Zeilen mit Spaltennamen
        self.connection.execute(CREATE_SCORES)
        self.connection.execute(CREATE_ROUNDS)
        self.connection.commit()
        self.scores = self.load()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Ende des with-Blocks: Verbindung schließen (gespeichert ist schon)."""
        self.connection.close()
        return False  # Fehler nicht verschlucken, sondern weiterreichen
```

Die Verbindung entsteht erst in `__enter__`, wie das Laden der JSON-Datei in `Scoreboard` (Lab 13.2). `__exit__` muss nichts speichern, weil `add` sofort committet.

## Aufgabe 3: load, add, add_round, top, backup

```python
    def load(self):
        """Liest alle Zeilen der Tabelle scores als Liste von Score-Objekten."""
        rows = self.connection.execute("SELECT * FROM scores").fetchall()
        scores = []
        for row in rows:  # row["name"] dank row_factory = sqlite3.Row
            score = logic.Score(
                row["name"],
                row["level"],
                row["tries"],
                row["seconds"],
                bool(row["won"]),  # SQLite speichert True als 1
                row["date"],
            )
            scores.append(score)
        return scores

    def add(self, score):
        """Speichert einen Gewinn sofort in der Tabelle scores."""
        self.scores.append(score)
        self.connection.execute(INSERT_SCORE, score_values(score))
        self.connection.commit()  # erst jetzt steht die Zeile sicher in game.db

    def add_round(self, score):
        """Speichert eine Runde, ob gewonnen oder nicht, in der Tabelle rounds."""
        self.connection.execute(INSERT_ROUND, score_values(score))
        self.connection.commit()
```

`top()` ist eine 1:1-Kopie aus `Scoreboard`, weil `self.scores` dieselbe Liste von `Score`-Objekten enthält. In `backup()`:

```python
    game_files = [HIGHSCORES_FILE, HISTORY_FILE, DB_FILE]
    files = [path for path in game_files if path.exists()]
```

## Aufgabe 4: __main__.py

```python
def run_export(args):
    """Speichert die Top 10 der Bestenliste als Datei, ohne zu spielen."""
    with storage.SqliteScoreboard("game.db") as board:
        scores = board.top(count=10)
```

```python
    # with: öffnet game.db beim Betreten, schließt die Verbindung beim Verlassen
    with storage.SqliteScoreboard("game.db") as board:
        ...
            storage.append_history(score)  # jede Runde, auch verlorene
            board.add_round(score)  # jede Runde auch in game.db (Tabelle rounds)
            game.save_score(score)  # nur ein Gewinn kommt in die Bestenliste
```

`game.save_score(score)` in `logic.py` bleibt, wie es ist: Es ruft `self.scoreboard.add(score)` auf, und das ist jetzt die SQLite-Methode. `history.csv` wird weiter geschrieben; nichts davon stört.

## Aufgabe 5: Testen

Eingaben (Geheimzahl beim Testen zufällig, hier 76 und 70): `50 75 80 77 76`, Enter, `j`, `50 60 65 68 69 71 72`, `n`.

```text
$ python -m sqlite3 game.db "SELECT * FROM scores"
(1, 'Anna', 'schwer', 5, 0.0, 1, '2026-11-08')
$ python -m sqlite3 game.db "SELECT * FROM rounds"
(1, 'Anna', 'schwer', 5, 0.0, 1, '2026-11-08')
(2, 'Anna', 'schwer', 7, 0.0, 0, '2026-11-08')
$ python -m guess_game --level schwer --name Anna --player mensch
...
Tipp: bestenliste

Bestenliste (Top 5 nach Versuchen)
1. Anna – 5 Versuche – 0,0 s · schwer · 90 Punkte
Tipp: quit
```

Bei echten Spielen steht statt `0.0` die gemessene Dauer. Ein Gewinn steht in beiden Tabellen, eine verlorene Runde nur in `rounds`. Die Bestenliste vom Neustart kommt aus `game.db`; alte Einträge aus `highscores.json` fehlen noch (Migration in Lab 18.3).

## Erweiterung: products_db.py

```python
# Produkte aus data/products.csv in eine SQLite-Tabelle übernehmen und abfragen
# Start im Ordner playground/: python products_db.py

import csv
import sqlite3

connection = sqlite3.connect(":memory:")  # Übung: Datenbank nur im Speicher
connection.execute("CREATE TABLE products (name TEXT, price REAL, qty INTEGER)")

with open("../data/products.csv", encoding="utf-8", newline="") as file:
    rows = []
    for item in csv.DictReader(file):  # jede Zeile als Dictionary (Lab 8.3)
        rows.append((item["name"], float(item["price"]), int(item["qty"])))
connection.executemany("INSERT INTO products VALUES (?, ?, ?)", rows)
connection.commit()

cheap = connection.execute(
    "SELECT name, price FROM products WHERE price < ? ORDER BY price", (2,)
).fetchall()
print(f"{len(rows)} Produkte übernommen, unter 2 Euro:")
for name, price in cheap:
    print(f"  {name}: {price} Euro")
connection.close()
```

```text
$ python products_db.py
4 Produkte übernommen, unter 2 Euro:
  Apfel: 0.45 Euro
  Orange: 0.89 Euro
  Mango: 1.99 Euro
```

CSV liefert jeden Wert als Text; `float` und `int` wandeln vor dem Speichern um, damit `price < 2` als Zahl vergleicht. Ohne Spaltenliste im `INSERT` müssen die Werte in der Reihenfolge der Tabelle stehen.
