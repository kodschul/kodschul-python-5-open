# Würfel: zwei Würfe mit random.randint

import random  # Werkzeug aus der Standardbibliothek holen

first = random.randint(1, 6)  # ganze Zahl von 1 bis 6, beide Grenzen möglich
second = random.randint(1, 6)

print(f"Wurf 1: {first}")
print(f"Wurf 2: {second}")
print(f"Summe: {first + second}")

if first == second:
    print("Pasch!")
