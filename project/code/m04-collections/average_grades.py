# Notendurchschnitt mit eingebauten Funktionen berechnen

grades = [1.7, 2.3, 1.0, 3.0, 2.0]

average = sum(grades) / len(grades)

print("Noten:", grades)
print("Anzahl Noten:", len(grades))
print("Durchschnitt:", round(average, 2))  # auf 2 Nachkommastellen runden
print("Beste Note:", min(grades))          # kleinste Zahl = beste Note
print("Schlechteste Note:", max(grades))
print("Sortiert:", sorted(grades))         # neue, sortierte Liste
print("Original bleibt:", grades)

# Neue Note eintragen und Durchschnitt neu berechnen
grades.append(1.3)
print(f"Mit neuer Note: {round(sum(grades) / len(grades), 2)}")
