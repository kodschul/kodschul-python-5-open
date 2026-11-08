# NumPy-Array vs. Liste: Rechnen mit ganzen Zahlenreihen auf einmal
# Start im Ordner project/: python code/m19-data-analysis/numpy_basics.py

import time

import numpy as np  # Kurzname np ist überall üblich

prices = [1.99, 0.89, 4.99, 0.45]  # Liste
array = np.array(prices)  # Array aus der Liste: alle Werte vom selben Typ

# 1. Vektorrechnung: eine Rechnung gilt für jedes Element
print("Liste * 2:", prices * 2)  # Liste wird verdoppelt (aneinandergehängt)
print("Array * 2:", array * 2)  # jeder Wert wird verdoppelt
print("Brutto:   ", (array * 1.19).round(2))  # 19 % auf jeden Preis
print("Array + Array:", np.array([1, 2, 3]) + np.array([10, 20, 30]))

# 2. Statistik direkt am Array
print("Summe:", array.sum().round(2), "· Mittelwert:", array.mean().round(2))
print("Median:", np.median(array), "· Max:", array.max(), "· dtype:", array.dtype)

# 3. Geschwindigkeit: eine Million Zahlen addieren
numbers = list(range(1_000_000))  # _ trennt Tausender, nur zur Lesbarkeit
numbers_array = np.arange(1_000_000)  # wie range, aber als Array

start = time.perf_counter()
total = 0
for number in numbers:
    total += number
loop_time = time.perf_counter() - start

start = time.perf_counter()
total_sum = sum(numbers)
sum_time = time.perf_counter() - start

start = time.perf_counter()
total_np = numbers_array.sum()
numpy_time = time.perf_counter() - start

print(f"\nSchleife:   {loop_time * 1000:.1f} ms  (Ergebnis {total})")
print(f"sum(liste): {sum_time * 1000:.1f} ms  (Ergebnis {total_sum})")
print(f"NumPy:      {numpy_time * 1000:.1f} ms  (Ergebnis {total_np})")
