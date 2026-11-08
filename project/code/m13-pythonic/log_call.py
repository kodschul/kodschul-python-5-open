# @log_call: zeigt bei jedem Aufruf Funktionsname, Argumente und Ergebnis
# Dateiname nicht logging.py: das würde das eingebaute Modul logging überdecken

import functools


def log_call(func):
    """Decorator: gibt Name, Argumente und Ergebnis jedes Aufrufs aus."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # nimmt jede Art von Argumenten an
        print(f"Aufruf {func.__name__} mit args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)  # alles unverändert weiterreichen
        print(f"  {func.__name__} gibt {result} zurück")
        return result

    return wrapper


@log_call
def add(a, b):
    """Addiert zwei Zahlen."""
    return a + b


@log_call
def price_with_vat(net, rate=0.19):
    """Bruttopreis aus Nettopreis und Steuersatz."""
    return round(net * (1 + rate), 2)


add(2, 3)
price_with_vat(10)
price_with_vat(10, rate=0.07)
