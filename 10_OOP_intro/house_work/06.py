class Pracownik:
    firma = "Love Python Company"

    def __init__(self, stanowisko, wynagrodzenie, imie, nazwisko, staz_pracy, student=False):
        self.stanowisko = stanowisko
        self.wynagrodzenie = wynagrodzenie
        self.imie = imie
        self.nazwisko = nazwisko
        self.staz_pracy = staz_pracy
        self.student = student

    def roczna_podwyzka(self, procent_podwyzki):
        podwyzka = self.wynagrodzenie * procent_podwyzki / 100
        self.wynagrodzenie += podwyzka

    def oblicz_podatek(self):
        if self.wynagrodzenie <= 5000:
            podatek = 0.15 * self.wynagrodzenie
        else:
            podatek = 0.20 * self.wynagrodzenie
        return podatek

    def oblicz_skladke_zdrowotna(self):
        if self.student:
            skladka_zdrowotna = 0
        else:
            skladka_zdrowotna = 0.045 * self.wynagrodzenie
        return skladka_zdrowotna

    def generuj_email(self):
        spolgloski = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        imie_spolgloski = [litera for litera in self.imie if litera in spolgloski]
        nazwisko_spolgloski = [litera for litera in self.nazwisko if litera in spolgloski]

        email = "".join(imie_spolgloski) + "".join(nazwisko_spolgloski) + "@" + self.firma.lower().replace(" ", "") + ".com"
        return email


pracownik1 = Pracownik("Programista", 5000, "Adam", "Kowalski", 3, student=True)

pracownik1.roczna_podwyzka(5)

print("Stanowisko:", pracownik1.stanowisko)
print("Wynagrodzenie:", pracownik1.wynagrodzenie)
print("Imię:", pracownik1.imie)
print("Nazwisko:", pracownik1.nazwisko)
print("Staż pracy:", pracownik1.staz_pracy)
print("Student:", pracownik1.student)
print("Podatek:", pracownik1.oblicz_podatek())
print("Skladka zdrowotna:", pracownik1.oblicz_skladke_zdrowotna())
print("Email:", pracownik1.generuj_email())
