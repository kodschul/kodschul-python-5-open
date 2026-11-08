# Inhalt einer Excel-Datei im Terminal zeigen, ohne Excel zu öffnen
# Start im Ordner project/:
# python code/m17-data-formats/excel_peek.py data/shopping_items.xlsx

import argparse
from pathlib import Path

from openpyxl import load_workbook

parser = argparse.ArgumentParser(description="Zeigt die Zellen einer .xlsx-Datei.")
parser.add_argument("path", type=Path, help="Pfad zur .xlsx-Datei")
args = parser.parse_args()

workbook = load_workbook(args.path)
for sheet in workbook.worksheets:  # alle Blätter der Arbeitsmappe
    print(f"Blatt „{sheet.title}“, Bereich {sheet.dimensions}")
    for row in sheet.iter_rows(values_only=True):
        print("  ", row)
    bold = [cell.font.b for cell in sheet[1]]  # Zeile 1: fett?
    print("   Kopfzeile fett:", bold)
    widths = {key: value.width for key, value in sheet.column_dimensions.items()}
    print("   Spaltenbreiten:", widths)
