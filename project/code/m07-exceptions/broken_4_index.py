# Kaputtes Skript 4 (Lab 7.1): letzte Note einer Liste
# Aufgabe: starten, Fehlertyp, Zeile und Ursache notieren – nicht vorher reparieren.


def last_grade(grades):
    """Gibt die letzte Note der Liste zurück."""
    return grades[len(grades)]


grades = [2.0, 1.3, 2.7]
print(f"Letzte Note: {last_grade(grades)}")
