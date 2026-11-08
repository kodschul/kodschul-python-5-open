# Nutzt das Paket helpers (Ordner mit __init__.py und zwei Modulen)

from helpers import calculator  # Modul aus dem Paket
from helpers.percent import percent_of  # Funktion aus einem Modul des Pakets

price = 80
print("80 + 20 =", calculator.add(price, 20))
print("80 / 4 =", calculator.divide(price, 4))
print("15 % von 80 =", percent_of(price, 15))
