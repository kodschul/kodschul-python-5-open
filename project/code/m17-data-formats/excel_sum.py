# Excel-Datei lesen, Summen ergänzen und als neue Datei speichern (openpyxl)
# Start im Ordner project/: python code/m17-data-formats/excel_sum.py
# Die Kursdatei data/shopping_items.xlsx bleibt unverändert.

from pathlib import Path

from openpyxl import load_workbook
from openpyxl.styles import Font

SOURCE = Path("data") / "shopping_items.xlsx"  # nur lesen
TARGET = Path("playground") / "shopping_items_sum.xlsx"  # Ergebnis, neue Datei

workbook = load_workbook(SOURCE)  # ganze Arbeitsmappe laden
print("Blätter:", workbook.sheetnames)
sheet = workbook.active  # das aktive (erste) Blatt
print("Bereich mit Daten:", sheet.dimensions)

# Zeilen als Tupel lesen; values_only=True liefert Werte statt Zellen
for row in sheet.iter_rows(values_only=True):
    print(row)

# Zelle über ihren Namen: Spalte als Buchstabe, Zeile als Zahl
print("B2 =", sheet["B2"].value, "· C2 =", sheet["C2"].value)

# Neue Spalte D: Menge × Einzelpreis, als Excel-Formel
sheet["D1"] = "Summe (€)"
sheet["D1"].font = Font(bold=True)
total = 0
last_row = sheet.max_row  # letzte Zeile mit Daten, hier 6
for number in range(2, last_row + 1):
    sheet[f"D{number}"] = f"=B{number}*C{number}"  # Excel rechnet beim Öffnen
    # Python rechnet sofort selbst mit
    total += sheet[f"B{number}"].value * sheet[f"C{number}"].value

# Summenzeile unter der letzten Zeile
sum_row = last_row + 1
sheet[f"A{sum_row}"] = "Gesamt"
sheet[f"D{sum_row}"] = f"=SUM(D2:D{last_row})"
sheet[f"A{sum_row}"].font = Font(bold=True)
sheet[f"D{sum_row}"].font = Font(bold=True)
sheet.column_dimensions["D"].width = 12

workbook.save(TARGET)  # neue Datei, das Original bleibt
print(f"Gespeichert: {TARGET}")
print(f"Gesamt (in Python gerechnet): {total:.2f} €".replace(".", ","))
print(f"In der Zelle D{sum_row} steht:", sheet[f"D{sum_row}"].value)
