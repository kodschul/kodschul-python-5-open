# Namen zeigen auf Objekte: id(), is und ==

# Zahl: b = a klebt ein zweites Etikett an dieselbe 5
a = 5
b = a
b = b + 1  # neues Objekt 6, nur b zeigt jetzt darauf
print("a =", a, "| b =", b)

# Liste: zwei Namen, ein Objekt
shopping = ["Milch", "Brot"]
same_list = shopping  # kein Kopieren: zweites Etikett
other_list = ["Milch", "Brot"]  # neues Objekt mit gleichem Inhalt

print("shopping == other_list:", shopping == other_list)  # gleicher Inhalt
print("shopping is other_list:", shopping is other_list)  # nicht dasselbe Objekt
print("shopping is same_list: ", shopping is same_list)  # dasselbe Objekt

print("id:", id(shopping), id(same_list), id(other_list))

same_list.append("Käse")  # ändert das gemeinsame Objekt
print("shopping:  ", shopping)
print("same_list: ", same_list)
print("other_list:", other_list)
