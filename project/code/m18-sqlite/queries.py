# Abfragen auf data/store.db: sortieren, begrenzen, gruppieren, verbinden
# Start im Ordner project/: python code/m18-sqlite/queries.py
# (Datenbank fehlt oder verändert? python code/m18-sqlite/init_store_db.py)

import sqlite3
from pathlib import Path

DB_FILE = Path("data") / "store.db"


def show(connection, title, sql, parameters=()):
    """Führt eine Abfrage aus und druckt Überschrift und Ergebniszeilen."""
    print(f"\n{title}")
    for row in connection.execute(sql, parameters).fetchall():
        print(" ", row)  # jede Zeile ist ein Tupel


connection = sqlite3.connect(DB_FILE)

# ORDER BY ... DESC: absteigend; LIMIT: nur die ersten n Zeilen
show(
    connection,
    "Die drei teuersten Bestellungen:",
    "SELECT product, price FROM orders ORDER BY price DESC, product LIMIT ?",
    (3,),
)

# Datum als Text JJJJ-MM-TT: Textvergleich = zeitlicher Vergleich
show(
    connection,
    "Bestellungen ab 01.11.2026:",
    "SELECT order_date, product FROM orders WHERE order_date >= ? ORDER BY order_date",
    ("2026-11-01",),
)

# GROUP BY: eine Ergebniszeile pro Stadt; COUNT, AVG, MIN rechnen pro Gruppe
show(
    connection,
    "Kunden pro Stadt (Anzahl, Ø Alter, jüngste Person):",
    """
    SELECT city, COUNT(*) AS customers, ROUND(AVG(age), 1) AS avg_age, MIN(age)
    FROM customers
    GROUP BY city
    ORDER BY customers DESC, city
    """,
)

# JOIN: Zeilen zweier Tabellen über den Schlüssel verbinden
show(
    connection,
    "Umsatz pro Kunde (JOIN customers + orders):",
    """
    SELECT customers.name, COUNT(*) AS orders, ROUND(SUM(orders.price), 2) AS total
    FROM orders
    JOIN customers ON orders.customer_id = customers.id
    GROUP BY customers.id
    ORDER BY total DESC, customers.name
    LIMIT 3
    """,
)

connection.close()
