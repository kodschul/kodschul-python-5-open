# Was passiert beim Übergeben? Zahl (unveränderlich) vs. Liste (veränderbar)


def add_bonus(points):
    """Erhöht points um 10, aber nur innerhalb der Funktion."""
    points = points + 10  # neues Objekt, nur der lokale Name zeigt darauf
    print("  in add_bonus:", points)


def add_guess(guesses):
    """Hängt 7 an die übergebene Liste an."""
    guesses.append(7)  # ändert das Objekt, auf das auch tips zeigt
    print("  in add_guess:", guesses)


score = 50
add_bonus(score)
print("score danach:", score)

tips = [5, 8]
add_guess(tips)
print("tips danach: ", tips)
