# Datum und Uhrzeit: jetzt, rechnen, formatieren, einlesen

from datetime import date, datetime, timedelta

now = datetime.now()                       # Datum + Uhrzeit, jetzt
today = date.today()                       # nur das Datum
print("Jetzt (Python-Darstellung):", now)
print("Heute:", today)

# Formatieren: Datum -> Text in einem gewünschten Format
print("Deutsch:", now.strftime("%d.%m.%Y, %H:%M Uhr"))
print("ISO-Format:", today.isoformat())

# Rechnen: Datum + Zeitspanne, Datum - Datum
in_two_weeks = today + timedelta(days=14)
print("In zwei Wochen:", in_two_weeks.strftime("%d.%m.%Y"))

exam = date(2027, 2, 15)
print("Tage bis zur Prüfung am 15.02.2027:", (exam - today).days)

# Schaltjahr: 2028 hat einen 29. Februar
span = date(2028, 3, 1) - date(2028, 2, 1)
print("Februar 2028 hat", span.days, "Tage")

# Einlesen: Text -> Datum (Format muss genau passen)
deadline = datetime.strptime("03.04.2026", "%d.%m.%Y")
print("Eingelesen:", deadline.date(), "| Monat:", deadline.month)
