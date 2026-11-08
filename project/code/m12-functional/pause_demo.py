# yield pausiert: die Generatorfunktion läuft immer nur bis zum nächsten yield


def steps():
    print("  [Generator] Schritt 1 vorbereiten")
    yield 1
    print("  [Generator] Schritt 2 vorbereiten")
    yield 2
    print("  [Generator] fertig, gleich kommt StopIteration")


gen = steps()  # noch läuft keine Zeile der Funktion
print("Generator erzeugt:", gen)
print("next ->", next(gen))
print("Hauptprogramm macht etwas anderes ...")
print("next ->", next(gen))
for value in gen:  # holt den Rest; nichts mehr da, die Schleife endet sofort
    print("nie erreicht", value)
print("Ende")
