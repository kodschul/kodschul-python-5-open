# map: eine Funktion auf jedes Element anwenden (aus dem alten Kurs, bereinigt)

nums = [2, 4, 6, 8, 9]

# Vorher: Schleife mit append
nums_squared = []
for num in nums:
    nums_squared.append(num**2)
print("Schleife:     ", nums_squared)


# map mit benannter Funktion
def square_num(num):
    """Gibt num hoch 2 zurück."""
    return num**2


print("map + def:    ", list(map(square_num, nums)))  # list(): Ergebnis einsammeln

# map mit lambda: dieselbe Funktion ohne Namen
print("map + lambda: ", list(map(lambda num: num**2, nums)))

# dasselbe als Listen-Comprehension (Lab 12.1)
print("Comprehension:", [num**2 for num in nums])

# map gibt kein fertiges Ergebnis, sondern ein map-Objekt, das erst auf Anfrage rechnet
print("ohne list():  ", map(square_num, nums))

persons = [
    {"name": "Fritz", "age": 18},
    {"name": "Paul", "age": 15},
    {"name": "Marie", "age": 40},
]
names = map(lambda person: person["name"], persons)
print("Namen:", list(names))
