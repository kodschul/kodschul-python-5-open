# Fehlerbeispiel: Endlosschleife. Abbrechen mit Strg+C (macOS: control+C).

count = 1
while count <= 3:
    print(f"Durchlauf {count}")
    # Hier fehlt eine Zeile, die count verändert: Die Bedingung bleibt immer wahr.
