# Lab 18.1 – Lösung: Datenbanken und SQL

Kein Spielstand: Die Übung ändert das Spiel nicht. Ausgaben unten aus einem echten Lauf mit Python 3.14.2; die SQLite-Version in der ersten Zeile hängt von der Installation ab.

## Aufgabe 1: Shell starten, Tabellen und Spalten

```text
$ python -m sqlite3 data/store.db
sqlite3 shell, running on SQLite version 3.51.1
Connected to 'data/store.db'

Each command will be run using execute() on the cursor.
Type ".help" for more information; type ".quit" or CTRL-D to quit.
sqlite> .help
Enter SQL code and press enter.
sqlite> SELECT name FROM sqlite_schema;
('customers',)
('orders',)
sqlite> SELECT sql FROM sqlite_schema WHERE name = 'customers';
('CREATE TABLE customers (\n    id INTEGER PRIMARY KEY,\n    name TEXT NOT NULL,\n    city TEXT NOT NULL,\n    age INTEGER,\n    since TEXT NOT NULL\n)',)
```

`\n` steht für einen Zeilenumbruch im gespeicherten Befehl. Jedes Ergebnis ist ein Tupel; ein Tupel mit einem Wert endet mit Komma (Lab 4.2).

## Aufgabe 2: Abfrage 1, Name und Stadt

```text
sqlite> SELECT name, city FROM customers;
('Anna Becker', 'Berlin')
('Ben Schulz', 'Hamburg')
('Cem Yılmaz', 'Köln')
('Dana Wolf', 'Berlin')
('Emil Braun', 'München')
('Fatma Demir', 'Stuttgart')
('Greta Hoffmann', 'Hamburg')
('Hannes Koch', 'Berlin')
('Ida Neumann', 'Köln')
('Jonas Richter', 'München')
('Jülide Kaya', 'Stuttgart')
('Lena Fischer', 'Berlin')
```

Ohne `ORDER BY` ist die Reihenfolge nicht garantiert; hier ist es die Reihenfolge des Einfügens.

## Aufgabe 3: Abfrage 2, Kunden aus Hamburg

```text
sqlite> SELECT * FROM customers WHERE city = 'Hamburg';
(2, 'Ben Schulz', 'Hamburg', 31, '2023-11-02')
(7, 'Greta Hoffmann', 'Hamburg', 52, '2021-05-05')
```

## Aufgabe 4: Abfrage 3, älter als 30, älteste zuerst

```text
sqlite> SELECT name, age FROM customers WHERE age > 30 ORDER BY age DESC;
('Greta Hoffmann', 52)
('Dana Wolf', 45)
('Fatma Demir', 38)
('Ida Neumann', 35)
('Ben Schulz', 31)
('Jülide Kaya', 31)
```

Lena Fischer fehlt: Ihr Alter ist `NULL`, und `NULL > 30` ist nicht wahr. Bei gleichem Alter (31) legt `ORDER BY age DESC, name` die Reihenfolge zusätzlich nach Namen fest.

## Aufgabe 5: Abfrage ohne Shell

```text
sqlite> .quit
$ python -m sqlite3 data/store.db "SELECT name, age FROM customers WHERE age > 30 ORDER BY age DESC"
('Greta Hoffmann', 52)
('Dana Wolf', 45)
('Fatma Demir', 38)
('Ida Neumann', 35)
('Ben Schulz', 31)
('Jülide Kaya', 31)
```

Die Abfrage steht in `"…"`, weil sie Leerzeichen enthält; das `;` ist hier nicht nötig. Diese Form nutzt Lab 18.2, um `game.db` nach dem Spielen zu prüfen.

## Erweiterung: INSERT, UPDATE, DELETE

```text
sqlite> INSERT INTO customers (name, city, age, since) VALUES ('Mia Lang', 'Leipzig', 26, '2026-11-08');
sqlite> SELECT * FROM customers WHERE name = 'Mia Lang';
(13, 'Mia Lang', 'Leipzig', 26, '2026-11-08')
sqlite> UPDATE customers SET city = 'Dresden' WHERE name = 'Mia Lang';
sqlite> SELECT * FROM customers WHERE name = 'Mia Lang';
(13, 'Mia Lang', 'Dresden', 26, '2026-11-08')
sqlite> DELETE FROM customers WHERE name = 'Mia Lang';
sqlite> SELECT COUNT(*) FROM customers;
(12,)
```

- Die `id` 13 vergibt SQLite selbst, weil die Spalte `id` fehlt.
- `COUNT(*)` zählt Zeilen; mehr dazu in Lab 18.3.
- Zurücksetzen:

```text
$ python code/m18-sqlite/init_store_db.py
data/store.db angelegt: 12 Kunden, 16 Bestellungen
```
