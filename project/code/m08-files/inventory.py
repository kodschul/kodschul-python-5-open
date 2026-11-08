# CSV aus deutschem Excel: Semikolon, Dezimalkomma, UTF-8 mit BOM

import csv
from pathlib import Path

INVENTORY_FILE = Path("data") / "inventory.csv"
PRICE_FILE = Path("playground") / "price_list.csv"
VAT = 1.19  # 19 % Mehrwertsteuer


def to_number(text):
    """Wandelt deutschen Zahlentext wie "1299,99" in eine Kommazahl um."""
    return float(text.replace(",", "."))


def to_text(number):
    """Wandelt eine Kommazahl in deutschen Zahlentext mit zwei Stellen um."""
    return f"{number:.2f}".replace(".", ",")  # :.2f = zwei Nachkommastellen


# lesen: utf-8-sig überspringt die BOM-Markierung, die Excel an den Anfang setzt
with open(INVENTORY_FILE, encoding="utf-8-sig", newline="") as file:
    products = list(csv.DictReader(file, delimiter=";"))

print(f"{len(products)} Produkte gelesen. Erste Zeile:")
print(products[0])

# schreiben: Spaltennamen festlegen, Kopfzeile und Zeilen als Dictionaries
with open(PRICE_FILE, "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Produkt", "Brutto"], delimiter=";")
    writer.writeheader()
    for product in products:
        gross = to_number(product["Preis"]) * VAT
        writer.writerow({"Produkt": product["Produkt"], "Brutto": to_text(gross)})

print("Preisliste gespeichert in", PRICE_FILE)
print(PRICE_FILE.read_text(encoding="utf-8-sig"))
