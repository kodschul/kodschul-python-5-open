# Tupel: feste Gruppen von Werten, die sich nicht ändern

point = (3, 5)              # Koordinate x, y
number_range = (1, 10)      # Bereich: kleinste und größte Zahl
birthday = (14, 3, 2005)    # Tag, Monat, Jahr

print("Punkt:", point)
print("x-Wert:", point[0])  # Lesen per Index wie bei Listen
print("Anzahl Werte im Geburtstag:", len(birthday))

# Entpacken: jeder Wert landet in einer eigenen Variablen
low, high = number_range
print(f"Bereich von {low} bis {high}")

day, month, year = birthday
print(f"Geboren am {day}.{month}.{year}")

# Tupel in einer Liste: mehrere Punkte
route = [(0, 0), (3, 5), (6, 2)]
for x, y in route:
    print(f"Gehe zu x={x}, y={y}")

# point[0] = 4  # TypeError: 'tuple' object does not support item assignment
