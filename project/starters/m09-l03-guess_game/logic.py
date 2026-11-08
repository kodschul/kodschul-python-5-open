# Zahlenraten – Starter für Lab 9.3 (Stand nach Lab 9.2)
# Spielregeln: Stufen, Geheimzahl, Prüfungen und die Klasse Game – ohne Ein- und Ausgabe

import random
import time
from datetime import datetime

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


class Game:
    """Ein Spiel: Geheimzahl, verbleibende Versuche und bisherige Tipps."""

    def __init__(self, name, level="leicht"):
        self.name = name
        self.level = level
        self.low, self.high, self.max_tries = LEVELS[level]
        # TODO Lab 9.3: Geheimzahl privat (__secret), max_tries intern (_max_tries)
        self.secret = draw_secret(self.low, self.high)
        # TODO Lab 9.3: attempts_left und won werden nur lesbare Properties
        self.attempts_left = self.max_tries
        self.guesses = []
        self.won = False
        self.started = datetime.now()  # Datum und Uhrzeit des Starts
        self.start_time = time.perf_counter()  # Stoppuhr starten
        self.seconds = 0.0

    def guess(self, number):
        """Wertet einen Tipp aus und gibt den Hinweis als Text zurück."""
        check_guess(number, self.low, self.high)  # löst ValueError aus
        if number in self.guesses:
            return "schon getippt"  # kostet keinen Versuch
        self.guesses.append(number)
        self.attempts_left -= 1
        if number == self.secret:
            self.won = True
        if self.is_over():  # Stoppuhr anhalten
            self.seconds = round(time.perf_counter() - self.start_time, 1)
        if self.won:
            return "richtig"
        if number > self.secret:
            return "zu hoch"
        return "zu niedrig"

    # TODO Lab 9.3: reveal_secret() verrät die Zahl erst, wenn das Spiel vorbei ist
    def is_over(self):
        """Gibt True zurück, wenn gewonnen oder alle Versuche verbraucht sind."""
        return self.won or self.attempts_left == 0

    def result(self):
        """Gibt das Ergebnis des Spiels als Dictionary zurück."""
        return {
            "name": self.name,
            "level": self.level,
            "tries": len(self.guesses),
            "seconds": self.seconds,
            "won": self.won,
            "date": self.started.strftime("%Y-%m-%d"),
        }
