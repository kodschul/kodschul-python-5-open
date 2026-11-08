# deque: Warteschlange mit fester Länge; namedtuple: Tupel mit Feldnamen

from collections import deque, namedtuple

# Die letzten drei Tipps merken: ein neuer Wert schiebt den ältesten hinaus
last_tips = deque(maxlen=3)
for tip in [50, 25, 37, 31, 34]:
    last_tips.append(tip)
    print(f"Tipp {tip} -> letzte drei: {list(last_tips)}")

# namedtuple: wie ein Tupel aus Lab 4.2, aber jedes Feld hat einen Namen
Point = namedtuple("Point", ["x", "y"])
start = Point(3, 4)
print(start)  # Point(x=3, y=4)
print("x =", start.x, "| y =", start[1])  # per Name oder per Index
x, y = start  # entpacken wie ein normales Tupel
print("entpackt:", x, y)
