# Drei Diagrammarten in einem Bild: Linie, Balken, Histogramm
# Start im Ordner project/: python code/m19-data-analysis/chart_types.py
# Ergebnis: chart_types.png im aktuellen Ordner

import matplotlib.pyplot as plt

plt.switch_backend("Agg")  # nur Bilddateien speichern, kein Fenster öffnen

days = ["Mo", "Di", "Mi", "Do", "Fr"]
temperatures = [12, 14, 11, 15, 17]
fruits = ["Äpfel", "Birnen", "Kiwis"]
sold = [30, 12, 21]
tries = [3, 4, 4, 5, 2, 4, 6, 3, 4, 5, 4, 3, 7, 4, 5]  # Versuche pro Spiel

# Figure = das ganze Bild, Axes = ein Diagramm darin; hier 1 Zeile, 3 Diagramme
fig, (ax_line, ax_bar, ax_hist) = plt.subplots(1, 3, figsize=(12, 3.6))

ax_line.plot(days, temperatures, marker="o")  # Linie: Verlauf über die Zeit
ax_line.set_title("Linie: Temperatur")
ax_line.set_ylabel("°C")

ax_bar.bar(fruits, sold, color="#eb6834")  # Balken: Kategorien vergleichen
ax_bar.set_title("Balken: Verkauf")
ax_bar.set_ylabel("Stück")

ax_hist.hist(tries, bins=range(1, 9), align="left", color="#1baf7a")  # Verteilung
ax_hist.set_title("Histogramm: Versuche")
ax_hist.set_xlabel("Versuche")
ax_hist.set_ylabel("Spiele")

fig.tight_layout()  # Abstände automatisch, nichts überlappt
fig.savefig("chart_types.png", dpi=100)
plt.close(fig)
print("Gespeichert: chart_types.png")
