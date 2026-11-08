# Legt die Übungsdatenbank data/store.db neu an: Tabellen customers und orders
# Start im Ordner project/: python code/m18-sqlite/init_store_db.py
# Setzt die Datenbank auch zurück, nach eigenen Versuchen mit INSERT, UPDATE, DELETE.
# Alle Namen und Bestellungen sind erfunden.

import sqlite3
from pathlib import Path

DB_FILE = Path("data") / "store.db"

CREATE_CUSTOMERS = """
CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    age INTEGER,
    since TEXT NOT NULL
)
"""
CREATE_ORDERS = """
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES customers (id),
    product TEXT NOT NULL,
    price REAL NOT NULL,
    order_date TEXT NOT NULL
)
"""

# (name, city, age, since): since = Kundin/Kunde seit (JJJJ-MM-TT)
CUSTOMERS = [
    ("Anna Becker", "Berlin", 24, "2024-03-15"),
    ("Ben Schulz", "Hamburg", 31, "2023-11-02"),
    ("Cem Yılmaz", "Köln", 27, "2025-06-20"),
    ("Dana Wolf", "Berlin", 45, "2022-01-10"),
    ("Emil Braun", "München", 19, "2026-09-01"),
    ("Fatma Demir", "Stuttgart", 38, "2024-08-30"),
    ("Greta Hoffmann", "Hamburg", 52, "2021-05-05"),
    ("Hannes Koch", "Berlin", 22, "2026-10-12"),
    ("Ida Neumann", "Köln", 35, "2025-02-14"),
    ("Jonas Richter", "München", 29, "2023-07-07"),
    ("Jülide Kaya", "Stuttgart", 31, "2026-01-25"),
    ("Lena Fischer", "Berlin", None, "2026-11-01"),  # Alter unbekannt -> NULL
]

# (customer_id, product, price, order_date)
ORDERS = [
    (1, "Notizbuch", 4.50, "2026-10-03"),
    (1, "Kabel, 2 m", 4.99, "2026-10-28"),
    (2, "Mango", 1.99, "2026-10-05"),
    (2, "USB-Stick", 12.90, "2026-11-02"),
    (2, "Orange", 0.89, "2026-11-04"),
    (3, "Kopfhörer", 39.00, "2026-10-17"),
    (4, "Apfel", 0.45, "2026-10-09"),
    (4, "Notizbuch", 4.50, "2026-11-03"),
    (4, "Kabel, 2 m", 4.99, "2026-11-06"),
    (6, "USB-Stick", 12.90, "2026-10-22"),
    (7, "Kopfhörer", 39.00, "2026-11-01"),
    (8, "Mango", 1.99, "2026-11-05"),
    (9, "Apfel", 0.45, "2026-10-30"),
    (9, "Orange", 0.89, "2026-11-07"),
    (10, "Notizbuch", 4.50, "2026-10-12"),
    (11, "USB-Stick", 12.90, "2026-11-07"),
]


def main():
    DB_FILE.unlink(missing_ok=True)  # alte Datei löschen: immer derselbe Startzustand
    connection = sqlite3.connect(DB_FILE)  # legt die Datei neu an
    connection.execute(CREATE_CUSTOMERS)
    connection.execute(CREATE_ORDERS)
    connection.executemany(
        "INSERT INTO customers (name, city, age, since) VALUES (?, ?, ?, ?)", CUSTOMERS
    )
    connection.executemany(
        "INSERT INTO orders (customer_id, product, price, order_date) "
        "VALUES (?, ?, ?, ?)",
        ORDERS,
    )
    connection.commit()  # erst jetzt stehen die Zeilen in der Datei
    connection.close()
    print(f"{DB_FILE} angelegt: {len(CUSTOMERS)} Kunden, {len(ORDERS)} Bestellungen")


if __name__ == "__main__":
    main()
