# Kunden einer Stadt suchen: Eingabe über ?-Platzhalter, Zeilen mit Spaltennamen
# Vorher einmal: python code/m18-sqlite/init_sql_db.py
# Start im Ordner project/: python code/m18-sqlite/sql_db.py

import sqlite3
import sys
from pathlib import Path

DB_FILE = Path("playground") / "customers.db"

if not DB_FILE.exists():  # connect würde sonst eine leere Datenbank anlegen
    print(f"{DB_FILE} fehlt. Erst init_sql_db.py starten.")
    sys.exit(1)

connection = sqlite3.connect(DB_FILE)
connection.row_factory = sqlite3.Row  # Zeilen wie Dictionaries: row["name"]

city = input("Stadt: ").strip()
# execute direkt auf der Verbindung: Abkürzung, legt den Cursor selbst an
rows = connection.execute(
    "SELECT name, age FROM customers WHERE city = ? ORDER BY name",
    (city,),  # Tupel mit einem Wert: Komma nicht vergessen
).fetchall()

if not rows:
    print(f"Keine Kunden in {city}.")
for row in rows:
    print(f"{row['name']} ({row['age']} Jahre)")

connection.close()
