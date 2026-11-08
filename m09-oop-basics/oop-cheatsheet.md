# OOP-Cheatsheet

Schnellreferenz für Modul 9 (Klassen, Objekte, Kapselung, Properties).

## Begriffe

| Begriff | Bedeutung |
| --- | --- |
| Klasse | Bauplan: was jedes Objekt weiß und kann |
| Objekt (Instanz) | nach dem Bauplan gebautes Ding mit eigenen Werten |
| Attribut | Wert eines Objekts („weiß“) |
| Methode | Funktion eines Objekts („kann“) |
| `self` | das Objekt vor dem Punkt, erster Parameter jeder Methode |
| Kapselung | Daten nur über Methoden der Klasse ändern |

## Klasse schreiben

| Syntax | Wirkung |
| --- | --- |
| `class BankAccount:` | Klasse anlegen, Name in CamelCase |
| `def __init__(self, owner):` | Startwerte setzen; läuft beim Erzeugen automatisch |
| `self.owner = owner` | Instanzattribut anlegen |
| `self.grades = []` | eigene, leere Liste für jedes Objekt |
| `currency = "€"` (im Klassenblock) | Klassenattribut: gilt für alle Objekte |
| `def deposit(self, amount):` | Methode; `self` immer zuerst |
| `self.balance += amount` | Attribut in einer Methode ändern |
| `self.is_over()` | andere Methode desselben Objekts aufrufen |

## Objekte benutzen

| Syntax | Wirkung |
| --- | --- |
| `account = BankAccount("Anna")` | Objekt erzeugen, ruft `__init__` auf |
| `account.deposit(100)` | Methode aufrufen; Python setzt `account` als `self` ein |
| `account.owner` | Attribut lesen |
| `account.owner = "Cem"` | Attribut ändern (nur bei öffentlichen Attributen sinnvoll) |
| `BankAccount.currency` | Klassenattribut über die Klasse lesen |
| `accounts = [alice, bob]` | Objekte in einer Liste sammeln |
| `for account in accounts:` | alle Objekte durchlaufen |
| `type(account)` | Klasse des Objekts: `<class '__main__.BankAccount'>` |
| `print(account)` | ohne Weiteres nur `<__main__.BankAccount object at 0x…>` |

## Sichtbarkeit

| Schreibweise | Bedeutung |
| --- | --- |
| `self.owner` | öffentlich: lesen und ändern erlaubt |
| `self._max_tries` | intern (Konvention): von außen nicht benutzen |
| `self.__secret` | privat: von außen unter diesem Namen nicht erreichbar |
| `game._Game__secret` | Umweg nach der Namensverschleierung; nie im echten Code |
| `game.__secret = 99` (von außen) | legt nur ein neues Attribut an, ändert nichts |

## Properties

| Syntax | Wirkung |
| --- | --- |
| `@property` über `def balance(self):` | Methode lesbar wie ein Attribut: `account.balance` |
| Property ohne Setter | schreibgeschützt; Zuweisung → `AttributeError … has no setter` |
| `@owner.setter` über `def owner(self, name):` | jede Zuweisung `account.owner = …` läuft durch diese Methode |
| `raise ValueError("…")` im Setter oder in einer Methode | ungültigen Wert ablehnen |
| `account.balance` | Property lesen, **ohne** `()` |

## Statt Überladung

| Syntax | Wirkung |
| --- | --- |
| `def __init__(self, owner, balance=0):` | Standardwert ersetzt einen zweiten Konstruktor |
| `BankAccount("Cem")` | `balance` ist 0 |
| `BankAccount("Anna", 100)` | `balance` ist 100 |

## Im Spiel (Stand Lab 9.3)

| Code | Wirkung |
| --- | --- |
| `game = logic.Game(name, level)` | ein neues Spiel pro Runde |
| `hint = game.guess(5)` | `"zu hoch"`, `"zu niedrig"`, `"richtig"` oder `"schon getippt"` |
| `game.is_over()` | Methode: Runde vorbei? |
| `game.is_won` | Property: gewonnen? |
| `game.attempts_left` | Property: verbleibende Versuche, nur lesbar |
| `game.reveal_secret()` | Geheimzahl, erst nach Spielende, sonst `None` |
| `game.result()` | Ergebnis-Dictionary für Bestenliste und `history.csv` |

## Typische Fehlermeldungen

| Meldung | Ursache |
| --- | --- |
| `takes 1 positional argument but 2 were given` | `self` in der Methode vergessen |
| `missing 1 required positional argument` | beim Erzeugen ein Argument vergessen |
| `Student() takes no arguments` | `__init__` falsch geschrieben |
| `object has no attribute '…'` | Attribut nie mit `self.` angelegt oder privat |
| `'int' object is not callable` | Property mit `()` aufgerufen |
| `property '…' of '…' object has no setter` | Zuweisung an nur lesbare Property |
