# Rundgang durch die Standardbibliothek: alles ohne Installation verfügbar

import json
import math
import os
import random
from datetime import date
from pathlib import Path

print("math.sqrt(16) =", math.sqrt(16))
print("math.pi =", round(math.pi, 4))

random.seed(1)  # fester Startwert: gleiche "Zufallszahl" bei jedem Lauf
print("random.choice:", random.choice(["Stein", "Schere", "Papier"]))

print("Heute:", date.today())

print("requirements.txt vorhanden:", Path("requirements.txt").exists())

print("Betriebssystem-Familie (os.name):", os.name)

text = json.dumps({"name": "Anna", "tries": 3})
print("Als JSON-Text:", text)
