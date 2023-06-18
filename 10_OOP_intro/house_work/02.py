class Storczyk:
    królestwo_roślin = "Rośliny"

    def __init__(self, kolor, pora_kwitnienia, gatunek):
        self.kolor = kolor
        self.pora_kwitnienia = pora_kwitnienia
        self.gatunek = gatunek

    def przedstaw_sie(self):
        print("Jestem storczykiem.")
        print("Kolor:", self.kolor)
        print("Pora kwitnienia:", self.pora_kwitnienia)
        print("Gatunek:", self.gatunek)


storczyk1 = Storczyk("biały", "wiosna", "Phalaenopsis")
storczyk2 = Storczyk("fioletowy", "lato", "Cattleya")

storczyk1.przedstaw_sie()

storczyk2.przedstaw_sie()

print("Królestwo roślin:", Storczyk.królestwo_roślin)
