# Zahlenraten – Starter für Lab 3.3 (Stand nach Lab 3.2)

import random  # Werkzeug aus der Standardbibliothek

secret = random.randint(1, 10)  # 1 und 10 sind beide möglich
# TODO Lab 3.3: Variable tries_left = 3 anlegen

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()
print(f"Hallo {name}! Rate eine Zahl zwischen 1 und 10.")

# TODO Lab 3.3: Tipp und Bewertung in eine while-Schleife mit drei Versuchen setzen, bei Treffer abbrechen
guess = int(input("Tipp: "))

if guess > secret:
    print("Zu hoch.")
elif guess < secret:
    print("Zu niedrig.")
else:
    print(f"Richtig, {name}!")
