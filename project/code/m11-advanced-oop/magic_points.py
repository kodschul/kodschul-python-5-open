# Point mit Magic Methods: +, ==, < und sorted() funktionieren wie bei Zahlen


class Point:
    """Ein Punkt im Koordinatensystem, z. B. Point(2, 3)."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Text für print(): (2, 3)."""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Text für REPL und Listen: Point(2, 3)."""
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        """a + b: x und y einzeln addieren, ergibt einen neuen Punkt."""
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        """a == b: gleich, wenn x und y gleich sind."""
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        """a < b: näher am Nullpunkt (0, 0) ist kleiner."""
        return self.x**2 + self.y**2 < other.x**2 + other.y**2


a = Point(1, 2)
b = Point(3, 4)

print("a =", a)
print("a + b =", a + b)  # ruft a.__add__(b) auf
print("a == Point(1, 2):", a == Point(1, 2))  # ruft a.__eq__(...) auf
print("a < b:", a < b)  # ruft a.__lt__(b) auf
print("b > a:", b > a)  # kein __gt__: Python prüft stattdessen a < b

points = [Point(5, 5), Point(0, 1), Point(2, 2)]
print("sortiert:", sorted(points))  # sorted vergleicht mit __lt__
