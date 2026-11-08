# Pseudozufall: gleicher Startwert (Seed) -> gleiche Zahlenfolge

import random

random.seed(42)  # Startwert festlegen
print("Durchgang 1:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

random.seed(42)  # derselbe Startwert noch einmal
print("Durchgang 2:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

random.seed()  # ohne Wert: neuer, unvorhersehbarer Startwert
print("Durchgang 3:", random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))
