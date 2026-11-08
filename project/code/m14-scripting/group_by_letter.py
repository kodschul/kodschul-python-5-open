# Wörter nach Anfangsbuchstaben gruppieren: erst mit if, dann mit defaultdict

from collections import defaultdict

WORDS = ["kaffee", "pause", "kurz", "vorlesung", "stark", "pizza", "skript"]

# 1) Von Hand: fehlende Liste erst anlegen
groups = {}
for word in WORDS:
    letter = word[0]
    if letter not in groups:
        groups[letter] = []
    groups[letter].append(word)
print("Dictionary:", groups)

# 2) defaultdict(list): fehlender Schlüssel bekommt automatisch eine leere Liste
groups = defaultdict(list)
for word in WORDS:
    groups[word[0]].append(word)
print("defaultdict:", dict(groups))  # dict(...) nur für eine kürzere Ausgabe

for letter in sorted(groups):
    print(f"  {letter}: {groups[letter]}")
