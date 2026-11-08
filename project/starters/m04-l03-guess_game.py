# Zahlenraten – Starter für Lab 4.3 (Stand nach Lab 4.2)

import random

# TODO Lab 4.3: MAX_TRIES, NUMBER_RANGE und das Entpacken darunter durch ein Dictionary LEVELS ersetzen
MAX_TRIES = 3
NUMBER_RANGE = (1, 10)  # Tupel: Bereich ändert sich nicht

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()
low, high = NUMBER_RANGE  # Tupel entpacken

play_again = "j"
while play_again == "j":
    # TODO Lab 4.3: Stufe abfragen, unbekannte Stufe erneut abfragen, Werte aus LEVELS entpacken
    secret = random.randint(low, high)
    tries = 0
    guesses = []    # Reihenfolge der Tipps für die Ausgabe
    tried = set()   # schnelle Prüfung: schon getippt?
    print(f"\nNeue Runde, {name}! Rate eine Zahl zwischen {low} und {high}.")

    # TODO Lab 4.3: hier und unten max_tries der gewählten Stufe statt MAX_TRIES verwenden
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
