# Lab 18.1 – Übung: Datenbanken und SQL

**Dauer:** ca. 12 Minuten
**Ändert die Zahlenraten-Projektbasis?** Nein — die Übung fragt die Beispiel-Datenbank `data/store.db` ab; das Spiel speichert ab Lab 18.2 in SQLite.
**Arbeitsdatei:** keine; alle Befehle laufen in der SQLite-Shell

## Vorbereitung

- Terminal in VS Code, `.venv` aktiv, im Ordner `project/` (nicht `playground/`).
- `data/store.db` enthält die Tabellen `customers` (12 erfundene Kundinnen und Kunden) und `orders`. Wurde die Datei schon verändert: `python code/m18-sqlite/init_store_db.py` stellt den Ausgangszustand her.

## Aufgaben

1. Starte die Shell mit `python -m sqlite3 data/store.db`. Rufe `.help` auf, zeige mit `SELECT name FROM sqlite_schema;` die Tabellen an und mit `SELECT sql FROM sqlite_schema WHERE name = 'customers';` die Spalten von `customers`.
2. Abfrage 1: Zeige Name und Stadt aller Kunden.
3. Abfrage 2: Zeige alle Spalten der Kunden aus Hamburg.
4. Abfrage 3: Zeige Name und Alter aller Kunden, die älter als 30 sind, die ältesten zuerst.
5. Beende die Shell mit `.quit` und führe Abfrage 3 noch einmal ohne Shell aus: `python -m sqlite3 data/store.db "<Abfrage>"`.

## Checkpoint

- Aufgabe 1 zeigt die Tabellen `customers` und `orders` und die fünf Spalten `id`, `name`, `city`, `age`, `since`.
- Abfrage 1 liefert 12 Zeilen, Abfrage 2 zwei Zeilen, Abfrage 3 sechs Zeilen, beginnend mit `('Greta Hoffmann', 52)`.
- Aufgabe 5 zeigt dieselben sechs Zeilen ohne Begrüßungstext der Shell.

## Abschlusskriterien

- Drei Abfragen laufen ohne Fehlermeldung und liefern die Zeilenzahlen aus dem Checkpoint.

## Erweiterung

Füge in der Shell eine eigene Kundin mit `INSERT` ein, ändere danach ihre Stadt mit `UPDATE` und lösche sie mit `DELETE`; prüfe jeden Schritt mit einem `SELECT`. Setze die Datenbank anschließend mit `python code/m18-sqlite/init_store_db.py` zurück.
