# Sicherer Zahlen-Input: so lange fragen, bis eine Zahl kommt (Lab 7.2)

while True:
    text = input("Zahl: ")
    try:
        number = float(text)  # kann ValueError auslösen
    except ValueError:  # nur dieser Fehler wird abgefangen
        print(f"'{text}' ist keine Zahl. Bitte erneut versuchen.")
    else:  # läuft nur, wenn im try-Block kein Fehler auftrat
        break

print(f"{number} ist eine gültige Zahl. Das Doppelte: {number * 2}")
