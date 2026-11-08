# Zahlenraten – Starter für Lab 3.1 (Stand nach Lab 2.4)

secret = 7

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()  # "  aNNa " -> "Anna"
print(f"Hallo {name}! Rate eine Zahl zwischen 1 und 10.")

guess = int(input("Tipp: "))

print(f"{name} tippt {guess}")
# TODO Lab 3.1: statt True/False einen Hinweis ausgeben: „Zu hoch.“, „Zu niedrig.“ oder „Richtig, <Name>!“
print("Treffer:", guess == secret)
