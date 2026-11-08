# Lab 2.3: Operatoren und Vergleiche

# Rechnen
print(7 + 2, 7 - 2, 7 * 2)  # 9 5 14
print(7 / 2)  # 3.5  (Division liefert immer float)
print(7 // 2)  # 3    (ganzzahlige Division)
print(7 % 2)  # 1    (Rest der Division)
print(2**3)  # 8    (Potenz)

# Zuweisungsoperatoren
points = 10
points += 5  # wie: points = points + 5
points -= 3  # wie: points = points - 3
print("Punkte:", points)

# Vergleiche liefern True oder False
a = 5
b = 3
print(a == b, a != b, a > b, a <= b)  # False True True False

# Logische Operatoren
raining = True
cold = False
print("Regen und kalt:", raining and cold)
print("Regen oder kalt:", raining or cold)
print("kein Regen:", not raining)

# Vorrang: * vor +, Klammern zuerst
print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
