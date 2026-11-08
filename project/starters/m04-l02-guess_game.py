# Zahlenraten – Starter für Lab 4.2 (Stand nach Lab 4.1)

import random

MAX_TRIES = 3
# TODO Lab 4.2: Zahlenbereich als Tupel festlegen und in low, high entpacken

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()

play_again = "j"
while play_again == "j":
    # TODO Lab 4.2: Bereich aus dem Tupel statt 1 und 10 verwenden
    secret = random.randint(1, 10)
    tries = 0
    guesses = []  # leere Liste: noch kein Tipp
    # TODO Lab 4.2: leeres Set für schon getippte Zahlen anlegen
    print(f"\nNeue Runde, {name}! Rate eine Zahl zwischen 1 und 10.")

    while tries < MAX_TRIES:
        guess = int(input("Tipp: "))
        # TODO Lab 4.2: schon getippte Zahl melden und ohne Versuch neu fragen, sonst im Set merken
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
