# Prozentrechnung; nutzt ein anderes Modul desselben Pakets

from helpers import calculator


def percent_of(base, percent):
    """Gibt percent Prozent von base zurück."""
    return calculator.divide(calculator.multiply(base, percent), 100)
