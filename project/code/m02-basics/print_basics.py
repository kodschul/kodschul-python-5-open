# Lab 2.1: Anweisungen, Kommentare und print()
# Jede Zeile ist eine Anweisung. Python führt sie von oben nach unten aus.

print("Erste Zeile")
print("Zweite Zeile")  # Kommentar am Zeilenende: Python ignoriert alles ab #

# Mehrere Werte in einem print: Python setzt ein Leerzeichen dazwischen
print("Kurs:", "Python", 2026)

# sep legt fest, was zwischen den Werten steht
print("2026", "11", "08", sep="-")

# end legt fest, was am Ende steht (Standard: Zeilenumbruch)
print("Laden", end="")
print("...", end="")
print(" fertig")

# Ein leeres print() gibt eine leere Zeile aus
print()
print("Ende des Programms")
