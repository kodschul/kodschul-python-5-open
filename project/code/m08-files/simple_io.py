# Pfade mit pathlib: zusammensetzen, prüfen, Text schreiben und lesen

from pathlib import Path

print("Aktueller Ordner:", Path.cwd())  # dort, wo das Terminal gerade steht

names_file = Path("data") / "names.txt"  # relativer Pfad, / fügt Teile zusammen
print("Relativ:", names_file)
print("Absolut:", names_file.absolute())
print("Existiert?", names_file.exists())
print("Dateiname:", names_file.name)

missing = Path("data") / "gibt_es_nicht.txt"
print("Existiert gibt_es_nicht.txt?", missing.exists())

# write_text: ganze Datei auf einmal schreiben (vorhandener Inhalt wird ersetzt)
note = Path("playground") / "note.txt"
note.write_text("Hallo Datei!\nGrüße aus Köln\n", encoding="utf-8")
print("Geschrieben:", note)

# read_text: ganze Datei auf einmal als einen String lesen
text = note.read_text(encoding="utf-8")
print("Gelesen:")
print(text)
