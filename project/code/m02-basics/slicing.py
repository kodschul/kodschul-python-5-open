# Lab 2.4: Index und Slicing

word = "Python"

# Index-Tabelle ausgeben
print("Zeichen:  P  y  t  h  o  n")
print("Index:    0  1  2  3  4  5")
print("negativ: -6 -5 -4 -3 -2 -1")
print()

print("word[0]   =", word[0])  # erstes Zeichen
print("word[-1]  =", word[-1])  # letztes Zeichen
print("word[1:4] =", word[1:4])  # Index 1 bis 3 (4 ist nicht dabei)
print("word[:3]  =", word[:3])  # die ersten drei Zeichen
print("word[3:]  =", word[3:])  # ab Index 3 bis zum Ende
print("word[::2] =", word[::2])  # jedes zweite Zeichen
print("len(word) =", len(word))  # Anzahl der Zeichen
