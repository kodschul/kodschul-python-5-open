# XML schreiben und lesen mit xml.etree.ElementTree (Standardbibliothek)
# Start im Ordner project/: python code/m17-data-formats/xml_basics.py

import xml.etree.ElementTree as ET
from pathlib import Path

XML_FILE = Path("playground") / "shopping_list.xml"

# 1. Schreiben: einen Baum aus Elementen bauen
root = ET.Element("shopping_list", owner="Anna")  # Wurzel mit Attribut owner
for name, amount in [("Orangen", 7), ("Mangos", 6), ("Milch", 3)]:
    item = ET.SubElement(root, "item", name=name)  # neues Kind von root
    amount_element = ET.SubElement(item, "amount")  # Kind von item
    amount_element.text = str(amount)  # Text zwischen <amount> und </amount>
ET.indent(root)  # Einrückung, damit Menschen den Baum sehen
ET.ElementTree(root).write(XML_FILE, encoding="utf-8", xml_declaration=True)
print(f"Geschrieben: {XML_FILE}")
with open(XML_FILE, encoding="utf-8") as file:
    print(file.read())

# 2. Lesen: Datei -> Baum -> Wurzel
tree = ET.parse(XML_FILE)
root = tree.getroot()
print("Wurzel:", root.tag, "· Attribute:", root.attrib)

first = root.find("item")  # find: das erste passende Kind
print("Erster Artikel:", first.get("name"))  # get: Wert eines Attributs

for item in root.findall("item"):  # findall: alle passenden Kinder als Liste
    amount = int(item.find("amount").text)  # .text ist immer ein String
    print(f"- {item.get('name')}: {amount} Stück")

# iter: alle Elemente mit diesem Namen im ganzen Baum, egal wie tief
total = sum(int(element.text) for element in root.iter("amount"))
print("Stück insgesamt:", total)
