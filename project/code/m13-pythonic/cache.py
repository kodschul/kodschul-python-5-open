# functools.cache: merkt sich Ergebnisse, gleiche Argumente rechnen nur einmal

import functools


def fib_slow(n):
    """Fibonacci-Zahl n, ohne Gedächtnis."""
    print(f"  berechne fib_slow({n})")
    if n < 2:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)  # ruft sich selbst auf (Lab 5.3)


@functools.cache  # Ergebnis je Argument merken
def fib_fast(n):
    """Fibonacci-Zahl n, mit Gedächtnis."""
    print(f"  berechne fib_fast({n})")
    if n < 2:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)


print("Ohne Cache:")
print("Ergebnis:", fib_slow(5))
print("Mit Cache:")
print("Ergebnis:", fib_fast(5))
print("Noch einmal mit Cache:")
print("Ergebnis:", fib_fast(5))  # keine Zeile "berechne": kommt aus dem Gedächtnis
