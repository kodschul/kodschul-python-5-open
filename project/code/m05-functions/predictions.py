# Vorhersage-Übung (Lab 5.3): erst alle fünf Ausgaben vorhersagen, dann starten

# Snippet 1: Zahl mit zwei Namen
a = 3
b = a
b = b + 1
print("Snippet 1:", a, b)

# Snippet 2: Liste mit zwei Namen
x = [1, 2]
y = x
y.append(3)
print("Snippet 2:", x)


# Snippet 3: Zahl an eine Funktion übergeben
def double(n):
    n = n * 2


value = 5
double(value)
print("Snippet 3:", value)


# Snippet 4: Liste an eine Funktion übergeben
def add_cheese(items):
    items.append("Käse")


shopping = ["Brot"]
add_cheese(shopping)
print("Snippet 4:", shopping)

# Snippet 5: gleicher Inhalt oder dasselbe Objekt?
first = [1, 2]
second = [1, 2]
print("Snippet 5:", first == second, first is second)
