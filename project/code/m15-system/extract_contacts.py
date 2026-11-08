# Lab 15.2: Telefonnummern und Datumsangaben aus einem Text herauslösen
# Alle Namen und Nummern sind erfunden.
import re

TEXT = """Protokoll Lerngruppe Statistik
Treffen am 12.11.2026 in Raum B204, nächstes Treffen am 3.12.2026.
Kontakt: Anna 0221 4710123, Ben +49 30 23125456, Clara (0221) 4710987.
Abgabe der Hausarbeit bis 15.1.2027, Rückfragen an Ben: 030/23125-789."""

# Telefonnummer: optional + oder (, dann eine Ziffer, dann mindestens fünf
# Zeichen aus Ziffern, Leerzeichen, / ( ) -, am Ende wieder eine Ziffer
PHONE_PATTERN = re.compile(r"[+(]?\d[\d /()-]{5,}\d")

# Datum T.M.JJJJ mit benannten Gruppen: (?P<name>...)
DATE_PATTERN = re.compile(r"(?P<day>\d{1,2})\.(?P<month>\d{1,2})\.(?P<year>\d{4})")

print("Telefonnummern:")
for number in PHONE_PATTERN.findall(TEXT):
    digits = re.sub(r"\D", "", number)  # \D = alles außer Ziffern -> weg
    print(f"  {number}  ->  {digits}")

print("Datumsangaben:")
for match in DATE_PATTERN.finditer(TEXT):  # finditer: ein Match-Objekt je Treffer
    day = match.group("day").zfill(2)  # "3" -> "03"
    month = match.group("month").zfill(2)
    print(f"  {match.group()}  ->  {match.group('year')}-{month}-{day}")

print("Anonymisiert:")
print(PHONE_PATTERN.sub("[Nummer]", TEXT))
