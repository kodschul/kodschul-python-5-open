# Artikel und Preise aus einer lokalen HTML-Seite lesen (BeautifulSoup)
# Start im Ordner project/: python code/m17-data-formats/shop_prices.py
# Nur lokale Datei: keine Anfrage an eine fremde Webseite

from pathlib import Path

from bs4 import BeautifulSoup

PAGE = Path("data") / "shopping_items.html"

with open(PAGE, encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")  # HTML-Text -> Baum aus Tags

print("Titel der Seite:", soup.title.get_text())

# find_all: alle <div>-Tags mit class="product"
products = soup.find_all("div", class_="product")  # class_ mit _, class ist reserviert
print(f"{len(products)} Artikel gefunden")

total = 0
for product in products:
    name = product.find("h2").get_text(strip=True)  # Text ohne Leerzeichen am Rand
    price_text = product.select_one(".price").get_text(strip=True)  # "0,99 €"
    price = float(price_text.replace("€", "").replace(",", ".").strip())
    total += price
    print(f"- {name}: {price:.2f} €".replace(".", ","))
print(f"Summe, je ein Stück: {total:.2f} €".replace(".", ","))

# select: CSS-Selektor wie im Stylesheet, liefert eine Liste
all_prices = [tag.get_text(strip=True) for tag in soup.select("div.product .price")]
print("Alle Preise per select:", all_prices)
