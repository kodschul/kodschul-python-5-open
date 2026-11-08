# Telefonbuch: Dictionary mit Name -> Nummer

phone_book = {
    "Anna": "0151 1234567",
    "Ben": "0160 7654321",
}

# Lesen per Schlüssel
print("Anna:", phone_book["Anna"])

# get: Standardwert, wenn der Schlüssel fehlt (kein Absturz)
print("Cem:", phone_book.get("Cem", "nicht eingetragen"))

# Eintragen und ändern: gleiche Schreibweise
phone_book["Cem"] = "0170 1112223"   # neuer Schlüssel: wird angelegt
phone_book["Ben"] = "0160 9998887"   # vorhandener Schlüssel: wird ersetzt

# Löschen
del phone_book["Anna"]
print("Einträge:", len(phone_book))
print("Ist Anna noch drin?", "Anna" in phone_book)

# Alle Paare durchlaufen
for name, number in phone_book.items():
    print(f"{name}: {number}")

print("Namen:", list(phone_book.keys()))
print("Nummern:", list(phone_book.values()))

# Verschachtelt: Liste von Dictionaries (eine Zeile pro Kontakt)
contacts = [
    {"name": "Dana", "city": "Köln", "number": "0171 5550001"},
    {"name": "Eva", "city": "Leipzig", "number": "0172 5550002"},
]
for contact in contacts:
    print(f"{contact['name']} aus {contact['city']}: {contact['number']}")
