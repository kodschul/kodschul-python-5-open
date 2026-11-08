# Lab 2.2: Alter abfragen und Geburtsjahr berechnen

current_year = 2026

age_text = input("Alter: ")  # input() liefert immer Text
age = int(age_text)  # Text in eine ganze Zahl umwandeln

birth_year = current_year - age
print(f"Geburtsjahr: {birth_year} oder {birth_year - 1}")
print(type(age_text), type(age))
