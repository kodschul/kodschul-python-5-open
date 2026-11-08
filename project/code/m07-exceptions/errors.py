# try, except, else und finally an drei Divisionen (Lab 7.2)

pairs = [("10", "4"), ("10", "0"), ("zehn", "2")]

for a_text, b_text in pairs:
    print(f"--- {a_text} / {b_text}")
    try:
        result = int(a_text) / int(b_text)
    except ZeroDivisionError:
        print("Durch 0 teilen geht nicht.")
    except ValueError as error:  # error enthält die Meldung von Python
        print(f"Keine ganze Zahl: {error}")
    else:  # nur ohne Fehler
        print(f"Ergebnis: {result}")
    finally:  # immer, mit und ohne Fehler
        print("Rechnung beendet.")
