# Wo steht das Terminal, wo liegt das Skript? Path.cwd() und Path(__file__)
# Start im Ordner project/: python code/m17-data-formats/where_am_i.py
# Vergleich: cd playground, dann python ../code/m17-data-formats/where_am_i.py

from pathlib import Path

print("Terminal steht in:", Path.cwd())  # hängt davon ab, wo gestartet wird
print("Diese Datei:      ", Path(__file__))  # __file__ = Pfad dieser .py-Datei
print("Ordner der Datei: ", Path(__file__).parent)  # immer derselbe Ordner

# zwei Wege zur selben Datei data/shopping_items.html
relative = Path("data") / "shopping_items.html"  # relativ zum Terminal
project = Path(__file__).parent.parent.parent  # code/m17-data-formats -> project
next_to_script = project / "data" / "shopping_items.html"  # relativ zum Skript
print("Path('data') / ... gefunden?      ", relative.exists())
print("Path(__file__).parent... gefunden?", next_to_script.exists())
