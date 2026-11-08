# Zahlenraten – Starter für Lab 7.3 (Stand nach Lab 7.2)
# Spielregeln: Stufen, Geheimzahl, Prüfungen – ohne Ein- und Ausgabe

import random

# Stufe -> (kleinste Zahl, größte Zahl, Versuche)
LEVELS = {
    "leicht": (1, 10, 5),
    "mittel": (1, 50, 7),
    "schwer": (1, 100, 7),
}


def draw_secret(low, high):
    """Gibt eine zufällige Geheimzahl zwischen low und high zurück."""
    return random.randint(low, high)


# TODO Lab 7.3: Funktion check_guess(guess, low, high) hier ergänzen


def is_guess_correct(guess, secret):
    """Gibt True zurück, wenn der Tipp die Geheimzahl trifft."""
    return guess == secret


def is_game_over(tries, max_tries):
    """Gibt True zurück, wenn alle Versuche verbraucht sind."""
    return tries >= max_tries
