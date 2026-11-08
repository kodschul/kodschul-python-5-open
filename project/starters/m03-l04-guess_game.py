# Zahlenraten – Starter für Lab 3.4 (Stand nach Lab 3.3)

import random

secret = random.randint(1, 10)
# TODO Lab 3.4: Konstante MAX_TRIES = 3 anlegen und Versuche mit tries hochzählen statt herunter
tries_left = 3

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()
print(f"Hallo {name}! Rate eine Zahl zwischen 1 und 10.")

# TODO Lab 3.4: äußere Schleife „Nochmal spielen? (j/n)“ um die Runde legen, Geheimzahl je Runde neu ziehen
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
