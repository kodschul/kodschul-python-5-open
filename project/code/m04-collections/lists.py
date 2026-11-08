# Listen: eine Einkaufsliste anlegen, lesen und ändern

shopping = ["Milch", "Brot", "Äpfel", "Käse"]
print("Liste:", shopping)
print("Anzahl:", len(shopping))

# Lesen per Index: Zählung beginnt bei 0
print("Erster Eintrag:", shopping[0])
print("Letzter Eintrag:", shopping[-1])   # negativ: von hinten zählen
print("Slicing [1:3]:", shopping[1:3])    # Index 1 bis vor 3

# Ändern: Listen sind veränderbar
shopping[1] = "Vollkornbrot"              # Eintrag ersetzen
shopping.append("Kaffee")                 # hinten anhängen
shopping.insert(0, "Butter")              # an Position 0 einfügen
shopping.remove("Käse")                   # ersten passenden Wert entfernen
last = shopping.pop()                     # letzten Eintrag herausnehmen
print("Herausgenommen:", last)
print("Liste jetzt:", shopping)

# Prüfen, ob ein Wert enthalten ist
if "Milch" in shopping:
    print("Milch steht auf der Liste.")

# Jeden Eintrag einzeln bearbeiten
for item in shopping:
    print("-", item)
