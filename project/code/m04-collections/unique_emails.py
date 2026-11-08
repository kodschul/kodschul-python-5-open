# Doppelte E-Mail-Adressen aus einer Anmeldeliste entfernen

signups = [
    "anna@uni-beispiel.de",
    "ben@uni-beispiel.de",
    " Anna@Uni-Beispiel.DE ",
    "cem@uni-beispiel.de",
    "ben@uni-beispiel.de",
]

unique = set()
for email in signups:
    unique.add(email.strip().lower())  # vereinheitlichen, dann sammeln

print("Anmeldungen:", len(signups))
print("Verschiedene Adressen:", len(unique))
for email in sorted(unique):
    print("-", email)
