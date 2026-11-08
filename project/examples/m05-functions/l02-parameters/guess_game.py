# Zahlenraten – Stand Lab 5.2: eine Runde als Funktion mit Rückgabewert

import random

# Stufe -> (kleinste Zahl, größte Zahl, Versuche)
LEVELS = {
    "leicht": (1, 10, 5),
    "mittel": (1, 50, 7),
    "schwer": (1, 100, 7),
}


def is_guess_correct(guess, secret):
    """Gibt True zurück, wenn der Tipp die Geheimzahl trifft."""
    return guess == secret


def show_hint(guess, secret):
    """Gibt aus, ob der Tipp zu hoch oder zu niedrig ist."""
    if guess > secret:
        print("Zu hoch.")
    else:
        print("Zu niedrig.")
    # kein return: Prozedur, Ergebnis ist None


def is_game_over(tries, max_tries):
    """Gibt True zurück, wenn alle Versuche verbraucht sind."""
    return tries >= max_tries


def ask_level():
    """Fragt so lange nach der Stufe, bis es sie gibt, und gibt sie zurück."""
    level = input("Stufe (leicht/mittel/schwer): ").strip().lower()
    while level not in LEVELS:
        print("Diese Stufe gibt es nicht.")
        level = input("Stufe (leicht/mittel/schwer): ").strip().lower()
    return level


def play_round(level="leicht"):
    """Spielt eine Runde und gibt die Anzahl der Versuche zurück."""
    low, high, max_tries = LEVELS[level]
    secret = random.randint(low, high)
    tries = 0
    guesses = []
    tried = set()
    # name kommt von außerhalb der Funktion (Umbau in Lab 5.3)
    print(f"\nStufe {level}, {name}: Rate eine Zahl zwischen {low} und {high}.")

    while not is_game_over(tries, max_tries):
        guess = int(input("Tipp: "))

        if guess in tried:
            print("Diese Zahl wurde schon getippt.")
            continue

        tried.add(guess)
        guesses.append(guess)
        tries += 1

        if is_guess_correct(guess, secret):
            print(f"Richtig, {name}! Benötigte Versuche: {tries}.")
            break

        show_hint(guess, secret)

        if is_game_over(tries, max_tries):
            print(f"Keine Versuche mehr. Die Zahl war {secret}.")
        else:
            print(f"Verbleibende Versuche: {max_tries - tries}")

    print("Bisherige Tipps:", guesses)
    return tries


def main():
    """Hauptablauf: Runden spielen, bis niemand mehr will."""
    all_tries = []  # Versuche jeder Runde
    play_again = "j"
    while play_again == "j":
        level = ask_level()
        tries = play_round(level=level)  # Schlüsselwortargument
        all_tries.append(tries)
        play_again = input("Nochmal spielen? (j/n): ").strip().lower()

    print("Versuche pro Runde:", all_tries)
    print(f"Danke fürs Spielen, {name}!")


print("=" * 40)
print("Zahlenraten")
print("=" * 40)

# globale Variable: play_round und main lesen sie von außen
name = input("Name: ").strip().title()
main()
