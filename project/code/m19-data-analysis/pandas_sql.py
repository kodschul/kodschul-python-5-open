# Dieselbe Frage einmal per SQL, einmal per pandas
# Start im Ordner project/: python code/m19-data-analysis/pandas_sql.py

import sqlite3

import pandas as pd

ORDERS = [
    ("Anna", "Bücher", 24.90),
    ("Ben", "Spiele", 59.99),
    ("Anna", "Spiele", 19.99),
    ("Chiara", "Bücher", 12.50),
    ("Ben", "Bücher", 8.99),
    ("Anna", "Bücher", 31.00),
]

# Datenbank nur im Arbeitsspeicher: ":memory:" statt Dateiname, nach close() weg
connection = sqlite3.connect(":memory:")
connection.execute("CREATE TABLE orders (customer TEXT, category TEXT, amount REAL)")
connection.executemany("INSERT INTO orders VALUES (?, ?, ?)", ORDERS)

# 1. read_sql: Ergebnis einer SELECT-Abfrage direkt als DataFrame
orders = pd.read_sql("SELECT * FROM orders", connection)
print(orders)

# 2. Summe pro Kategorie in SQL ...
query = """
SELECT category, COUNT(*) AS orders, ROUND(SUM(amount), 2) AS total
FROM orders
GROUP BY category
"""
print("\nSQL GROUP BY:")
print(pd.read_sql(query, connection))
connection.close()

# 3. ... und dieselbe Frage in pandas, plus Median (gibt es in SQLite nicht)
print("\npandas groupby:")
print(orders.groupby("category")["amount"].agg(["count", "sum", "median"]))
