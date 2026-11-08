# Rabatt-Check: Welcher Rabatt gilt an der Kasse?
# Regeln: Mitglieder 20 %, unter 14 oder ab 65 Jahren 15 %,
# Studierende unter 30 Jahren 10 %, alle anderen 0 %.

age = int(input("Alter: "))
is_student = input("Studierend? (j/n): ").strip().lower() == "j"
is_member = input("Mitglied? (j/n): ").strip().lower() == "j"

if is_member:  # höchster Rabatt zuerst prüfen
    discount = 20
elif age < 14 or age >= 65:  # eine der beiden Bedingungen genügt
    discount = 15
elif is_student and age < 30:  # beide Bedingungen müssen stimmen
    discount = 10
else:  # keine Regel passt
    discount = 0

if discount > 0:
    print(f"Rabatt: {discount} %")
else:
    print("Kein Rabatt.")

# Bedingungsausdruck: ein Wert, je nach Bedingung
status = "Mitglied" if is_member else "Gast"
print(f"Status: {status}")
