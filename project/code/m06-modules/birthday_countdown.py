# Tage bis zum nächsten Geburtstag

from datetime import date, datetime

WEEKDAYS = ["Montag", "Dienstag", "Mittwoch", "Donnerstag",
            "Freitag", "Samstag", "Sonntag"]

text = input("Geburtstag (TT.MM.JJJJ): ").strip()
birthday = datetime.strptime(text, "%d.%m.%Y").date()  # Text -> Datum
today = date.today()

# Geburtstag in diesem Jahr; schon vorbei -> nächstes Jahr
next_birthday = birthday.replace(year=today.year)
if next_birthday < today:
    next_birthday = birthday.replace(year=today.year + 1)

days = (next_birthday - today).days        # Datum - Datum = Zeitspanne
weekday = WEEKDAYS[next_birthday.weekday()]  # 0 = Montag, 6 = Sonntag
age = next_birthday.year - birthday.year

if days == 0:
    print(f"Heute ist der {age}. Geburtstag!")
elif days == 1:
    print(f"Morgen ist der {age}. Geburtstag ({weekday}).")
else:
    print(f"Noch {days} Tage bis zum {age}. Geburtstag.")
    print(f"Das ist ein {weekday}, der {next_birthday.strftime('%d.%m.%Y')}.")
