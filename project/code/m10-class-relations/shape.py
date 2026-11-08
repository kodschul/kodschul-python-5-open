# Formen: Circle und Rectangle erben von Shape und berechnen ihre Fläche (Lab 10.1)

import math


class Shape:
    """Basisklasse für Formen: hat einen Namen und eine Fläche."""

    def __init__(self, name):
        self.name = name

    def area(self):
        """Fläche; jede Unterklasse muss sie selbst berechnen."""
        raise NotImplementedError("Diese Methode muss eine Unterklasse festlegen.")

    def describe(self):
        """Gibt Name und Fläche als Text zurück (gilt für alle Formen)."""
        return f"{self.name}: Fläche {round(self.area(), 2)} cm²"


class Circle(Shape):
    """Kreis mit Radius."""

    def __init__(self, radius):
        super().__init__("Kreis")  # Name setzt die Basisklasse
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2  # π · r²


class Rectangle(Shape):
    """Rechteck mit Breite und Höhe."""

    def __init__(self, width, height):
        super().__init__("Rechteck")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(4)
rectangle = Rectangle(15, 25)

print(circle.describe())  # describe kommt aus Shape, area aus Circle
print(rectangle.describe())
print("Kreis ist eine Form:", isinstance(circle, Shape))
print("Kreis ist ein Rechteck:", isinstance(circle, Rectangle))

shape = Shape("Irgendwas")
try:
    print(shape.describe())
except NotImplementedError as error:  # Shape allein kennt keine Fläche
    print("Fehler:", error)
