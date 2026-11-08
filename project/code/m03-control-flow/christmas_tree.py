# Weihnachtsbaum aus Sternen: eine for-Schleife statt jeder Zeile einzeln

height = 6  # Anzahl der Sternzeilen

print(" " * height + "X")  # Spitze

for row in range(height):  # row läuft von 0 bis height - 1
    spaces = " " * (height - row)  # nach unten immer weniger Leerzeichen
    stars = "*" * (2 * row + 1)  # 1, 3, 5, ... Sterne
    print(spaces + stars)

print(" " * (height - 1) + "###")  # Stamm
