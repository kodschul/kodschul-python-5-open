# Lab 15.2: Die wichtigsten Funktionen aus dem Modul re
import re

text = "Raum B204, Raum C12 und Raum A7"

# search: erste passende Stelle irgendwo im Text (oder None)
match = re.search(r"\d+", text)  # \d+ = eine oder mehr Ziffern
print("search:   ", match.group())  # der gefundene Text

# match: nur ganz am Anfang des Textes
print("match:    ", re.match(r"\d+", text))  # None: der Text beginnt mit "R"
print("match:    ", re.match(r"Raum", text).group())

# fullmatch: der ganze Text muss passen
print("fullmatch:", re.fullmatch(r"[A-Z]\d+", "B204") is not None)
print("fullmatch:", re.fullmatch(r"[A-Z]\d+", "B204a") is not None)

# findall: alle Treffer als Liste
print("findall:  ", re.findall(r"[A-Z]\d+", text))

# Gruppen in runden Klammern: findall liefert dann nur die Gruppen
print("Gruppen:  ", re.findall(r"([A-Z])(\d+)", text))

# sub: Treffer ersetzen
print("sub:      ", re.sub(r"\d", "#", text))

# Flag IGNORECASE: Groß- und Kleinschreibung egal
print("Flag:     ", re.findall(r"raum", text, re.IGNORECASE))

# Raw-String r"...": der Backslash bleibt ein Backslash
normal = "\bAnna"  # ohne r: \b wird zum Steuerzeichen "Rückschritt"
raw = r"\bAnna"  # mit r: Backslash + b = Wortgrenze im Muster
print("ohne r:   ", re.findall(normal, "Anna und Hanna"))
print("mit r:    ", re.findall(raw, "Anna und Hanna"))
