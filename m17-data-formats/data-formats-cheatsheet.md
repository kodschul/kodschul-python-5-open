# Cheatsheet Modul 17: Datenformate

## Welches Format wofür?

| Format | Einsatz |
| --- | --- |
| JSON (Lab 8.2) | Daten speichern und austauschen, Web-APIs |
| CSV (Lab 8.3) | einfache Tabellen, Austausch mit Excel |
| XML (Lab 17.1) | Konfiguration, Office-Dateien, ältere Schnittstellen |
| HTML (Lab 17.1) | Webseiten, Berichte zum Ansehen im Browser |
| `.xlsx` (Lab 17.2) | Tabellen mit Formatierung, Formeln, mehreren Blättern |
| pickle (Lab 17.3) | eigene Python-Objekte kurz zwischenspeichern, nur eigene Dateien laden |

## XML lesen mit ElementTree (Lab 17.1)

| Befehl | Wirkung |
| --- | --- |
| `import xml.etree.ElementTree as ET` | Modul laden (Standardbibliothek) |
| `root = ET.parse(pfad).getroot()` | Datei lesen, Wurzelelement holen |
| `element.tag` | Name des Elements |
| `element.text` | Text zwischen den Tags, immer `str` |
| `element.get("name")` | Wert eines Attributs, sonst `None` |
| `element.attrib` | alle Attribute als Dictionary |
| `element.find("low")` | erstes direktes Kind mit diesem Namen, sonst `None` |
| `element.findall("level")` | alle direkten Kinder mit diesem Namen |
| `element.iter("amount")` | alle Elemente mit diesem Namen im ganzen Baum |

## XML schreiben (Lab 17.1)

| Befehl | Wirkung |
| --- | --- |
| `root = ET.Element("shopping_list", owner="Anna")` | Wurzel mit Attribut anlegen |
| `item = ET.SubElement(root, "item", name="Milch")` | Kind anhängen |
| `item.text = str(3)` | Text setzen (immer `str`) |
| `ET.indent(root)` | einrücken für Menschen |
| `ET.ElementTree(root).write(pfad, encoding="utf-8", xml_declaration=True)` | speichern |
| `defusedxml` (PyPI) | abgesicherte Variante für XML aus fremden Quellen |

## HTML lesen mit BeautifulSoup (Lab 17.1)

| Befehl | Wirkung |
| --- | --- |
| `from bs4 import BeautifulSoup` | Paket `beautifulsoup4` laden |
| `soup = BeautifulSoup(file, "html.parser")` | HTML parsen |
| `soup.title.get_text()` | Titel der Seite |
| `soup.find("h2")` | erstes `<h2>`, sonst `None` |
| `soup.find_all("div", class_="product")` | alle `<div>` mit dieser Klasse |
| `soup.select("div.product .price")` | alle Elemente zum CSS-Selektor |
| `soup.select_one(".price")` | erstes Element zum CSS-Selektor |
| `tag.get_text(strip=True)` | Text ohne Leerzeichen am Rand |
| `tag.get("href")` | Wert eines Attributs |

## HTML schreiben (Lab 17.1)

| Befehl | Wirkung |
| --- | --- |
| `<!DOCTYPE html>`, `<html lang="de">`, `<meta charset="utf-8">` | Grundgerüst einer Seite |
| `<table>`, `<tr>`, `<th>`, `<td>` | Tabelle, Zeile, Kopfzelle, Zelle |
| `<td colspan="7">` | Zelle über sieben Spalten |
| `html.escape(text)` | `<`, `>`, `&` als Text statt als Tag |
| `"/".join(liste)` | Strings mit `/` verbinden: `"leicht/mittel/schwer"` |

## Pfade (Lab 17.1)

| Befehl | Wirkung |
| --- | --- |
| `Path("data") / "x.html"` | relativ zum Ordner des Terminals |
| `Path(__file__)` | Pfad der aktuellen `.py`-Datei |
| `Path(__file__).parent / "levels.xml"` | Datei neben dem Modul, egal wo das Terminal steht |
| `dictionary.get(schlüssel)` | Wert oder `None` statt `KeyError` |

## Excel mit openpyxl (Lab 17.2)

| Befehl | Wirkung |
| --- | --- |
| `from openpyxl import Workbook, load_workbook` | Paket `openpyxl` laden |
| `from openpyxl.styles import Font` | Schriftangaben |
| `workbook = load_workbook(pfad)` | vorhandene Datei laden |
| `load_workbook(pfad, data_only=True)` | Formelergebnisse statt Formeln (von Excel gespeichert) |
| `workbook = Workbook()` | neue Mappe mit einem Blatt |
| `workbook.sheetnames` / `workbook.active` | Blattnamen / aktives Blatt |
| `workbook["Einkauf"]` | Blatt über seinen Namen |
| `sheet.title = "Bestenliste"` | Blatt umbenennen |
| `sheet["B2"].value` | Zellwert lesen |
| `sheet["D7"] = "=SUM(D2:D6)"` | Wert oder Formel schreiben (Excel rechnet beim Öffnen) |
| `sheet.append([1, "Anna", 5])` | neue Zeile unten anhängen |
| `sheet[1]` | Zellen der Zeile 1 |
| `sheet.iter_rows(values_only=True)` | alle Zeilen als Tupel von Werten |
| `sheet.max_row`, `sheet.dimensions` | letzte Zeile, Bereich wie `"A1:C6"` |
| `cell.font = Font(bold=True)` | Zelle fett |
| `sheet.column_dimensions["B"].width = 14` | Spaltenbreite |
| `workbook.save(pfad)` | speichern; nie über die Originaldatei |
| `python -m zipfile -l datei.xlsx` | Inhalt des ZIP-Pakets anzeigen |

## pickle (Lab 17.3)

| Befehl | Wirkung |
| --- | --- |
| `import pickle` | Modul laden (Standardbibliothek) |
| `with open(pfad, "wb") as file: pickle.dump(obj, file)` | Objekt in Binärdatei speichern |
| `with open(pfad, "rb") as file: obj = pickle.load(file)` | Objekt laden; **nur eigene Dateien** |
| `def __getstate__(self):` | festlegen, was `pickle` speichert |
| `self.__dict__.copy()` | Kopie aller Attribute als Dictionary |
| `path.unlink()` | Datei löschen |

## Eigene Objekte als JSON (Lab 17.3)

| Befehl | Wirkung |
| --- | --- |
| `asdict(obj)` | Dataclass → Dictionary (Lab 11.2) |
| `json.dump(daten, file, default=str)` | Unbekanntes (z. B. `datetime`) als Text speichern |
| `datetime.fromisoformat(text)` | Text `"2026-11-08 15:30:00"` → `datetime` |

## Im Spiel (Stand Lab 17.3)

| Befehl | Wirkung |
| --- | --- |
| `guess_game/levels.xml` | Stufen; neue Stufe = neues `<level>`-Element |
| `python -m guess_game --export html` | Bestenliste als `highscores.html` |
| `python -m guess_game --export excel` | Bestenliste als `highscores.xlsx` |
| Tipp: `speichern` | laufendes Spiel in `savegame.pkl`, Spiel endet |
| `python -m guess_game --resume` | gespeichertes Spiel einmal fortsetzen |
