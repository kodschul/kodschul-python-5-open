# JSON: Python-Daten in Text verwandeln (dumps/dump) und zurück (loads/load)

import json
from pathlib import Path

score = {
    "name": "Jürgen",
    "tries": 3,
    "seconds": 12.4,
    "won": True,
    "guesses": [5, 8, 10],
    "bonus": None,
}

text = json.dumps(score)  # Dictionary -> JSON-Text (ein String)
print(text)
print(type(text))

pretty = json.dumps(score, indent=2, ensure_ascii=False)  # eingerückt, Umlaute lesbar
print(pretty)

back = json.loads(text)  # JSON-Text -> Dictionary
print(back["name"], back["tries"], type(back))

# mit Datei: dump schreibt in die Datei, load liest aus der Datei
target = Path("playground") / "score.json"
with open(target, "w", encoding="utf-8") as file:
    json.dump(score, file, indent=2, ensure_ascii=False)

with open(target, encoding="utf-8") as file:
    loaded = json.load(file)
print("Aus Datei gelesen, gleich wie vorher?", loaded == score)
