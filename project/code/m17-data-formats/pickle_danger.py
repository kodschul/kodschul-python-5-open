# Warum pickle nur eigene Dateien laden darf: beim Laden läuft Code
# Harmlose Vorführung: die Datei ruft nur print auf, sie könnte aber alles tun
# Start im Ordner project/: python code/m17-data-formats/pickle_danger.py

import pickle
from pathlib import Path

TRAP_FILE = Path("playground") / "trap.pkl"


class Trap:
    def __reduce__(self):
        # pickle fragt: "Wie wird dieses Objekt beim Laden wieder aufgebaut?"
        # Antwort hier: "Rufe print mit diesem Text auf" (statt z. B. Dateien löschen)
        return (print, ("!!! Diese Zeile hat die Datei beim Laden ausgeführt !!!",))


with open(TRAP_FILE, "wb") as file:
    pickle.dump(Trap(), file)
print(f"{TRAP_FILE} geschrieben. Jetzt nur laden, sonst nichts:")

with open(TRAP_FILE, "rb") as file:
    result = pickle.load(file)  # führt print(...) aus
print("pickle.load hat geliefert:", result)
