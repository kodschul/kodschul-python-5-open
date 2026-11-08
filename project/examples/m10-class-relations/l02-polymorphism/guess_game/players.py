# Spieler: wer den nächsten Tipp liefert

from guess_game import ui


class Player:
    """Basisklasse für alle Spieler: hat einen Namen und liefert Tipps."""

    def __init__(self, name):
        self.name = name
        self.low = 0  # Zahlenbereich der aktuellen Runde, setzt start_round
        self.high = 0

    def start_round(self, low, high):
        """Merkt sich zu Beginn jeder Runde den Zahlenbereich."""
        self.low = low
        self.high = high

    def next_guess(self):
        """Gibt den nächsten Tipp zurück; jede Unterklasse legt fest, wie."""
        raise NotImplementedError("Diese Methode muss eine Unterklasse festlegen.")

    def on_hint(self, guess, hint):
        """Bekommt den Hinweis zum letzten Tipp; Standard: nichts tun."""
        pass


class HumanPlayer(Player):
    """Ein Mensch, der seine Tipps im Terminal eingibt."""

    def next_guess(self):
        """Fragt den Tipp per input ab (überschreibt Player.next_guess)."""
        return ui.ask_number("Tipp: ")


class ComputerPlayer(Player):
    """Der Computer rät per Intervallhalbierung: immer die Mitte des Bereichs."""

    def __init__(self):
        super().__init__("Computer")  # fester Name, Rest erledigt die Basisklasse

    def next_guess(self):
        """Tippt die Mitte des Bereichs und zeigt den Tipp an."""
        guess = (self.low + self.high) // 2
        ui.show_guess(guess)
        return guess

    def on_hint(self, guess, hint):
        """Halbiert den Bereich: zu hoch -> untere Hälfte, zu niedrig -> obere."""
        # self.low und self.high: Bereich, in dem die Zahl noch liegen kann
        if hint == "zu hoch":
            self.high = guess - 1
        elif hint == "zu niedrig":
            self.low = guess + 1
