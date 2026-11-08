# Fehlersuche-Datei (Lab 3.4): Zahlenraten mit genau einem Fehler.
# Symptom: Die Versuche zählen nicht bei jedem Tipp herunter.
# Der Code läuft ohne Fehlermeldung; der Fehler steckt in einer Einrückung.

import random

secret = random.randint(1, 10)
tries = 3

print("Rate eine Zahl zwischen 1 und 10. Es gibt 3 Versuche.")

while tries > 0:
    guess = int(input("Tipp: "))

    if guess == secret:
        print("Richtig!")
        break
    elif guess > secret:
        print("Zu hoch.")
    else:
        print("Zu niedrig.")
        tries -= 1

    if tries > 0:
        print(f"Verbleibende Versuche: {tries}")
    else:
        print(f"Keine Versuche mehr. Die Zahl war {secret}.")
