# Warum Umlaute kaputt aussehen: mit einer anderen Kodierung gelesen

from pathlib import Path

sample = Path("playground") / "umlaut.txt"
sample.write_text("Grüße aus Köln", encoding="utf-8")

print("Gelesen mit utf-8: ", sample.read_text(encoding="utf-8"))
# cp1252: alte Windows-Kodierung, liest die UTF-8-Bytes falsch
print("Gelesen mit cp1252:", sample.read_text(encoding="cp1252"))
