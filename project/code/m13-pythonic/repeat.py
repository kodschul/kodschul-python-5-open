# Decorator mit Parameter: @repeat(times=3) ruft die Funktion mehrmals auf

import functools


def repeat(times):
    """Gibt einen Decorator zurück, der func times-mal aufruft."""

    def decorator(func):  # Ebene 2: der eigentliche Decorator
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # Ebene 3: läuft bei jedem Aufruf
            for _ in range(times):  # _: Zählvariable wird nicht gebraucht
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(times=3)  # erst repeat(times=3) aufrufen, das Ergebnis ist der Decorator
def cheer(name):
    """Feuert eine Person an."""
    print(f"Los, {name}!")


cheer("Anna")
