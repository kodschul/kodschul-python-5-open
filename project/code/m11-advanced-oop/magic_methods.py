# Magic Methods: Python ruft sie selbst auf, z. B. bei print() und len()


class PlainPlaylist:
    """Playlist ohne Magic Methods: print zeigt nur Klasse und Speicheradresse."""

    def __init__(self, name, songs):
        self.name = name
        self.songs = songs


class Playlist:
    """Playlist mit __str__, __repr__ und __len__."""

    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __str__(self):
        """Lesbarer Text für Menschen: print(), str(), f-Strings."""
        return f"Playlist {self.name} mit {len(self.songs)} Songs"

    def __repr__(self):
        """Eindeutiger Text für Entwickler: REPL, Listen, repr()."""
        return f"Playlist('{self.name}', {self.songs})"

    def __len__(self):
        """Antwort auf len(playlist): die Anzahl der Songs."""
        return len(self.songs)


plain = PlainPlaylist("Lernen", ["Lofi 1", "Lofi 2"])
print("Ohne __str__:", plain)
same = PlainPlaylist("Lernen", ["Lofi 1", "Lofi 2"])
print("Ohne __eq__ gleich?", plain == same)  # vergleicht nur: dasselbe Objekt?

party = Playlist("Party", ["Song A", "Song B", "Song C"])
print(party)  # ruft party.__str__() auf
print(f"Gerade läuft: {party}")  # f-String ruft ebenfalls __str__ auf
print(repr(party))  # ruft party.__repr__() auf
print([party])  # in einer Liste zeigt Python repr
print("Anzahl Songs:", len(party))  # ruft party.__len__() auf
