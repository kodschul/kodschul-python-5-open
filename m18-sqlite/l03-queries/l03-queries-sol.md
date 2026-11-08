# Lab 18.3 – Lösung: Abfragen und Auswertungen

Fertiger Stand: [project/examples/m18-sqlite/l03-queries/](../../project/examples/m18-sqlite/l03-queries/) mit geänderter [storage.py](../../project/examples/m18-sqlite/l03-queries/guess_game/storage.py), [ui.py](../../project/examples/m18-sqlite/l03-queries/guess_game/ui.py) und neu [migrate_json.py](../../project/examples/m18-sqlite/l03-queries/migrate_json.py).

## Aufgabe 1: Konstanten und to_scores

```python
# Bestenliste: die Datenbank sortiert und schneidet ab (LIMIT ? = count)
TOP_QUERIES = {
    "versuche": "SELECT * FROM scores ORDER BY tries, seconds LIMIT ?",
    "zeit": "SELECT * FROM scores ORDER BY seconds, tries LIMIT ?",
}

# Statistik: eine Ergebniszeile pro Stufe; won ist 1 oder 0, SUM zählt Gewinne
LEVEL_STATS = """
SELECT level,
       COUNT(*) AS games,
       SUM(won) AS wins,
       ROUND(100.0 * SUM(won) / COUNT(*)) AS win_rate,
       ROUND(AVG(tries), 1) AS avg_tries
FROM rounds
GROUP BY level
ORDER BY level
"""
```

```python
def to_scores(rows):
    """Macht aus Datenbankzeilen (sqlite3.Row) eine Liste von Score-Objekten."""
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
```

In `load()` bleibt davon nur `return to_scores(rows)`. Die Statistik liest aus `rounds` (alle Runden), die Bestenliste aus `scores` (nur Gewinne).

## Aufgabe 2: top, level_stats, add_many

```python
    def add_many(self, scores):
        """Speichert viele Gewinne auf einmal (executemany), z. B. bei der Migration."""
        rows = [score_values(score) for score in scores]
        self.connection.executemany(INSERT_SCORE, rows)  # ein INSERT pro Tupel
        self.connection.commit()
        self.scores.extend(scores)

    def top(self, by="versuche", count=10):
        """Gibt die besten Ergebnisse zurück: nach Versuchen, Zeit oder Punkten."""
        if by == "punkte":  # Punkte rechnet Python (LEVEL_POINTS), nicht SQL
            ranked = sorted(self.scores, key=lambda score: score.points(), reverse=True)
            return ranked[:count]
        rows = self.connection.execute(TOP_QUERIES[by], (count,)).fetchall()
        return to_scores(rows)

    def level_stats(self):
        """Spiele, Gewinne, Gewinnquote und Durchschnittsversuche pro Stufe."""
        return self.connection.execute(LEVEL_STATS).fetchall()
```

- `ORDER BY tries, seconds` entspricht `Score.__lt__` aus Lab 11.1: erst Versuche, bei Gleichstand die Zeit.
- `extend` hält `self.scores` auf dem Stand der Tabelle; sonst würde ein zweiter Aufruf im selben Lauf Einträge doppelt übernehmen.

## Aufgabe 3: ui.py

```python
    print("  bestenliste   Bestenliste zeigen (Top 10)")
    print("  statistik     Spiele, Gewinnquote und Versuche pro Stufe")
```

```python
    print(f"\nBestenliste (Top 10 nach {RANKINGS[by]})")
```

```python
def show_level_stats(rows):
    """Zeigt die Statistik aus game.db: gesamt und pro Stufe."""
    print("\nStatistik aller Runden (game.db)")
    if not rows:
        print("Noch keine Runden gespielt.")
        return
    games = sum(row["games"] for row in rows)  # Summe über alle Stufen
    wins = sum(row["wins"] for row in rows)
    rate = round(100 * wins / games)  # ganze Prozent
    print(f"Gesamt: {wins} von {games} Spielen gewonnen ({rate} %)")
    for row in rows:
        average = str(row["avg_tries"]).replace(".", ",")
        print(
            f"  {row['level']}: {row['wins']} von {row['games']} gewonnen "
            f"({round(row['win_rate'])} %) · Ø {average} Versuche"
        )
```

```python
            case ["statistik"]:
                show_level_stats(game.scoreboard.level_stats())  # GROUP BY
```

- `sum(row["games"] for row in rows)` ist eine Comprehension ohne eckige Klammern direkt in `sum` (Lab 12.3, Generator-Ausdruck).
- Die Gesamtquote rechnet Python aus den Zeilen; eine zweite Abfrage ohne `GROUP BY` ginge auch.
- `round(row['win_rate'])` macht aus `75.0` die ganze Zahl `75`; `replace(".", ",")` setzt das Komma wie in der übrigen Ausgabe des Spiels.

## Aufgabe 4: migrate_json.py

