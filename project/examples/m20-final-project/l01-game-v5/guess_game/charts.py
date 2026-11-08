# Diagramme: wertet die Runden aus game.db aus und speichert sie als PNG
# Nur die Bilder erzeugen (ohne HTML): python -m guess_game.charts

import sqlite3
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator

from guess_game import storage

plt.switch_backend("Agg")  # nur Bilddateien, nie ein Fenster (auch ohne Bildschirm)

TRIES_CHART = Path("chart_tries.png")  # entstehen im aktuellen Ordner
WIN_RATE_CHART = Path("chart_win_rate.png")
TRIES_TITLE = "Versuche bis zum Gewinn"
WIN_RATE_TITLE = "Gewinnquote pro Stufe"

# feste Farbe pro Stufe, damit leicht in jedem Diagramm gleich aussieht
COLORS = {"leicht": "#2a78d6", "mittel": "#eb6834", "schwer": "#1baf7a"}


def load_rounds(path=storage.DB_FILE):
    """Lädt alle Runden aus der Tabelle rounds als DataFrame."""
    connection = sqlite3.connect(path)
    rounds = pd.read_sql("SELECT * FROM rounds", connection)
    connection.close()
    return rounds


def save_tries_chart(rounds, path=TRIES_CHART):
    """Histogramm: Wie viele Versuche brauchten die Gewinne, je Stufe?"""
    won = rounds[rounds["won"] == 1]  # nur gewonnene Runden
    levels = sorted(won["level"].unique())  # leicht, mittel, schwer
    data = [won[won["level"] == level]["tries"] for level in levels]
    colors = [COLORS.get(level, "gray") for level in levels]  # neue Stufe: grau
    bins = range(1, rounds["tries"].max() + 2)  # ein Balken pro Versuchszahl
    fig, ax = plt.subplots(figsize=(7, 4))  # Figure = Bild, Axes = Diagramm
    ax.hist(data, bins=bins, align="left", color=colors, label=levels)
    ax.set_title(TRIES_TITLE)
    ax.set_xlabel("Versuche")
    ax.set_ylabel("Runden")
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))  # nur ganze Zahlen
    ax.legend(title="Stufe")
    fig.savefig(path, dpi=100)
    plt.close(fig)  # Speicher freigeben
    return path


def save_win_rate_chart(rounds, path=WIN_RATE_CHART):
    """Balkendiagramm: Anteil gewonnener Runden pro Stufe in Prozent."""
    rates = rounds.groupby("level")["won"].mean() * 100  # wie in analyze.py
    fig, ax = plt.subplots(figsize=(7, 4))
    bars = ax.bar(rates.index, rates.values, color=COLORS["leicht"])
    ax.bar_label(bars, fmt="%.0f %%")  # Wert über jedem Balken, z. B. 75 %
    ax.set_title(WIN_RATE_TITLE)
    ax.set_xlabel("Stufe")
    ax.set_ylabel("gewonnen in %")
    ax.set_ylim(0, 110)  # Platz für die Beschriftung über 100 %
    fig.savefig(path, dpi=100)
    plt.close(fig)
    return path


def save_charts(rounds):
    """Speichert beide Diagramme; gibt [(Datei, Titel), ...] zurück.

    Ohne gewonnene Runde gibt es nichts zu zeigen: leere Liste.
    """
    if rounds["won"].sum() == 0:
        return []
    return [
        (save_tries_chart(rounds), TRIES_TITLE),
        (save_win_rate_chart(rounds), WIN_RATE_TITLE),
    ]


if __name__ == "__main__":  # python -m guess_game.charts
    for path, title in save_charts(load_rounds()):
        print(f"Diagramm gespeichert: {path} ({title})")
