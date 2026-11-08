# Zahlenraten – Stand Lab 4.2: Bereich als Tupel, doppelte Tipps per Set

import random

MAX_TRIES = 3
NUMBER_RANGE = (1, 10)  # Tupel: Bereich ändert sich nicht

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()
low, high = NUMBER_RANGE  # Tupel entpacken

play_again = "j"
while play_again == "j":
    secret = random.randint(low, high)
    tries = 0
    guesses = []    # Reihenfolge der Tipps für die Ausgabe
    tried = set()   # schnelle Prüfung: schon getippt?
    print(f"\nNeue Runde, {name}! Rate eine Zahl zwischen {low} und {high}.")

    while tries < MAX_TRIES:
        guess = int(input("Tipp: "))

        if guess in tried:
            print("Diese Zahl wurde schon getippt.")
            continue  # kein Versuch abziehen, gleich neu fragen

        tried.add(guess)
        guesses.append(guess)
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

    print("Bisherige Tipps:", guesses)
    play_again = input("Nochmal spielen? (j/n): ").strip().lower()

print(f"Danke fürs Spielen, {name}!")
