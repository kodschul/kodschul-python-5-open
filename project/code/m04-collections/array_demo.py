# Modul array: typisierte Zahlenreihe (alle Werte haben denselben Typ)

import array

# "d" = Kommazahlen (float), "i" = ganze Zahlen (int)
temperatures = array.array("d", [12.5, 14.0, 9.8, 11.2])
print(temperatures)
print("Erster Wert:", temperatures[0])
print("Anzahl:", len(temperatures))
print("Mittelwert:", round(sum(temperatures) / len(temperatures), 2))

temperatures.append(13.1)  # wie bei einer Liste
print("Nach append:", temperatures)

# Eine Liste nimmt alles auf, ein Array nur Zahlen des festgelegten Typs
mixed = [12.5, "warm", True]
print("Liste mit gemischten Typen:", mixed)
# temperatures.append("warm")  # TypeError: must be real number, not str
