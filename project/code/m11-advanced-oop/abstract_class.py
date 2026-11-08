# Abstrakte Klasse: Shape legt fest, was jede Form können muss

import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstrakte Basisklasse: Vertrag für alle Formen, selbst nicht erzeugbar."""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        """Fläche berechnen: jede Unterklasse muss das festlegen."""

    def describe(self):
        """Fertige Methode, die alle Formen erben; nutzt area() der Unterklasse."""
        return f"{self.name}: Fläche {self.area():.1f}"


class Circle(Shape):
    """Kreis: erfüllt den Vertrag mit einer eigenen area()."""

    def __init__(self, radius):
        super().__init__("Kreis")
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2


class Rectangle(Shape):
    """Rechteck: erfüllt den Vertrag ebenfalls."""

    def __init__(self, width, height):
        super().__init__("Rechteck")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    """Unvollständig: area() fehlt, daher lässt sich kein Dreieck erzeugen."""


shapes = [Circle(2), Rectangle(3, 4)]
for shape in shapes:
    print(shape.describe())  # jede Form rechnet ihre Fläche selbst

try:
    Shape("Form")  # abstrakte Klasse direkt erzeugen
except TypeError as error:
    print("TypeError:", error)

try:
    Triangle("Dreieck")  # Unterklasse ohne area()
except TypeError as error:
    print("TypeError:", error)
