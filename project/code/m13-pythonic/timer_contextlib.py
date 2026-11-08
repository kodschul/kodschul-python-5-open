# Timer mit contextlib.contextmanager: eine Generatorfunktion statt einer Klasse

import time
from contextlib import contextmanager


@contextmanager  # macht aus der Generatorfunktion einen Context Manager
def timer(label):
    """Stoppuhr: alles vor yield ist __enter__, alles danach __exit__."""
    start = time.perf_counter()
    try:
        yield  # hier läuft der with-Block
    finally:  # auch nach einem Fehler im Block
        seconds = time.perf_counter() - start
        print(f"{label}: {seconds:.1f} s".replace(".", ","))


with timer("Kaffee kochen"):
    time.sleep(0.3)

try:
    with timer("Tee kochen"):
        time.sleep(0.2)
        raise ValueError("Wasser alle")
except ValueError as error:
    print("abgefangen:", error)
