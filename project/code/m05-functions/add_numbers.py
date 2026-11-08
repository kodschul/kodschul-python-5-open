# *args: beliebig viele Werte nach Position, gesammelt in einem Tupel


def add(*numbers):
    """Addiert beliebig viele Zahlen und gibt die Summe zurück."""
    print("numbers ist", numbers)  # ein Tupel aus allen Argumenten
    total = 0
    for number in numbers:
        total += number
    return total


print(add(1, 2))
print(add(1, 2, 3, 4))
print(add())  # kein Argument: leeres Tupel, Summe 0
