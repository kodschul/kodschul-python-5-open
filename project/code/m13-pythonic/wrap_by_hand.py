# Vom Funktionswert zum Decorator: einpacken von Hand, dann mit @


def greet(name):
    """Begrüßt eine Person."""
    print(f"Hallo, {name}!")


# 1. Funktion, die eine Funktion bekommt und eine neue Funktion zurückgibt
def announce(func):
    """Packt func ein: vorher und nachher eine Zeile ausgeben."""

    def wrapper(name):
        print("-- vorher --")
        func(name)  # die eingepackte Funktion aufrufen
        print("-- nachher --")

    return wrapper  # zurückgeben, nicht aufrufen


# 2. Von Hand einpacken: der Name greet zeigt jetzt auf wrapper
greet = announce(greet)
greet("Anna")
print("greet heißt jetzt:", greet.__name__)


# 3. Dasselbe mit @: kurz für  welcome = announce(welcome)
@announce
def welcome(name):
    """Heißt eine Person willkommen."""
    print(f"Willkommen, {name}!")


welcome("Ben")
