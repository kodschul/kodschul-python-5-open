# Zahlenraten – Stand Lab 3.4: mehrere Runden, Versuchszähler

import random

MAX_TRIES = 3  # Großbuchstaben: Wert ändert sich im Programm nicht

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()

play_again = "j"
while play_again == "j":  # äußere Schleife: eine Runde pro Durchlauf
    secret = random.randint(1, 10)
    tries = 0
    print(f"\nNeue Runde, {name}! Rate eine Zahl zwischen 1 und 10.")

    while tries < MAX_TRIES:  # innere Schleife: ein Tipp pro Durchlauf
        guess = int(input("Tipp: "))
        tries += 1

        if guess == secret:
            print(f"Richtig, {name}! Benötigte Versuche: {tries}.")
            break
        elif guess > secret:
            print("Zu hoch.")
        else:
            print("Zu niedrig.")

        if tries < MAX_TRIES:
            print(f"Verbleibende Versuche: {MAX_TRIES - tries}")
        else:
            print(f"Keine Versuche mehr. Die Zahl war {secret}.")

    play_again = input("Nochmal spielen? (j/n): ").strip().lower()

print(f"Danke fürs Spielen, {name}!")
