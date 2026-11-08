# Absichtlich fehlerhaft: der vierte next() findet kein Element mehr

tips = [5, 8, 10]
iterator = iter(tips)
print(next(iterator), next(iterator), next(iterator))
print(next(iterator))  # StopIteration: Iterator ist leer
