# E-Mail-Adressen aufräumen: Listen-, Set- und Dict-Comprehension

emails = [
    " Anna@Uni-Koeln.de",
    "ben@example.org ",
    "ANNA@uni-koeln.de",
    "cem@Example.org",
]

# Liste: jede Adresse ohne Leerzeichen und klein geschrieben
cleaned = [email.strip().lower() for email in emails]
print("Liste:", cleaned)

# Set: geschweifte Klammern, doppelte Adressen fallen weg
unique = {email.strip().lower() for email in emails}
print("Set:", sorted(unique))  # sorted: Sets haben keine feste Reihenfolge

# Dictionary: Schlüssel: Wert – Adresse -> Domain (Teil nach dem @)
domains = {email: email.split("@")[1] for email in sorted(unique)}
print("Dictionary:", domains)

# Mit Bedingung: nur Adressen der Uni
uni = [email for email in sorted(unique) if email.endswith("uni-koeln.de")]
print("Nur Uni:", uni)
