# sys.argv: die Wörter hinter dem Skriptnamen, als Liste von Strings
# Start: python code/m14-scripting/argv_demo.py Anna 3

import sys

print("sys.argv:", sys.argv)  # [0] ist immer der Skriptname

if len(sys.argv) < 2:  # kein Name angegeben
    print("Aufruf: python code/m14-scripting/argv_demo.py <name> [anzahl]")
    sys.exit(1)  # Exit-Code 1 = Fehler

name = sys.argv[1]
times = 1
if len(sys.argv) > 2:
    times = int(sys.argv[2])  # alles kommt als Text an, Zahl selbst umwandeln

for number in range(times):
    print(f"{number + 1}. Hallo, {name}!")
