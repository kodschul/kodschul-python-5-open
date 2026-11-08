# Zahlenraten – Starter für Lab 3.2 (Stand nach Lab 3.1)

# TODO Lab 3.2: random importieren und die Geheimzahl per random.randint(1, 10) ziehen
secret = 7

print("=" * 40)
print("Zahlenraten")
print("=" * 40)

name = input("Name: ").strip().title()
print(f"Hallo {name}! Rate eine Zahl zwischen 1 und 10.")

guess = int(input("Tipp: "))

if guess > secret:
    print("Zu hoch.")
elif guess < secret:
    print("Zu niedrig.")
else:
    print(f"Richtig, {name}!")
