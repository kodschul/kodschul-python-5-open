# Lab 18.3 – Übung: Abfragen und Auswertungen

**Dauer:** ca. 18 Minuten (allein oder zu zweit)
**Ändert die Zahlenraten-Projektbasis?** Ja — `storage.py` und `ui.py` bekommen SQL-Abfragen und den Befehl `statistik`; neben dem Paket entsteht `migrate_json.py`.
**Arbeitsdatei:** `playground/guess_game/storage.py`, `playground/guess_game/ui.py`, neu `playground/migrate_json.py`
**Starter:** `starters/m18-l03-guess_game/` mit `storage.py`, `ui.py` (Spielstand nach Lab 18.2)

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `playground/`.
- Das eigene Spiel liegt in `playground/guess_game/`. Ohne eigenen Stand: Ordner `playground/guess_game/` löschen oder umbenennen, `examples/m18-sqlite/l02-sqlite3/guess_game/` per **Copy**/**Paste** nach `playground/` kopieren, danach die Dateien aus `starters/m18-l03-guess_game/` nach `playground/guess_game/` kopieren und die vorhandenen ersetzen. die `TODO`-Kommentare zeigen die Stellen.
- Für die Migration braucht `playground/` eine `highscores.json` (aus den Labs bis 17.3). Fehlt sie: `data/highscores_sample.json` nach `playground/` kopieren und in `highscores.json` umbenennen.

## Aufgaben

1. Ergänze in `storage.py` die Konstanten `TOP_QUERIES` und `LEVEL_STATS` aus der Theorie. Verschiebe die Schleife aus `SqliteScoreboard.load()` in eine Funktion `to_scores(rows)` und nutze sie in `load()`.
2. Ändere `SqliteScoreboard.top()`: Standard `count=10`; `punkte` sortiert weiter Python, `versuche` und `zeit` holen die Zeilen per `TOP_QUERIES[by]` mit `(count,)`. Ergänze `level_stats()` (führt `LEVEL_STATS` aus, gibt alle Zeilen zurück) und `add_many(scores)` (mit `executemany`, `commit`, danach `self.scores.extend(scores)`).
3. Ergänze in `ui.py` die Funktion `show_level_stats(rows)`, die Überschrift `Bestenliste (Top 10 nach …)`, die Hilfezeilen `bestenliste   Bestenliste zeigen (Top 10)` und `statistik     Spiele, Gewinnquote und Versuche pro Stufe` sowie `case ["statistik"]:` im Befehlsmenü. Ausgabe wie im Checkpoint; ohne Zeilen nur `Noch keine Runden gespielt.`
4. Schreibe `playground/migrate_json.py`: alte Einträge mit `storage.Scoreboard("highscores.json").load()` lesen (fehlt die Datei: `Keine highscores.json gefunden, nichts zu übernehmen.` und `sys.exit(1)`), in `with storage.SqliteScoreboard("game.db") as board:` nur Einträge übernehmen, die noch nicht in `board.scores` stehen, und drei Zeilen ausgeben, z. B. `highscores.json: 6 Einträge gelesen`, `Übernommen: 6 · schon vorhanden: 0`, `game.db enthält jetzt 12 Einträge in der Tabelle scores.`
5. Spiele einige Runden (auch verlorene, auch mit `--player computer`), tippe dann `statistik` und `bestenliste`. Starte `python migrate_json.py` zweimal und prüfe danach `bestenliste` erneut.

## Checkpoint

- `statistik` zeigt z. B.:

  ```text
  Statistik aller Runden (game.db)
  Gesamt: 6 von 8 Spielen gewonnen (75 %)
    leicht: 3 von 4 gewonnen (75 %) · Ø 3,8 Versuche
    mittel: 2 von 2 gewonnen (100 %) · Ø 4,0 Versuche
    schwer: 1 von 2 gewonnen (50 %) · Ø 6,0 Versuche
  ```

- `bestenliste` zeigt bis zu 10 Einträge, sortiert nach Versuchen, bei Gleichstand nach Zeit.
- Der zweite Lauf von `migrate_json.py` meldet `Übernommen: 0`; danach stehen alte und neue Einträge gemeinsam in der Bestenliste.

## Abschlusskriterien

- `python -m sqlite3 game.db "SELECT COUNT(*) FROM scores"` zeigt dieselbe Zahl wie die letzte Zeile von `migrate_json.py`.
- In `storage.py` steht kein f-String in einem SQL-Befehl.

## Erweiterung

Lege in `game.db` per Shell (`python -m sqlite3 game.db`) eine Tabelle `players` an (`id INTEGER PRIMARY KEY`, `name TEXT UNIQUE`, `city TEXT`; `UNIQUE` erlaubt jeden Namen nur einmal) und trage zwei Namen aus der Bestenliste mit einer Stadt ein. Zeige dann per `JOIN … ON rounds.name = players.name` für jede Stadt die Zahl der Runden und der Gewinne.
