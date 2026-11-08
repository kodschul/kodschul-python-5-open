# Lab 15.2: Drittmodul regex – Unicode-Kategorien wie \p{L} (= jeder Buchstabe)
import re

import regex  # pip install regex (steht in requirements.txt)

text = "Zoë, José, Jürgen, Łukasz und R2D2"

# re: die Zeichenklasse kennt nur die aufgezählten Buchstaben
print("re    [A-Za-zÄÖÜäöüß]+:", re.findall(r"[A-Za-zÄÖÜäöüß]+", text))

# regex: \p{L} passt auf jeden Buchstaben jeder Sprache, aber nicht auf Ziffern
print("regex \\p{L}+:         ", regex.findall(r"\p{L}+", text))

# re kennt \p{L} nicht
try:
    re.findall(r"\p{L}+", text)
except re.error as error:
    print("re    \\p{L}+:          re.error:", error)
