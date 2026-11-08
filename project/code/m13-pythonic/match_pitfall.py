# Absichtlich fehlerhaft: ein bloßer Name hinter case fängt jeden Wert ein

command = "hilfe"

match command:
    case quit:  # kein Vergleich mit "quit", sondern: quit = command
        print("Spiel beendet")
    case "hilfe":
        print("Befehle: hilfe, quit")
