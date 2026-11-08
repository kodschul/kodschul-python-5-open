# Dauer messen: Unix-Zeit mit time.time(), Stoppuhr mit time.perf_counter()

import time

print("Sekunden seit dem 01.01.1970 (Unix-Zeit):", round(time.time()))

input("Enter drücken, um die Stoppuhr zu starten ...")
start = time.perf_counter()                # Stoppuhr starten
input("Enter drücken, um sie anzuhalten ...")
seconds = time.perf_counter() - start      # Stoppuhr anhalten: Differenz

print("Rohwert:", seconds)
print(f"Gerundet: {seconds:.1f} s")        # :.1f = eine Nachkommastelle
print("Deutsch:", f"{seconds:.1f}".replace(".", ","), "s")
