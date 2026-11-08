# Zahlenraten – Starter für Lab 9.2 (Stand nach Lab 8.3)
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


def check_guess(guess, low, high):
    """Löst ValueError aus, wenn der Tipp nicht zwischen low und high liegt."""
    if guess < low or guess > high:
        raise ValueError(f"Der Tipp muss zwischen {low} und {high} liegen.")


# TODO Lab 9.2: is_guess_correct und is_game_over werden Methoden der Klasse Game
def is_guess_correct(guess, secret):
    """Gibt True zurück, wenn der Tipp die Geheimzahl trifft."""
    return guess == secret


def is_game_over(tries, max_tries):
    """Gibt True zurück, wenn alle Versuche verbraucht sind."""
    return tries >= max_tries


# TODO Lab 9.2: class Game mit __init__, guess(number), is_over() und result()
