# Erst ohne Decorator: dieselbe Prüfung steht in jeder Funktion von Hand


def square_area(side):
    """Fläche eines Quadrats."""
    if side <= 0:  # Prüfung 1
        raise ValueError(f"{side} ist keine positive Länge.")
    return side * side


def rectangle_area(width, height):
    """Fläche eines Rechtecks."""
    if width <= 0:  # Prüfung 2: dieselbe Zeile noch einmal
        raise ValueError(f"{width} ist keine positive Länge.")
    if height <= 0:  # Prüfung 3
        raise ValueError(f"{height} ist keine positive Länge.")
    return width * height


def triangle_area(base, height):
    """Fläche eines Dreiecks."""
    if base <= 0:  # Prüfung 4
        raise ValueError(f"{base} ist keine positive Länge.")
    if height <= 0:  # Prüfung 5
        raise ValueError(f"{height} ist keine positive Länge.")
    return base * height / 2


print("Quadrat:", square_area(4))
print("Rechteck:", rectangle_area(3, 5))
print("Dreieck:", triangle_area(6, 2))
try:
    rectangle_area(3, -5)
except ValueError as error:
    print("Fehler:", error)
