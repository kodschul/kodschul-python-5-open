# Personendatenbank: JSON laden, neue Personen ergänzen, auswerten, speichern

import json
from pathlib import Path

SOURCE_FILE = Path("data") / "persons.json"  # Beispieldaten, bleiben unverändert
TARGET_FILE = Path("playground") / "persons.json"  # eigene Kopie mit Ergänzungen


def load_persons():
    """Lädt die eigene Kopie, beim allerersten Start die Beispieldaten."""
    path = TARGET_FILE if TARGET_FILE.exists() else SOURCE_FILE
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def save_persons(persons):
    """Speichert alle Personen als eingerücktes JSON."""
    with open(TARGET_FILE, "w", encoding="utf-8") as file:
        json.dump(persons, file, indent=2, ensure_ascii=False)


def ask_int(prompt):
    """Fragt so lange, bis eine ganze Zahl eingegeben wird (wie in Lab 7.2)."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Bitte eine ganze Zahl eingeben.")


def ask_person():
    """Fragt eine neue Person ab; gibt None zurück, wenn der Name leer bleibt."""
    name = input("Name (leer = fertig): ").strip()
    if name == "":
        return None
    return {
        "name": name,
        "age": ask_int("Alter: "),
        "height": ask_int("Größe in cm: "),
        "weight": ask_int("Gewicht in kg: "),
    }


def show_averages(persons):
    """Gibt Anzahl und Durchschnittswerte aus."""
    count = len(persons)
    age_sum = 0
    height_sum = 0
    for person in persons:
        age_sum += person["age"]
        height_sum += person["height"]
    print(f"Personen: {count}")
    print(f"Durchschnittsalter: {round(age_sum / count, 1)} Jahre")
    print(f"Durchschnittsgröße: {round(height_sum / count, 1)} cm")


def main():
    """Laden, ergänzen, auswerten, speichern."""
    persons = load_persons()
    print(f"{len(persons)} Personen geladen.")
    while True:
        person = ask_person()
        if person is None:
            break
        persons.append(person)
    show_averages(persons)
    save_persons(persons)
    print("Gespeichert in", TARGET_FILE)


if __name__ == "__main__":
    main()
