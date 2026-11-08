# Zahlenraten – Stand Lab 2.3: Tipp mit der Geheimzahl vergleichen

secret = 7  # vorerst fest; ab Lab 3.2 zufällig

print("=" * 40)
print("Zahlenraten")
print("Rate eine Zahl zwischen 1 und 10.")
print("=" * 40)

name = input("Name: ")
guess = int(input("Tipp: "))

print(f"{name} tippt {guess}")
print("Treffer:", guess == secret)  # == liefert True oder False
