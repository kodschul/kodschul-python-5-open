# Zahlenraten – Stand Lab 3.3: drei Versuche in einer while-Schleife

import random

secret = random.randint(1, 10)
tries_left = 3

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()
print(f"Hallo {name}! Rate eine Zahl zwischen 1 und 10.")

while tries_left > 0:
    guess = int(input("Tipp: "))
    tries_left -= 1  # jeder Tipp kostet einen Versuch

    if guess == secret:
        print(f"Richtig, {name}!")
        break  # Treffer: Schleife sofort verlassen
    elif guess > secret:
        print("Zu hoch.")
    else:
        print("Zu niedrig.")

    if tries_left > 0:
        print(f"Verbleibende Versuche: {tries_left}")
    else:
        print(f"Keine Versuche mehr. Die Zahl war {secret}.")
