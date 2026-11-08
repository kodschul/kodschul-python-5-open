# Zahlenraten – Starter für Lab 13.3 (Stand nach Lab 13.2)
# Spieler: wer den nächsten Tipp liefert

from abc import ABC, abstractmethod

from guess_game import ui


class Player(ABC):
    """Abstrakte Basisklasse: Vertrag, den jeder Spielertyp erfüllen muss."""

    def __init__(self, name):
        self.name = name
        self.low = 0  # Zahlenbereich der aktuellen Runde, setzt start_round
        self.high = 0

    def start_round(self, low, high):
        """Merkt sich zu Beginn jeder Runde den Zahlenbereich."""
        self.low = low
        self.high = high

    @abstractmethod
    def next_guess(self):
        """Gibt den nächsten Tipp zurück; jede Unterklasse muss das festlegen."""

    @abstractmethod
    def on_hint(self, guess, hint):
        """Reagiert auf den Hinweis zum letzten Tipp; Pflicht für jede Unterklasse."""


class HumanPlayer(Player):
    """Ein Mensch, der seine Tipps im Terminal eingibt."""

    def next_guess(self):
        """Fragt den Tipp per input ab (überschreibt Player.next_guess)."""
        # TODO Lab 13.3: Text liefern: ui.ask_command("Tipp: ")
        return ui.ask_number("Tipp: ")

    def on_hint(self, guess, hint):
        """Ein Mensch liest den Hinweis selbst im Terminal: nichts zu tun."""
        pass


class ComputerPlayer(Player):
    """Der Computer rät per Intervallhalbierung: immer die Mitte des Bereichs."""

    def __init__(self):
        super().__init__("Computer")  # fester Name, Rest erledigt die Basisklasse

    def next_guess(self):
        """Tippt die Mitte des Bereichs und zeigt den Tipp an."""
        guess = (self.low + self.high) // 2
        ui.show_guess(guess)
        # TODO Lab 13.3: als Text zurückgeben: str(guess)
        return guess

    def on_hint(self, guess, hint):
        """Halbiert den Bereich: zu hoch -> untere Hälfte, zu niedrig -> obere."""
        # self.low und self.high: Bereich, in dem die Zahl noch liegen kann
        if hint == "zu hoch":
            self.high = guess - 1
        elif hint == "zu niedrig":
            self.low = guess + 1
