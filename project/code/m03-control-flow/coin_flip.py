# Münzwurf: random.choice wählt ein zufälliges Zeichen aus einem String

import random

side = random.choice("KZ")  # "K" für Kopf oder "Z" für Zahl
call = input("Kopf oder Zahl? (k/z): ").strip().upper()

name = "Kopf" if side == "K" else "Zahl"  # Bedingungsausdruck aus Lab 3.1
print(f"Die Münze zeigt: {name}")

if call == side:
    print("Richtig getippt!")
else:
    print("Leider falsch.")
