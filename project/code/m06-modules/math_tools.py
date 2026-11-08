# Eigenes Modul: zwei Rechenfunktionen, die andere Dateien importieren können


def add(a, b):
    """Gibt die Summe von a und b zurück."""
    return a + b


def subtract(a, b):
    """Gibt die Differenz a - b zurück."""
    return a - b


# Läuft nur, wenn diese Datei direkt gestartet wird, nicht beim Import
if __name__ == "__main__":
    print("__name__ ist:", __name__)
    print("Selbsttest: 2 + 3 =", add(2, 3))
    print("Selbsttest: 10 - 4 =", subtract(10, 4))
