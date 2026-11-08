# Lab 2.4: String-Methoden

raw = "  aNNa schMIDT  "

print(f"[{raw}]")
print(f"[{raw.strip()}]")  # Leerzeichen am Rand entfernen
print(raw.strip().lower())  # alles klein
print(raw.strip().upper())  # alles groß
print(raw.strip().title())  # jedes Wort mit Großbuchstaben beginnen
print(raw.replace("NN", "nn"))  # Teil ersetzen
print(raw.strip().startswith("aN"))  # beginnt mit ...? -> True/False
print("schMIDT" in raw)  # enthält ...? -> True/False
print("rot;grün;blau".split(";"))  # zerlegen -> Liste (mehr in Lab 4.1)

# Strings sind unveränderlich: Methoden liefern einen NEUEN String
name = "anna"
name.upper()  # Ergebnis wird nicht gespeichert
print(name)  # anna
name = name.upper()
print(name)  # ANNA
