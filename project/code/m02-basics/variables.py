# Lab 2.2: Variablen und Datentypen

name = "Anna"  # str: Text
age = 21  # int: ganze Zahl
height = 1.68  # float: Kommazahl (mit Punkt geschrieben)
is_student = True  # bool: True oder False
phone = None  # None: "noch kein Wert"

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print(phone, type(phone))

# Dynamische Typisierung: dieselbe Variable kann später einen anderen Typ tragen
age = "einundzwanzig"
print(age, type(age))

# Umwandeln
print(int("42") + 1)  # Text -> ganze Zahl
print(float("1.5") * 2)  # Text -> Kommazahl
print(str(42) + "!")  # Zahl -> Text
print("3" + "4")  # zwei Texte werden aneinandergehängt
print(int("3") + int("4"))
