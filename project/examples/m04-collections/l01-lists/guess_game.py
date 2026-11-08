# Zahlenraten – Stand Lab 4.1: alle Tipps einer Runde in einer Liste

import random

MAX_TRIES = 3

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()

play_again = "j"
while play_again == "j":
    secret = random.randint(1, 10)
    tries = 0
    guesses = []  # leere Liste: noch kein Tipp
    print(f"\nNeue Runde, {name}! Rate eine Zahl zwischen 1 und 10.")

    while tries < MAX_TRIES:
        guess = int(input("Tipp: "))
        tries += 1
        guesses.append(guess)  # Tipp hinten anhängen

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

    print("Bisherige Tipps:", guesses)
    play_again = input("Nochmal spielen? (j/n): ").strip().lower()

print(f"Danke fürs Spielen, {name}!")
