# with schließt die Datei auch dann, wenn im Block ein Fehler passiert

from pathlib import Path

note_file = Path("playground") / "note.txt"  # Start im Ordner project/

try:
    with open(note_file, "w", encoding="utf-8") as file:
        file.write("Zeile 1\n")
        print("im Block, geschlossen?", file.closed)
        number = int("abc")  # ValueError mitten im Schreiben
        file.write("Zeile 2\n")  # wird nie erreicht
except ValueError as error:
    print("Fehler:", error)

print("nach dem Block, geschlossen?", file.closed)
print("Inhalt:", repr(note_file.read_text(encoding="utf-8")))
note_file.unlink()  # unlink: Datei löschen, damit playground/ sauber bleibt
