# Zahlenraten – Stand Lab 4.3 (Spiel v1): drei Schwierigkeitsstufen

import random

# Stufe -> (kleinste Zahl, größte Zahl, Versuche)
LEVELS = {
    "leicht": (1, 10, 5),
    "mittel": (1, 50, 7),
    "schwer": (1, 100, 7),
}

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()

play_again = "j"
while play_again == "j":
    level = input("Stufe (leicht/mittel/schwer): ").strip().lower()
    while level not in LEVELS:  # unbekannte Stufe: erneut fragen
        print("Diese Stufe gibt es nicht.")
        level = input("Stufe (leicht/mittel/schwer): ").strip().lower()

    low, high, max_tries = LEVELS[level]  # Tupel aus dem Dictionary entpacken
    secret = random.randint(low, high)
    tries = 0
    guesses = []
    tried = set()
    print(f"\nStufe {level}, {name}: Rate eine Zahl zwischen {low} und {high}.")

    while tries < max_tries:
        guess = int(input("Tipp: "))

        if guess in tried:
            print("Diese Zahl wurde schon getippt.")
            continue

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

        if tries < max_tries:
            print(f"Verbleibende Versuche: {max_tries - tries}")
        else:
            print(f"Keine Versuche mehr. Die Zahl war {secret}.")

    print("Bisherige Tipps:", guesses)
    play_again = input("Nochmal spielen? (j/n): ").strip().lower()

print(f"Danke fürs Spielen, {name}!")
