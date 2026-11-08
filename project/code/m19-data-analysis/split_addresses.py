# Adressblöcke aus einem Textexport zerlegen: ein Datensatz geht über mehrere Zeilen
# Start im Ordner project/: python code/m19-data-analysis/split_addresses.py

import re
from pathlib import Path

TEXT = Path("data/addresses.txt").read_text(encoding="utf-8")  # ganze Datei, ein Text

# 1. ^ ohne und mit re.MULTILINE
LINE = r"^Name: (.+)$"
print("Ohne MULTILINE:", re.findall(LINE, TEXT))  # ^ nur am Textanfang
print("Mit MULTILINE: ", re.findall(LINE, TEXT, re.MULTILINE))  # ^ an jeder Zeile

# 2. Block bis zur Leerzeile mit re.DOTALL (. passt dann auch auf \n)
greedy = re.findall(r"^Name: .*\n\n", TEXT, re.MULTILINE | re.DOTALL)
lazy = re.findall(r"^Name: .*?\n\n", TEXT, re.MULTILINE | re.DOTALL)
lazy_end = re.findall(r"^Name: .*?(?:\n\n|\Z)", TEXT, re.MULTILINE | re.DOTALL)
print("\ngierig .*         :", len(greedy), "Treffer")  # bis zur letzten Leerzeile
print("nicht gierig .*?  :", len(lazy), "Treffer")  # letzter Block fehlt
print("mit Textende \\Z   :", len(lazy_end), "Treffer")

# 3. Feste Zeilenfolge mit benannten Gruppen, Telefon-Zeile optional
ADDRESS_PATTERN = re.compile(
    r"""
    ^Name:\ (?P<name>.+)\n               # .+ bleibt in einer Zeile
    Straße:\ (?P<street>.+)\n
    Ort:\ (?P<zip>\d{5})\ (?P<city>.+)$
    (?:\nTelefon:\ (?P<phone>.+))?       # (?:...)? = ganze Zeile optional
    """,
    re.MULTILINE | re.VERBOSE,  # VERBOSE: Leerzeichen als "\ ", Kommentare mit #
)

addresses = []
for match in ADDRESS_PATTERN.finditer(TEXT):  # ein Treffer pro Block
    addresses.append(match.groupdict())  # Dictionary mit allen benannten Gruppen

print(f"\n{len(addresses)} Adressen:")
for address in addresses:
    phone = address["phone"] if address["phone"] is not None else "–"
    print(f"  {address['name']}, {address['zip']} {address['city']}, Tel. {phone}")
print("\nErster Datensatz:", addresses[0])
