# Lab 2.3: einfacher Rechner für zwei Zahlen

a = float(input("Zahl 1: "))
b = float(input("Zahl 2: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {round(a / b, 2)}")  # round(..., 2): auf 2 Stellen runden
print(f"{a} ** {b} = {a**b}")
