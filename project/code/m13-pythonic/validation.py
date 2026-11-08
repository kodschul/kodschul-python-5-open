# Dann mit Decorator: die Prüfung steht einmal, @positive_lengths legt sie um alle

import functools


def positive_lengths(func):
    """Decorator: prüft vor dem Aufruf, dass alle Argumente positiv sind."""

    @functools.wraps(func)  # Name und Docstring von func bleiben erhalten
    def wrapper(*args):
        for value in args:  # args: Tupel mit allen Argumenten des Aufrufs
            if value <= 0:
                raise ValueError(f"{value} ist keine positive Länge.")
        return func(*args)  # Tupel wieder auspacken: func(3, 5)

    return wrapper


@positive_lengths
def square_area(side):
    """Fläche eines Quadrats."""
    return side * side


@positive_lengths
def rectangle_area(width, height):
    """Fläche eines Rechtecks."""
    return width * height


@positive_lengths
def triangle_area(base, height):
    """Fläche eines Dreiecks."""
    return base * height / 2


print("Quadrat:", square_area(4))
print("Rechteck:", rectangle_area(3, 5))
print("Dreieck:", triangle_area(6, 2))
try:
    rectangle_area(3, -5)
except ValueError as error:
    print("Fehler:", error)
print("Name der Funktion:", rectangle_area.__name__)  # dank wraps: rectangle_area
