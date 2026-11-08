# Umsatz pro Region: gruppieren, zusammenfassen, sortieren (erfundene Umsätze)
# Start im Ordner project/: python code/m19-data-analysis/region_stat_pd.py

import pandas as pd

sales = pd.read_csv("data/umsatz_pro_ort.csv")  # Spalten: Ort, Region, Umsatz
print(f"{len(sales)} Orte, Gesamtumsatz {sales['Umsatz'].sum()} Euro")

# 1. Top 3 Orte
print("\nTop 3 Orte:")
print(sales.sort_values("Umsatz", ascending=False).head(3))

# 2. Filter mit zwei Bedingungen: & = und (Klammern um jede Bedingung)
print("\nSüd mit mehr als 50 000 Euro:")
print(sales[(sales["Region"] == "Süd") & (sales["Umsatz"] > 50000)])

# 3. groupby: Zeilen nach Region bündeln, dann je Gruppe rechnen
groups = sales.groupby("Region")
print("\nUmsatz-Summe pro Region:")
print(groups["Umsatz"].sum().sort_values(ascending=False))

# 4. agg: mehrere Kennzahlen auf einmal
print("\nKennzahlen pro Region:")
print(groups["Umsatz"].agg(["count", "sum", "mean", "median"]).round())
