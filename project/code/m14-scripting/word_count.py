# Wörter zählen: erst mit einem normalen Dictionary, dann mit Counter

from collections import Counter

TEXT = """Der Kaffee ist heiß. Der Kaffee ist stark.
Die Vorlesung ist lang, die Pause ist kurz, der Kaffee ist leer."""

# Text aufräumen: klein schreiben, Satzzeichen entfernen, in Wörter teilen
words = TEXT.lower().replace(".", "").replace(",", "").split()
print("Wörter im Text:", len(words))

# 1) Von Hand: jedes Wort prüfen, ob es schon einen Zähler hat
counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print("Dictionary:", counts)

# 2) Mit Counter: eine Zeile, Ergebnis wie ein Dictionary
counter = Counter(words)
print("Counter:   ", counter)
print("Wie oft 'kaffee'?", counter["kaffee"])
print("Wie oft 'tee'?   ", counter["tee"])  # fehlendes Wort -> 0, kein KeyError
print("Top 3:", counter.most_common(3))  # Liste von (Wort, Anzahl)
