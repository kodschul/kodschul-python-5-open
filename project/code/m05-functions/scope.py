# Gültigkeitsbereiche: lokal, global und das Schlüsselwort global

counter = 0  # global: auf Modulebene angelegt


def show():
    """Liest die globale Variable; Lesen klappt ohne Zusatz."""
    print("show liest counter:", counter)


def try_change():
    """Zuweisung legt eine neue lokale Variable an; die globale bleibt."""
    counter = 99
    print("try_change, lokal:", counter)


def change_global():
    """Ändert die globale Variable mit global (funktioniert, besser vermeiden)."""
    global counter
    counter = counter + 1


def increase(value):
    """Besser: Wert hinein, Ergebnis heraus."""
    return value + 1


show()
try_change()
print("nach try_change:   ", counter)
change_global()
print("nach change_global:", counter)
counter = increase(counter)
print("nach increase:     ", counter)
