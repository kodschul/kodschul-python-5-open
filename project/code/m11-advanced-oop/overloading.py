# Überladen in Python: eine Methode pro Name, dafür Standardwerte und Operatoren


class Greeter:
    """Zwei Methoden mit gleichem Namen: nur die zweite bleibt übrig."""

    def greet(self):
        return "Hallo!"

    def greet(self, name):  # noqa: F811 (Absicht: ersetzt die erste)
        return f"Hallo, {name}!"


greeter = Greeter()
print(greeter.greet("Anna"))
try:
    print(greeter.greet())  # die Version ohne name gibt es nicht mehr
except TypeError as error:
    print("TypeError:", error)


class FriendlyGreeter:
    """Statt Überladen: ein Standardwert macht den Parameter freiwillig."""

    def greet(self, name="Gast"):
        return f"Hallo, {name}!"


friendly = FriendlyGreeter()
print(friendly.greet())
print(friendly.greet("Anna"))


def add(*numbers):
    """Beliebig viele Zahlen: *numbers sammelt alle Argumente (Lab 5.2)."""
    return sum(numbers)


print(add(1), add(1, 2), add(1, 2, 3))

# Operatoren: dasselbe + ruft je nach Typ eine andere __add__-Methode auf
print(3 + 4, (3).__add__(4))  # int.__add__ rechnet
print("3" + "4", "3".__add__("4"))  # str.__add__ hängt an
print([3] + [4], [3].__add__([4]))  # list.__add__ verbindet Listen
