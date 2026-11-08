# Lab 2.3: gerade oder ungerade? (Rest mit %)

number = int(input("Zahl: "))

remainder = number % 2  # Rest beim Teilen durch 2: 0 oder 1
print(f"{number} % 2 = {remainder}")
print("gerade:", remainder == 0)
