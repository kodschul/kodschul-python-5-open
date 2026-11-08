# Intervallhalbierung: Zahl zwischen 1 und 100 in höchstens 7 Tipps finden (Lab 10.2)


def find_number(secret, low, high, show=False):
    """Rät immer die Mitte von low..high und gibt die Anzahl der Tipps zurück."""
    tries = 0
    while True:
        guess = (low + high) // 2  # Mitte, // schneidet die Nachkommastelle ab
        tries += 1
        if show:
            print(f"Tipp {tries}: Bereich {low}–{high}, Mitte {guess}")
        if guess == secret:
            return tries
        if guess > secret:  # zu hoch: obere Hälfte fällt weg
            high = guess - 1
        else:  # zu niedrig: untere Hälfte fällt weg
            low = guess + 1


print("Geheimzahl 76:")
tries = find_number(76, 1, 100, show=True)
print(f"Gefunden nach {tries} Tipps.\n")

most_tries = 0
for secret in range(1, 101):  # alle 100 möglichen Geheimzahlen ausprobieren
    tries = find_number(secret, 1, 100)
    if tries > most_tries:
        most_tries = tries
print(f"Schlechtester Fall bei 1–100: {most_tries} Tipps")

# Warum 7? Jeder Tipp halbiert den Bereich: 100 → 50 → 25 → 12 → 6 → 3 → 1
print("2 hoch 6 =", 2**6, "reicht nicht für 100 Zahlen; 2 hoch 7 =", 2**7)
