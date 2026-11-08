# Dataclass: dieselbe Klasse einmal von Hand, einmal mit @dataclass

import json
from dataclasses import asdict, dataclass


class ProductByHand:
    """Von Hand: __init__ schreibt jedes Attribut einzeln, print zeigt nichts."""

    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock


@dataclass  # erzeugt __init__, __repr__ und __eq__ aus den Feldern
class Product:
    """Mit @dataclass: nur die Felder mit Typ angeben."""

    name: str  # Feld: Typ (Python prüft den Typ nicht)
    price: float
    stock: int = 0  # Standardwert: darf beim Erzeugen fehlen

    def total_value(self):
        """Eigene Methoden funktionieren wie in jeder Klasse."""
        return self.price * self.stock


print(ProductByHand("Kaffee", 4.99, 12))

coffee = Product("Kaffee", 4.99, 12)
tea = Product("Tee", 2.49)  # stock bekommt den Standardwert 0
print(coffee)  # __repr__ kommt von @dataclass
print(tea)
print("Gleich?", coffee == Product("Kaffee", 4.99, 12))  # __eq__ vergleicht Felder
print("Lagerwert:", round(coffee.total_value(), 2))

data = asdict(coffee)  # Dataclass -> Dictionary
print(data)
print(json.dumps(data, ensure_ascii=False))  # und weiter nach JSON

wrong = Product("Saft", "teuer")  # falscher Typ: Python meldet nichts
print(wrong)