```python
# Migration: übernimmt highscores.json einmalig in die Tabelle scores von game.db
# Start im Ordner mit guess_game/ und highscores.json: python migrate_json.py
# Mehrfach starten schadet nicht: vorhandene Einträge werden übersprungen.

import sys

from guess_game import storage


def main():
    old_board = storage.Scoreboard("highscores.json")  # die JSON-Bestenliste
    if not old_board.path.exists():
        print("Keine highscores.json gefunden, nichts zu übernehmen.")
        sys.exit(1)
    old_scores = old_board.load()  # nur lesen, die JSON-Datei bleibt unverändert
    with storage.SqliteScoreboard("game.db") as board:
        # == vergleicht alle Felder (Dataclass): gleicher Eintrag = schon da
        new_scores = [score for score in old_scores if score not in board.scores]
        board.add_many(new_scores)
        total = len(board.scores)
    skipped = len(old_scores) - len(new_scores)
    print(f"highscores.json: {len(old_scores)} Einträge gelesen")
    print(f"Übernommen: {len(new_scores)} · schon vorhanden: {skipped}")
    print(f"game.db enthält jetzt {total} Einträge in der Tabelle scores.")


if __name__ == "__main__":
    main()
```

- `old_board.load()` statt `with storage.Scoreboard(...)`: Der `with`-Block würde die JSON-Datei am Ende neu schreiben (Lab 13.2); hier wird nur gelesen.
- Gleiche Einträge (Name, Stufe, Versuche, Sekunden, Datum) gelten als schon vorhanden. Bei echten Spielzeiten ist ein zufällig identischer Gewinn praktisch ausgeschlossen.

## Aufgabe 5: Testen

Vier Läufe vorher (Anna leicht: ein Gewinn, eine Niederlage; Anna schwer: ebenso; Computer mittel und leicht je zwei Gewinne), dann:

```text
$ python -m guess_game --level leicht --name Anna --player mensch
...
Tipp: statistik

Statistik aller Runden (game.db)
Gesamt: 6 von 8 Spielen gewonnen (75 %)
  leicht: 3 von 4 gewonnen (75 %) · Ø 3,8 Versuche
  mittel: 2 von 2 gewonnen (100 %) · Ø 4,0 Versuche
  schwer: 1 von 2 gewonnen (50 %) · Ø 6,0 Versuche
Tipp: bestenliste

Bestenliste (Top 10 nach Versuchen)
1. Computer – 2 Versuche – 0,0 s · mittel · 120 Punkte
2. Anna – 3 Versuche – 0,0 s · leicht · 30 Punkte
3. Computer – 3 Versuche – 0,0 s · leicht · 30 Punkte
4. Computer – 4 Versuche – 0,0 s · leicht · 20 Punkte
5. Anna – 5 Versuche – 0,0 s · schwer · 90 Punkte
6. Computer – 6 Versuche – 0,0 s · mittel · 40 Punkte
Tipp: quit
```

Migration mit `data/highscores_sample.json` als `highscores.json`:

```text
$ python migrate_json.py
highscores.json: 6 Einträge gelesen
Übernommen: 6 · schon vorhanden: 0
game.db enthält jetzt 12 Einträge in der Tabelle scores.
$ python migrate_json.py
highscores.json: 6 Einträge gelesen
Übernommen: 0 · schon vorhanden: 6
game.db enthält jetzt 12 Einträge in der Tabelle scores.
$ python -m sqlite3 game.db "SELECT COUNT(*) FROM scores"
(12,)
```

Danach mischt `bestenliste` alte und neue Einträge: `2. Jürgen – 2 Versuche – 21,7 s · leicht · 40 Punkte` steht direkt hinter dem Computer, `10.` ist `Computer – 6 Versuche`. Ohne `highscores.json` endet das Skript mit `Keine highscores.json gefunden, nichts zu übernehmen.` und Exit-Code `1`.

## Erweiterung: Tabelle players mit JOIN

```text
$ python -m sqlite3 game.db
sqlite> CREATE TABLE players (id INTEGER PRIMARY KEY, name TEXT UNIQUE, city TEXT);
sqlite> INSERT INTO players (name, city) VALUES ('Anna', 'Berlin'), ('Computer', 'Köln');
sqlite> SELECT players.city, COUNT(*) AS games, SUM(rounds.won) AS wins
    ... FROM rounds JOIN players ON rounds.name = players.name
    ... GROUP BY players.city ORDER BY players.city;
('Berlin', 4, 2)
('Köln', 4, 4)
```

- Ein `INSERT` kann mehrere Zeilen auf einmal einfügen: `VALUES (…), (…)`.
- Runden von Namen ohne Eintrag in `players` fallen beim `JOIN` weg.
- Sauberer wäre eine Spalte `player_id` in `rounds` als Fremdschlüssel auf `players.id`; dafür müsste das Spiel beim Speichern die `id` nachschlagen. Für den Kurs reicht der Name als Schlüssel.
