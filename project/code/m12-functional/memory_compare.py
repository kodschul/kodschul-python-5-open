# Speicher messen: Liste (Lagerhalle) gegen Generator (Förderband)

import sys
import tracemalloc  # Standardbibliothek: misst, wie viel Speicher Python belegt

COUNT = 1_000_000  # Unterstriche nur zur Lesbarkeit: eine Million

squares_list = [n * n for n in range(COUNT)]  # alle Werte sofort berechnet
squares_gen = (n * n for n in range(COUNT))  # berechnet erst auf Anfrage
# sys.getsizeof: Größe eines Objekts in Bytes (ohne die Zahlen darin)
print("Größe der Liste:     ", sys.getsizeof(squares_list), "Bytes")
print("Größe des Generators:", sys.getsizeof(squares_gen), "Bytes")

tracemalloc.start()
total_list = sum([n * n for n in range(COUNT)])  # eckige Klammern: erst Liste
peak_list = tracemalloc.get_traced_memory()[1]  # [1] = Höchstwert in Bytes
tracemalloc.stop()

tracemalloc.start()
total_gen = sum(n * n for n in range(COUNT))  # runde Klammern: Wert für Wert
peak_gen = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print("Gleiche Summe?", total_list == total_gen)
print("Höchster Speicher mit Liste:    ", round(peak_list / 1000), "KB")
print("Höchster Speicher mit Generator:", round(peak_gen / 1000), "KB")
