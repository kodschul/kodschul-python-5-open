# Timer als Klasse: misst, wie lange der with-Block dauert

import time


class Timer:
    """Context Manager: Stoppuhr für den Inhalt des with-Blocks."""

    def __init__(self, label):
        self.label = label
        self.seconds = 0.0

    def __enter__(self):
        self.start = time.perf_counter()  # Stoppuhr starten
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.seconds = time.perf_counter() - self.start  # Stoppuhr anhalten
        print(f"{self.label}: {self.seconds:.1f} s".replace(".", ","))
        return False


with Timer("Kaffee kochen"):
    time.sleep(0.3)  # 0,3 Sekunden warten, steht für echte Arbeit

with Timer("Summe bis 10 Millionen") as timer:
    total = sum(range(10_000_000))
print("Ergebnis:", total, "| gemessen:", round(timer.seconds, 2), "s")
