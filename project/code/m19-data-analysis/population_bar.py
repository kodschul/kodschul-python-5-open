# Einwohner pro Stadtteil als Balkendiagramm (erfundene Stadt, data/population.csv)
# Start im Ordner project/: python code/m19-data-analysis/population_bar.py
# Ergebnis: population_bar.png und population_compare.png im aktuellen Ordner

import matplotlib.pyplot as plt
import pandas as pd

plt.switch_backend("Agg")

population = pd.read_csv("data/population.csv")
population = population.sort_values("Einwohner_2025", ascending=False)

# 1. Balkendiagramm Schritt für Schritt
fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(population["Stadtteil"], population["Einwohner_2025"], color="#2a78d6")
ax.bar_label(bars)  # Zahl über jedem Balken
ax.set_title("Einwohner pro Stadtteil 2025")
ax.set_xlabel("Stadtteil")
ax.set_ylabel("Einwohner")
ax.tick_params(axis="x", labelrotation=30)  # lange Namen schräg stellen
fig.tight_layout()
fig.savefig("population_bar.png", dpi=100)
plt.close(fig)
print("Gespeichert: population_bar.png")

# 2. Abkürzung DataFrame.plot: pandas ruft matplotlib selbst auf
ax = population.plot(
    x="Stadtteil",
    y=["Einwohner_2015", "Einwohner_2025"],
    kind="bar",
    rot=30,  # Beschriftung der x-Achse um 30 Grad drehen
    figsize=(8, 4),
    title="Einwohner 2015 und 2025",
)
ax.set_ylabel("Einwohner")
ax.figure.tight_layout()
ax.figure.savefig("population_compare.png", dpi=100)
plt.close(ax.figure)
print("Gespeichert: population_compare.png")
