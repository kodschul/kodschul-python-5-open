# Grenzen von JSON: nicht jeder Python-Typ lässt sich speichern

import json
from datetime import datetime

print(json.dumps((1, 10)))  # Tupel wird zur Liste [1, 10]

for value in [{5, 8}, datetime(2026, 11, 8, 14, 5)]:
    try:
        print(json.dumps(value))
    except TypeError as error:
        print("TypeError:", error)

# Ausweg: vorher in einen passenden Typ umwandeln
print(json.dumps(sorted({5, 8})))  # Set -> sortierte Liste
print(json.dumps(datetime(2026, 11, 8, 14, 5).strftime("%Y-%m-%d %H:%M")))
