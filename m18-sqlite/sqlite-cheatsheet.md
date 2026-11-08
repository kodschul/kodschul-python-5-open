# Cheatsheet Modul 18: SQLite

## SQLite-Shell (Lab 18.1)

| Befehl | Wirkung |
| --- | --- |
| `python -m sqlite3 data/store.db` | Shell mit dieser Datenbank starten (seit Python 3.12) |
| `python -m sqlite3 game.db "SELECT * FROM rounds"` | eine Abfrage ausführen, Ergebnis zeigen, fertig |
| `SELECT name FROM sqlite_schema;` | alle Tabellen anzeigen |
| `SELECT sql FROM sqlite_schema WHERE name = 'customers';` | Spalten einer Tabelle (ihr `CREATE TABLE`) |
| `.help` · `.version` · `.quit` | Kurzhilfe · SQLite-Version · beenden |
| `;` | beendet jeden Befehl; ohne `;` wartet die Shell mit `...` |
| `python code/m18-sqlite/init_store_db.py` | `data/store.db` neu anlegen (Übungsdaten zurücksetzen) |

## Tabellen und Daten ändern (Lab 18.1)

| Befehl | Wirkung |
| --- | --- |
| `CREATE TABLE t (id INTEGER PRIMARY KEY, name TEXT NOT NULL)` | Tabelle mit Primärschlüssel und Pflichtfeld anlegen |
| `CREATE TABLE IF NOT EXISTS t (…)` | nur anlegen, wenn es die Tabelle noch nicht gibt |
| `INTEGER` · `REAL` · `TEXT` | ganze Zahl · Kommazahl · Text |
| `INSERT INTO t (name, age) VALUES ('Mia', 26)` | Zeile einfügen; `id` vergibt SQLite |
| `UPDATE t SET city = 'Dresden' WHERE id = 13` | Werte passender Zeilen ändern |
| `DELETE FROM t WHERE id = 13` | passende Zeilen löschen; ohne `WHERE`: alle |

## Abfragen (Lab 18.1, 18.3)

| Befehl | Wirkung |
| --- | --- |
| `SELECT * FROM t` | alle Spalten, alle Zeilen |
| `SELECT name, city FROM t` | nur diese Spalten |
| `WHERE city = 'Berlin'` | nur passende Zeilen; Text in `'…'` |
| `=` `<>` `<` `>` `<=` `>=` · `AND` `OR` | vergleichen · verknüpfen |
| `WHERE age IS NULL` | Zeilen ohne Wert in `age` |
| `WHERE order_date >= '2026-11-01'` | Datum als Text `JJJJ-MM-TT` vergleichen |
| `ORDER BY age DESC, name` | sortieren: absteigend, bei Gleichstand nach Name |
| `LIMIT 3` | nur die ersten 3 Zeilen |
| `-- Kommentar` | Kommentar in SQL |

## Gruppieren und verbinden (Lab 18.3)

| Befehl | Wirkung |
| --- | --- |
| `SELECT city, COUNT(*) FROM t GROUP BY city` | eine Zeile pro Stadt mit Anzahl |
| `COUNT(*)` · `SUM(x)` · `AVG(x)` · `MIN(x)` · `MAX(x)` | Anzahl · Summe · Durchschnitt (ohne `NULL`) · Minimum · Maximum |
| `ROUND(AVG(tries), 1)` | auf eine Nachkommastelle runden |
| `COUNT(*) AS games` | Ergebnisspalte benennen, in Python `row["games"]` |
| `100.0 * SUM(won) / COUNT(*)` | Prozent; `100.0` verhindert ganzzahlige Division |
| `FROM orders JOIN customers ON orders.customer_id = customers.id` | Zeilen zweier Tabellen über den Schlüssel verbinden |
| `customers.name` | Spalte `name` aus Tabelle `customers` |

## sqlite3 in Python (Lab 18.2)

| Befehl | Wirkung |
| --- | --- |
| `import sqlite3` | Modul laden (in Python enthalten) |
| `connection = sqlite3.connect("game.db")` | Verbindung öffnen; Datei entsteht, falls sie fehlt |
| `sqlite3.connect(":memory:")` | Datenbank nur im Arbeitsspeicher |
| `cursor = connection.cursor()` | Cursor anlegen |
| `connection.execute(sql, (wert,))` | Befehl ausführen (Abkürzung über die Verbindung) |
| `connection.executemany(sql, [(…), (…)])` | denselben Befehl für jedes Tupel |
| `….fetchone()` · `….fetchall()` | eine Ergebniszeile · alle Ergebniszeilen |
| `connection.commit()` | Änderungen endgültig speichern |
| `connection.rollback()` | Änderungen seit dem letzten Commit verwerfen |
| `connection.close()` | Verbindung schließen |
| `connection.row_factory = sqlite3.Row` | Zeilen mit Spaltennamen: `row["name"]` |
| `with connection:` | am Ende `commit`, bei Fehler `rollback`; schließt **nicht** |

## Platzhalter (Lab 18.2)

| Befehl | Wirkung |
| --- | --- |
| `execute("… WHERE city = ?", (city,))` | Wert sicher einsetzen; Tupel mit Komma |
| `execute("INSERT INTO t VALUES (?, ?)", ("Anna", 3))` | ein `?` pro Wert, Reihenfolge wie im Tupel |
| `execute("… LIMIT ?", (count,))` | auch Zahlen über `?` |
| `f"… WHERE name = '{name}'"` | **nie**: SQL-Injection |
| Tabellen- und Spaltennamen | nicht per `?`; feste Abfragen im Code, z. B. Dictionary `TOP_QUERIES` |

## Im Spiel (Lab 18.2, 18.3)

| Befehl | Wirkung |
| --- | --- |
| `with storage.SqliteScoreboard("game.db") as board:` | Bestenliste aus SQLite statt JSON |
| `board.add(score)` · `board.add_round(score)` | Gewinn in `scores` · jede Runde in `rounds` |
| `board.top("zeit")` | Top 10 per `ORDER BY … LIMIT ?` |
| `board.level_stats()` | Zeilen aus `GROUP BY level` |
| `board.add_many(scores)` | viele Gewinne per `executemany` |
| Befehl `statistik` | Spiele, Gewinnquote, Ø Versuche pro Stufe |
| `python migrate_json.py` | `highscores.json` einmalig nach `game.db` übernehmen |
| `python -m sqlite3 game.db "SELECT * FROM scores"` | Bestenliste direkt in der Datenbank ansehen |
