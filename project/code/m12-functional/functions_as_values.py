# Funktionen sind Werte: in Variablen, als Argument, in Dictionaries, als Rückgabe


def double(number):
    """Gibt die doppelte Zahl zurück."""
    return number * 2


def square(number):
    """Gibt die Zahl mal sich selbst zurück."""
    return number * number


# 1. In einer Variablen: ohne () wird die Funktion nicht aufgerufen, nur benannt
action = double
print("action(5):", action(5))
print("Typ:", type(action))


# 2. Als Argument: apply_to_all bekommt eine Funktion und ruft sie selbst auf
def apply_to_all(function, numbers):
    """Wendet function auf jede Zahl an und gibt die neue Liste zurück."""
    return [function(number) for number in numbers]


print("doppelt:", apply_to_all(double, [1, 2, 3]))
print("Quadrat:", apply_to_all(square, [1, 2, 3]))

# 3. In einem Dictionary: Name -> Funktion, Auswahl per Schlüssel
operations = {"doppelt": double, "quadrat": square}
choice = "quadrat"
print(f"{choice}(7):", operations[choice](7))

# 4. lambda: kleine Funktion ohne Namen, direkt an der Stelle, wo sie gebraucht wird
operations["halb"] = lambda number: number / 2
print("halb(7):", operations["halb"](7))


# 5. Als Rückgabewert: Closure merkt sich den Wert von percent
def make_discount(percent):
    """Gibt eine Funktion zurück, die immer percent Prozent abzieht."""

    def discount(price):
        return round(price * (100 - percent) / 100, 2)

    return discount


student_price = make_discount(20)  # merkt sich 20
print("Studierendenpreis von 15 €:", student_price(15))
print("Studierendenpreis von 40 €:", student_price(40))
