# MRO-Quiz (Lab 10.4): erst Teil 1 lesen und vorhersagen, dann starten

# Teil 1: die Klassen


class Device:
    def info(self):
        return "Device"


class Phone(Device):
    def info(self):
        return "Phone"


class Camera(Device):
    def info(self):
        return "Camera"


class LoggingMixin:
    def log(self, text):
        print(f"[Log] {text}")


class Smartphone(Phone, Camera):
    pass


class CameraPhone(Camera, Phone):
    pass


class LoggingSmartphone(LoggingMixin, Smartphone):
    pass


# Teil 2: Auflösung – erst nach der Vorhersage starten

for cls in [Smartphone, CameraPhone, LoggingSmartphone]:
    names = []
    for parent in cls.__mro__:
        names.append(parent.__name__)
    print(f"{cls.__name__}.__mro__: {names}")
    print(f"  {cls.__name__}().info() → {cls().info()}")
