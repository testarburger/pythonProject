class Pies:
    def __init__(self, imie, kolor, rasa):
        self.imie = imie
        self.kolor = kolor
        self.rasa = rasa

    def szczekaj(self):
        print(f"{self.imie} szczeka: Woof woof!")

    def machaj_ogonem(self):
        print(f"{self.imie} macha ogonem.")


pies1 = Pies("Burek", "brązowy", "mieszaniec")
pies2 = Pies("Azor", "czarny", "owczarek niemiecki")

print(pies1.imie)
print(pies2.rasa)

pies1.szczekaj()
pies2.machaj_ogonem()
