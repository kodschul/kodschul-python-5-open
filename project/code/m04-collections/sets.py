# Sets: Mengen ohne doppelte Werte

numbers = {1, 1, 2, 3, 3, 3}
print("Set:", numbers)            # Duplikate sind weg

numbers.add(4)
numbers.add(1)                    # schon vorhanden: nichts passiert
print("Nach add:", numbers)
print("Ist 2 enthalten?", 2 in numbers)

# Mengenoperationen: zwei Kurse und ihre Teilnehmenden
python_course = {"Anna", "Ben", "Cem", "Dana"}
excel_course = {"Ben", "Dana", "Eva"}

print("In beiden Kursen:", python_course & excel_course)       # Schnitt
print("In mindestens einem Kurs:", python_course | excel_course)  # Vereinigung
print("Nur im Python-Kurs:", python_course - excel_course)     # Differenz

# Liste ohne Duplikate: in ein Set umwandeln, dann zurück in eine Liste
dice = [6, 2, 6, 3, 2, 6]
print("Gewürfelte Augenzahlen:", sorted(set(dice)))
print("Verschiedene Werte:", len(set(dice)))

empty = set()                     # leeres Set; {} wäre ein leeres Dictionary
print("Leeres Set:", empty)
