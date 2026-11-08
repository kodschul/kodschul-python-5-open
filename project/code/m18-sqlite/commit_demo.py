# Wann stehen die Daten wirklich in der Datei? Zwei Verbindungen zur selben Datei
# Vorher einmal: python code/m18-sqlite/init_sql_db.py
# Start im Ordner project/: python code/m18-sqlite/commit_demo.py

import sqlite3
from pathlib import Path

DB_FILE = Path("playground") / "customers.db"
COUNT = "SELECT COUNT(*) FROM customers"

writer = sqlite3.connect(DB_FILE)  # Verbindung 1: schreibt
reader = sqlite3.connect(DB_FILE)  # Verbindung 2: liest, wie ein zweites Programm

print("vorher:", reader.execute(COUNT).fetchone()[0], "Kunden")
writer.execute(
    "INSERT INTO customers (name, city, age) VALUES (?, ?, ?)", ("Test", "Testdorf", 1)
)
print("nach INSERT, ohne commit:", reader.execute(COUNT).fetchone()[0], "Kunden")
writer.commit()  # jetzt landet die Zeile in der Datei
print("nach commit:", reader.execute(COUNT).fetchone()[0], "Kunden")

# with connection: commit am Ende des Blocks, rollback (zurücknehmen) bei Fehler
try:
    with writer:
        writer.execute("DELETE FROM customers WHERE name = ?", ("Test",))
        raise ValueError("Fehler mitten in der Transaktion")
except ValueError as error:
    print("Fehler:", error)
print("nach Fehler im with-Block:", reader.execute(COUNT).fetchone()[0], "Kunden")

with writer:  # diesmal ohne Fehler: DELETE wird gespeichert (Testzeile weg)
    writer.execute("DELETE FROM customers WHERE name = ?", ("Test",))
print("nach DELETE im with-Block:", reader.execute(COUNT).fetchone()[0], "Kunden")

writer.close()  # with writer: schließt die Verbindung nicht, close bleibt nötig
reader.close()
