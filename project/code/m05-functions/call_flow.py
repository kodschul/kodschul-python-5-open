# Aufruf-Ablauf: Wohin springt das Programm bei einem Funktionsaufruf?


def make_tea(kind):
    """Bereitet einen Tee zu und gibt die fertige Tasse zurück."""
    print(f"  2. in make_tea: Wasser kochen, {kind} aufgießen")
    return f"Tasse {kind}"


print("1. Hauptprogramm: vor dem Aufruf")
cup = make_tea("Pfefferminztee")  # Sprung in die Funktion, Rückgabe landet in cup
print(f"3. Hauptprogramm: zurück mit „{cup}“")
