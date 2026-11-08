# pandas-DataFrame: eine Tabelle mit Spaltennamen, wie ein Excel-Blatt in Python
# Start im Ordner project/: python code/m19-data-analysis/pandas_basics.py

import pandas as pd  # Kurzname pd ist überall üblich

shopping_items = [
    {"name": "Orange", "qty": 7, "unit_price": 0.99},
    {"name": "Mango", "qty": 6, "unit_price": 2.99},
    {"name": "Limonade", "qty": 5, "unit_price": 1.99},
    {"name": "Apfel", "qty": 10, "unit_price": 0.45},
]

df = pd.DataFrame(shopping_items)  # Liste von Dictionaries -> Tabelle
print(df)  # links der Index 0, 1, 2 ... (Zeilennummer)
print("\nForm (Zeilen, Spalten):", df.shape)

# 1. Spalte wählen: eine Series (eine Spalte mit Index)
print("\nSpalte qty:")
print(df["qty"])

# 2. neue Spalte aus einer Rechnung: gilt für jede Zeile (wie bei NumPy)
df["total"] = df["qty"] * df["unit_price"]

# 3. filtern: Bedingung ergibt True/False je Zeile, df[...] behält nur True
print("\nTeurer als 1 Euro:")
print(df[df["unit_price"] > 1])

# 4. sortieren und Kennzahlen
print("\nNach Summe sortiert:")
print(df.sort_values("total", ascending=False))
print("\nKennzahlen der Spalte total:")
print(df["total"].describe().round(2))
