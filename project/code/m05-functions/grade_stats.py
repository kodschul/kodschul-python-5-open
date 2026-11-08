# Mehrere Rückgabewerte: return mit Komma liefert ein Tupel


def grade_stats(grades):
    """Gibt beste Note, schlechteste Note und Durchschnitt zurück."""
    best = min(grades)  # deutsche Noten: kleiner ist besser
    worst = max(grades)
    average = round(sum(grades) / len(grades), 2)
    return best, worst, average


result = grade_stats([1.7, 2.3, 1.0, 3.0])
print("Ergebnis:", result)

best, worst, average = grade_stats([2.0, 1.3, 2.3])  # direkt entpacken
print(f"Beste: {best}, schlechteste: {worst}, Durchschnitt: {average}")
