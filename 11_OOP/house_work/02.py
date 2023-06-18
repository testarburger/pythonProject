class Człowiek:
    def __init__(self, imię, wiek):
        self.imię = imię
        self.wiek = wiek

    def opis(self):
        print("Jestem człowiekiem.")
        print("Imię:", self.imię)
        print("Wiek:", self.wiek)


class Ssaki(Człowiek):
    def __init__(self, imię, wiek, gatunek):
        super().__init__(imię, wiek)
        self.gatunek = gatunek

    def opis(self):
        super().opis()
        print("Jestem ssakiem.")
        print("Gatunek:", self.gatunek)


ssak = Ssaki("Wilk", 5, "Canis lupus")

ssak.opis()
