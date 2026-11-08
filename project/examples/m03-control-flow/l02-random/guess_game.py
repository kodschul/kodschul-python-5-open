# Zahlenraten – Stand Lab 3.2: Geheimzahl per Zufall

import random  # Werkzeug aus der Standardbibliothek

secret = random.randint(1, 10)  # 1 und 10 sind beide möglich

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()
print(f"Hallo {name}! Rate eine Zahl zwischen 1 und 10.")

guess = int(input("Tipp: "))

if guess > secret:
    print("Zu hoch.")
elif guess < secret:
    print("Zu niedrig.")
else:
    print(f"Richtig, {name}!")
