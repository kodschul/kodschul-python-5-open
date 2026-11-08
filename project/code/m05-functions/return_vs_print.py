# return oder print? Nur ein Rückgabewert lässt sich weiterverwenden


def add_and_print(a, b):
    """Gibt die Summe aus, gibt aber nichts zurück."""
    print(a + b)


def add(a, b):
    """Gibt die Summe zurück, ohne etwas auszugeben."""
    return a + b


x = add_and_print(2, 3)  # zeigt 5 im Terminal, x ist None
y = add(2, 3)  # zeigt nichts, y ist 5

print("x =", x)
print("y =", y)
print("y * 10 =", y * 10)
# print("x * 10 =", x * 10)  # TypeError: None lässt sich nicht multiplizieren
