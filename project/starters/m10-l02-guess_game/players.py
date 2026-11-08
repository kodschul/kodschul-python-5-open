# Zahlenraten – Starter für Lab 10.2 (Stand nach Lab 10.1)
# Spieler: wer den nächsten Tipp liefert

from guess_game import ui


class Player:
    """Basisklasse für alle Spieler: hat einen Namen und liefert Tipps."""

    def __init__(self, name):
        self.name = name

    # TODO Lab 10.2: low/high, start_round(low, high), on_hint(guess, hint)
    def next_guess(self):
        """Gibt den nächsten Tipp zurück; jede Unterklasse legt fest, wie."""
        raise NotImplementedError("Diese Methode muss eine Unterklasse festlegen.")


class HumanPlayer(Player):
    """Ein Mensch, der seine Tipps im Terminal eingibt."""

    def next_guess(self):
        """Fragt den Tipp per input ab (überschreibt Player.next_guess)."""
        return ui.ask_number("Tipp: ")


# TODO Lab 10.2: class ComputerPlayer(Player) mit Intervallhalbierung
