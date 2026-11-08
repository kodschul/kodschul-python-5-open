# Rekursion: eine Funktion ruft sich selbst auf; der Aufrufstapel merkt sich jede Ebene


def countdown(number):
    """Zählt von number bis 0 herunter, indem sie sich selbst aufruft."""
    if number == 0:  # Abbruchbedingung: hier endet die Rekursion
        print("Start!")
        return
    print(number)
    countdown(number - 1)  # gleicher Ablauf mit kleinerer Zahl


def count_up(number, limit, depth=0):
    """Zählt in Zweierschritten bis über limit und zeigt jede Ebene eingerückt."""
    indent = "  " * depth
    print(f"{indent}→ count_up({number}, {limit})")
    if number > limit:
        print(f"{indent}← gibt {number} zurück")
        return number
    result = count_up(number + 2, limit, depth + 1)
    print(f"{indent}← gibt {result} zurück")
    return result


countdown(3)
print()
final = count_up(1, 6)
print("Ergebnis:", final)
