# Ein Objekt speichern: pickle (Python-Objekt) und JSON (Text) im Vergleich
# Start im Ordner project/: python code/m17-data-formats/pickle_vs_json.py

import json
import pickle
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path

PICKLE_FILE = Path("playground") / "shopping_list.pkl"
JSON_FILE = Path("playground") / "shopping_list.json"


@dataclass
class ShoppingList:
    owner: str
    items: list
    created: datetime  # JSON kennt kein Datum


shopping = ShoppingList("Anna", ["Orangen", "Milch"], datetime(2026, 11, 8, 15, 30))

# 1. pickle: Objekt -> Bytes -> Datei ("wb" = write binary)
with open(PICKLE_FILE, "wb") as file:
    pickle.dump(shopping, file)
with open(PICKLE_FILE, "rb") as file:  # "rb" = read binary
    loaded = pickle.load(file)  # Bytes -> wieder ein ShoppingList-Objekt
print("pickle geladen:", loaded)
print("Typ:", type(loaded).__name__, "· gleich?", loaded == shopping)
with open(PICKLE_FILE, "rb") as file:
    print("Die ersten Bytes:", file.read()[:30])  # für Menschen unlesbar

# 2. JSON direkt: geht nicht, json kennt nur dict, list, str, Zahlen, bool, None
try:
    json.dumps(shopping)
except TypeError as error:
    print("JSON direkt:", error)

# 3. JSON mit Umwandlung: asdict -> Dictionary, default=str für das Datum
data = asdict(shopping)  # {"owner": "Anna", "items": [...], "created": datetime(...)}
with open(JSON_FILE, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2, default=str)
with open(JSON_FILE, encoding="utf-8") as file:
    print("JSON-Datei:")
    print(file.read())
with open(JSON_FILE, encoding="utf-8") as file:
    back = json.load(file)
print("JSON geladen:", type(back).__name__)  # ein Dictionary, kein Objekt
print("created ist jetzt:", type(back["created"]).__name__)  # Text, kein Datum

print("Größe pickle:", PICKLE_FILE.stat().st_size, "Bytes")
print("Größe JSON:  ", JSON_FILE.stat().st_size, "Bytes")
