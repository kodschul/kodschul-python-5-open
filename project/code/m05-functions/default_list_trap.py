# Falle: Liste als Standardwert wird nur einmal angelegt


# Die leere Liste entsteht einmal beim def, nicht bei jedem Aufruf
def add_tip(tip, tips=[]):  # noqa: B006 (Falle mit Absicht)
    tips.append(tip)
    return tips


print(add_tip(5))
print(add_tip(8))  # erwartet [8], liefert [5, 8]


def add_tip_safe(tip, tips=None):
    """Legt bei jedem Aufruf ohne Liste eine neue Liste an."""
    if tips is None:
        tips = []
    tips.append(tip)
    return tips


print(add_tip_safe(5))
print(add_tip_safe(8))  # [8]
