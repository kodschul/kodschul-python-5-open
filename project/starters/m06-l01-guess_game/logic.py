# Spielregeln: Stufen, Geheimzahl, Prüfungen – ohne Ein- und Ausgabe

import random

# TODO Lab 6.1: LEVELS, is_guess_correct und is_game_over aus der alten Datei hierher


def draw_secret(low, high):
    """Gibt eine zufällige Geheimzahl zwischen low und high zurück."""
    return random.randint(low, high)
