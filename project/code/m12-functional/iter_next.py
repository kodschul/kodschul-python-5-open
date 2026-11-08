# Was for intern macht: iter() holt einen Iterator, next() das nächste Element

tips = [5, 8, 10]

iterator = iter(tips)  # Iterator: merkt sich, wo er gerade steht
print(next(iterator))  # 5
print(next(iterator))  # 8
print(next(iterator))  # 10

# for macht genau das und fängt das Ende (StopIteration) selbst ab
iterator = iter(tips)
while True:
    try:
        tip = next(iterator)
    except StopIteration:  # keine Elemente mehr: Schleife beenden
        print("StopIteration: Liste zu Ende")
        break
    print("Tipp:", tip)

# Kurzform mit for: dasselbe in zwei Zeilen
for tip in tips:
    print("for:", tip)
