# itertools: fertige Bausteine für Schleifen über Folgen

from itertools import chain, combinations, count, cycle, groupby, islice, product

# count: zählt ohne Ende hoch; islice nimmt nur die ersten Werte
ticket_numbers = count(101)
print("count:       ", list(islice(ticket_numbers, 4)))

# cycle: wiederholt eine Folge ohne Ende (hier: wer ist dran?)
turns = cycle(["Anna", "Ben"])
print("cycle:       ", list(islice(turns, 5)))

# chain: mehrere Listen hintereinander durchlaufen, ohne sie zu verbinden
morning = ["Mathe", "Physik"]
afternoon = ["Python", "Englisch"]
print("chain:       ", list(chain(morning, afternoon)))

# groupby: fasst direkt aufeinanderfolgende gleiche Werte zusammen
results = ["gewonnen", "gewonnen", "verloren", "gewonnen"]
for result, group in groupby(results):
    print("groupby:     ", result, "x", len(list(group)))

# combinations: alle Paare ohne Wiederholung (z. B. Spielpaarungen)
players = ["Anna", "Ben", "Cem"]
print("combinations:", list(combinations(players, 2)))

# product: jede Kombination aus zwei Listen (z. B. Stufe x Spieler)
print("product:     ", list(product(["leicht", "schwer"], ["mensch", "computer"])))
