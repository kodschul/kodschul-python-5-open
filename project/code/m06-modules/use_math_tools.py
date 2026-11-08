# Drei Arten, das eigene Modul math_tools.py zu importieren

import math_tools  # 1. ganzes Modul, Aufruf mit math_tools.add
import math_tools as mt  # 2. ganzes Modul unter kürzerem Namen
from math_tools import subtract  # 3. nur eine Funktion, Aufruf ohne Präfix

print("math_tools.add(7, 5) =", math_tools.add(7, 5))
print("mt.add(1, 1) =", mt.add(1, 1))
print("subtract(7, 5) =", subtract(7, 5))

# Beim Import heißt das Modul nicht "__main__", sondern wie seine Datei
print("Name des importierten Moduls:", math_tools.__name__)
