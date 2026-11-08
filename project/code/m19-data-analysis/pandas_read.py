# Dateien in DataFrames laden: CSV und Excel
# Start im Ordner project/: python code/m19-data-analysis/pandas_read.py

import pandas as pd

# 1. CSV mit Komma als Trennzeichen (Standard)
products = pd.read_csv("data/products.csv")
print("products.csv:")
print(products)

# 2. CSV des Spiels (Lab 8.3): Semikolon, Dezimalkomma, UTF-8 mit BOM
history = pd.read_csv(
    "data/history_sample.csv",
    sep=";",  # Trennzeichen
    decimal=",",  # "12,4" -> 12.4 (Zahl)
    encoding="utf-8-sig",  # BOM am Anfang nicht in den ersten Spaltennamen
)
print("\nhistory_sample.csv:")
print(history.head())  # die ersten fünf Zeilen
print("\nSpaltentypen:")
print(history.dtypes)  # Dauer ist eine Zahl (float64), keine Zeichenkette

# 3. Excel-Datei (braucht openpyxl, Lab 17.2)
items = pd.read_excel("data/shopping_items.xlsx")
print("\nshopping_items.xlsx:")
print(items)
