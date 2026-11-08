# Warum .*? mit re.DOTALL bei Logs zu viel findet: eine Runde ohne Ergebnis
# Start im Ordner project/: python code/m19-data-analysis/log_blocks.py

import re

# vereinfachtes Log: die mittlere Runde wurde abgebrochen (kein ENDE)
LOG = """\
START leicht
Tipp 5
Tipp 8
ENDE gewonnen Anna
START mittel
Tipp 20
START schwer
Tipp 50
Tipp 75
ENDE gewonnen Ben
"""

# Variante 1: alles zwischen START und ENDE, . passt auch auf \n
LOOSE = re.compile(
    r"^START (?P<level>\w+)\n(?P<body>.*?)ENDE (?P<result>\w+) (?P<name>\w+)$",
    re.MULTILINE | re.DOTALL,
)
# Variante 2: dazwischen nur Tipp-Zeilen, sonst kein Treffer an dieser Stelle
STRICT = re.compile(
    r"^START (?P<level>\w+)\n"
    r"(?P<body>(?:Tipp .*\n)*?)"  # nur Tipp-Zeilen, so wenige wie möglich
    r"ENDE (?P<result>\w+) (?P<name>\w+)$",
    re.MULTILINE,
)

for title, pattern in [("DOTALL .*?", LOOSE), ("nur Tipp-Zeilen", STRICT)]:
    print(f"{title}:")
    for match in pattern.finditer(LOG):
        lines = match.group().count("\n") + 1
        print(f"  {match.group('level')} · {match.group('name')} · {lines} Zeilen")
