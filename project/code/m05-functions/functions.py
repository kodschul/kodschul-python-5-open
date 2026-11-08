# Eigene Funktionen: definieren, aufrufen, Rückgabewert verwenden


def greet(name):
    """Gibt eine Begrüßung für name aus."""
    print(f"Hallo {name}, willkommen im Kurs!")
    # kein return: Prozedur, das Ergebnis ist None


def is_even(number):
    """Gibt True zurück, wenn number gerade ist."""
    return number % 2 == 0


# Die Definition allein gibt nichts aus; erst der Aufruf führt den Körper aus
greet("Anna")
greet("Ben")

print(is_even(4))
print(is_even(7))

# Rückgabewert direkt als Bedingung verwenden
for number in range(1, 5):
    if is_even(number):
        print(f"{number} ist gerade")
    else:
        print(f"{number} ist ungerade")

# Eine Prozedur liefert None
result = greet("Cem")
print("Ergebnis von greet:", result)
