# Spielregeln und Spieldaten: Stufen, Game, Score – ohne Ein- und Ausgabe

import functools
import random
import time
from dataclasses import dataclass
from datetime import datetime

# Stufe -> (kleinste Zahl, größte Zahl, Versuche)
LEVELS = {
    "leicht": (1, 10, 5),
    "mittel": (1, 50, 7),
    "schwer": (1, 100, 7),
}

# Stufe -> Funktion, die aus den Versuchen Punkte macht (Funktionen als Werte)
# weniger Versuche und schwerere Stufe = mehr Punkte
LEVEL_POINTS = {
    "leicht": lambda tries: (6 - tries) * 10,
    "mittel": lambda tries: (8 - tries) * 20,
    "schwer": lambda tries: (8 - tries) * 30,
}


def timed(func):
    """Decorator: misst die Laufzeit von func und trägt sie ins Ergebnis ein."""

    @functools.wraps(func)  # Name und Docstring von func bleiben erhalten
    def wrapper(*args, **kwargs):
        start = time.perf_counter()  # Stoppuhr starten
        result = func(*args, **kwargs)  # die eigentliche Funktion aufrufen
        result.seconds = round(time.perf_counter() - start, 1)
        return result

    return wrapper


def draw_secret(low, high):
    """Gibt eine zufällige Geheimzahl zwischen low und high zurück."""
    return random.randint(low, high)


class InvalidGuessError(ValueError):
    """Spielfehler: Der Tipp verletzt eine Regel, z. B. außerhalb des Bereichs."""


def check_guess(guess, low, high):
    """Löst InvalidGuessError aus, wenn der Tipp nicht zwischen low und high liegt."""
    if guess < low or guess > high:
        raise InvalidGuessError(f"Der Tipp muss zwischen {low} und {high} liegen.")


@dataclass  # erzeugt __init__, __repr__ und __eq__ aus den Feldern
class Score:
    """Ergebnis eines Spiels, das sich lesbar ausgeben und sortieren lässt."""

    # Feld: Typ (bei Dataclasses Pflicht, Python prüft ihn nicht)
    name: str
    level: str
    tries: int
    seconds: float
    won: bool
    date: str

    def __str__(self):
        """Text für print() und f-Strings: Anna – 3 Versuche – 12,4 s."""
        word = "Versuch" if self.tries == 1 else "Versuche"
        seconds = f"{self.seconds:.1f}".replace(".", ",")
        return f"{self.name} – {self.tries} {word} – {seconds} s"

    def points(self):
        """Berechnet die Punkte mit der Funktion, die zur Stufe gehört."""
        calculate = LEVEL_POINTS[self.level]  # eine Funktion aus dem Dictionary
        return calculate(self.tries)

    def __lt__(self, other):
        """Kleiner = besser: weniger Versuche, bei Gleichstand weniger Zeit."""
        if self.tries != other.tries:
            return self.tries < other.tries
        return self.seconds < other.seconds


class Game:
    """Ein Spiel: hat einen Spieler, eine Bestenliste, Geheimzahl und Tipps."""

    def __init__(self, player, scoreboard, level="leicht"):
        self.player = player  # Komposition: Game hat einen Player ...
        self.scoreboard = scoreboard  # ... und ein Scoreboard
        self.level = level
        self.low, self.high, self._max_tries = LEVELS[level]
        self.__secret = draw_secret(self.low, self.high)  # privat: nur in Game
        self.guesses = []
        self.started = datetime.now()  # Datum und Uhrzeit des Starts

    @property
    def attempts_left(self):
        """Verbleibende Versuche, nur lesbar und immer aus den Tipps berechnet."""
        return self._max_tries - len(self.guesses)

    @property
    def is_won(self):
        """True, wenn die Geheimzahl unter den Tipps ist."""
        return self.__secret in self.guesses

    def guess(self, number):
        """Wertet einen Tipp aus und gibt den Hinweis als Text zurück."""
        check_guess(number, self.low, self.high)  # löst InvalidGuessError aus
        if number in self.guesses:
            return "schon getippt"  # kostet keinen Versuch
        self.guesses.append(number)
        if self.is_won:
            return "richtig"
        if number > self.__secret:
            return "zu hoch"
        return "zu niedrig"

    def is_over(self):
        """Gibt True zurück, wenn gewonnen oder alle Versuche verbraucht sind."""
        return self.is_won or self.attempts_left == 0

    def reveal_secret(self):
        """Verrät die Geheimzahl, aber erst, wenn das Spiel vorbei ist."""
        if self.is_over():
            return self.__secret
        return None

    def save_score(self, score):
        """Trägt score in die Bestenliste ein, aber nur bei einem Gewinn."""
        if self.is_won:
            self.scoreboard.add(score)  # Dateizugriff erledigt Scoreboard

    def score(self):
        """Gibt das Ergebnis als Score zurück; die Dauer trägt @timed ein."""
        return Score(
            self.player.name,
            self.level,
            len(self.guesses),
            0.0,  # Dauer: misst der Decorator @timed um play_round
            self.is_won,
            self.started.strftime("%Y-%m-%d"),
        )


def average(numbers):
    """Gibt den Durchschnitt einer Zahlenliste mit einer Nachkommastelle zurück."""
    return round(sum(numbers) / len(numbers), 1)


def statistics(scores):
    """Wertet eine Liste von Scores aus: Gewinner, Versuche, Schnitt pro Stufe."""
    # Set-Comprehension: jeder Name nur einmal
    winners = {score.name for score in scores}
    # Dict-Comprehension mit Listen-Comprehension als Wert
    tries_per_player = {
        name: [score.tries for score in scores if score.name == name]
        for name in winners
    }
    levels = {score.level for score in scores}  # gespielte Stufen
    average_per_level = {
        level: average([score.tries for score in scores if score.level == level])
        for level in levels
    }
    return {
        "winners": winners,
        "tries_per_player": tries_per_player,
        "average_per_level": average_per_level,
    }
