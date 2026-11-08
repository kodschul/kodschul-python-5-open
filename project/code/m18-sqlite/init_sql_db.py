# Kundentabelle anlegen und befüllen: connect, cursor, execute, commit, close
# Start im Ordner project/: python code/m18-sqlite/init_sql_db.py

import sqlite3
from pathlib import Path

DB_FILE = Path("playground") / "customers.db"

NEW_CUSTOMERS = [
    ("Anna Becker", "Berlin", 24),
    ("Ben Schulz", "Hamburg", 31),
    ("Cem Yılmaz", "Köln", 27),
]

connection = sqlite3.connect(DB_FILE)  # öffnet die Datei, legt sie notfalls an
cursor = connection.cursor()  # Cursor: führt Befehle aus und liefert Ergebnisse

# IF NOT EXISTS: beim zweiten Start keine Fehlermeldung "table already exists"
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        city TEXT,
        age INTEGER
    )
""")

cursor.execute("SELECT COUNT(*) FROM customers")
count = cursor.fetchone()[0]  # eine Zeile als Tupel, z. B. (0,)
if count == 0:
    # ein Datensatz: Werte als Tupel, eingesetzt an den ?-Platzhaltern
    cursor.execute(
        "INSERT INTO customers (name, city, age) VALUES (?, ?, ?)",
        ("Eva Mustermann", "Stuttgart", 40),
    )
    # viele Datensätze: dasselbe INSERT einmal pro Tupel der Liste
    cursor.executemany(
        "INSERT INTO customers (name, city, age) VALUES (?, ?, ?)", NEW_CUSTOMERS
    )
    connection.commit()  # erst jetzt stehen die Zeilen sicher in der Datei
    print("4 Kunden eingefügt.")
else:
    print(f"Tabelle schon befüllt ({count} Kunden), nichts eingefügt.")

cursor.execute("SELECT * FROM customers")
for row in cursor.fetchall():  # alle Ergebniszeilen als Liste von Tupeln
    print(row)

connection.close()  # Verbindung schließen, Datei freigeben
