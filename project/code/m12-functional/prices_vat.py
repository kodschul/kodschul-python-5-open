# Bruttopreise: erst mit for-Schleife, dann als Listen-Comprehension

net_prices = [10.0, 24.9, 3.5, 120.0]
VAT = 1.19  # 19 % Mehrwertsteuer

# Vorher: leere Liste, Schleife, append
gross_prices = []
for price in net_prices:
    gross_prices.append(round(price * VAT, 2))
print("Schleife:      ", gross_prices)

# Nachher: dieselbe Liste in einer Zeile
gross_prices = [round(price * VAT, 2) for price in net_prices]
print("Comprehension: ", gross_prices)

# Mit Bedingung: nur Preise ab 20 Euro netto
expensive = [round(price * VAT, 2) for price in net_prices if price >= 20]
print("Ab 20 € netto: ", expensive)

# Ausdruck vorne darf alles sein, was einen Wert liefert, z. B. ein f-String
labels = [f"{price:.2f} €".replace(".", ",") for price in gross_prices]
print("Preisschilder: ", labels)

# Vorschau auf Lab 12.3: runde statt eckige Klammern direkt in sum()
total = sum(price * VAT for price in net_prices)
print("Summe brutto:  ", round(total, 2))
