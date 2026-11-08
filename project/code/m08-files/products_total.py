# Gesamtwert aller Produkte aus data/products.csv berechnen

import csv
from pathlib import Path

products_file = Path("data") / "products.csv"

total = 0
with open(products_file, encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)  # erste Zeile = Spaltennamen
    for row in reader:  # jede Zeile ist ein Dictionary
        price = float(row["price"])  # alle Werte kommen als Text
        qty = int(row["qty"])
        value = round(price * qty, 2)
        print(f"{row['name']}: {qty} × {price} = {value}")
        total += value

print("Gesamtwert:", round(total, 2))
