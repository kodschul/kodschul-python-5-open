# CSV erst von Hand mit split(",") zerlegen, dann mit dem csv-Modul

import csv
from pathlib import Path

products_file = Path("data") / "products.csv"

print("--- Von Hand mit split(',') ---")
with open(products_file, encoding="utf-8") as file:
    lines = file.readlines()

columns = lines[0].strip().split(",")
print("Spalten:", columns)
for line in lines[1:]:  # ab Zeile 2: die Daten
    values = line.strip().split(",")
    print(len(values), "Werte:", values)  # "Kabel, 2 m" zerfällt in zwei Teile

print("--- Mit csv.reader ---")
with open(products_file, encoding="utf-8", newline="") as file:
    reader = csv.reader(file)  # beachtet Anführungszeichen
    for row in reader:
        print(len(row), "Werte:", row)

print("--- Mit csv.writer ---")
copy_file = Path("playground") / "products_copy.csv"
with open(copy_file, "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "price", "qty"])  # eine Zeile = eine Liste
    writer.writerow(["Kabel, 5 m", 7.99, 1])  # setzt Anführungszeichen selbst
print(copy_file.read_text(encoding="utf-8"))
