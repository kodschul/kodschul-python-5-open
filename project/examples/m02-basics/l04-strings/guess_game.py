# Zahlenraten – Stand Lab 2.4: Spielernamen normalisieren

secret = 7

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()  # "  aNNa " -> "Anna"
print(f"Hallo {name}! Rate eine Zahl zwischen 1 und 10.")

guess = int(input("Tipp: "))

print(f"{name} tippt {guess}")
print("Treffer:", guess == secret)
