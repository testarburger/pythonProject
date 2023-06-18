import datetime

class Zegar:
    def __init__(self, strefa_czasowa):
        self.strefa_czasowa = strefa_czasowa

    def aktualny_czas(self):
        czas = datetime.datetime.now(self.strefa_czasowa)
        return czas.strftime("%H:%M:%S")


class Kalendarz:
    def __init__(self, rok, miesiac):
        self.rok = rok
        self.miesiac = miesiac

    def ile_dni(self):
        dni_w_miesiacu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.miesiac == 2 and self.czy_przestepny():
            return 29
        else:
            return dni_w_miesiacu[self.miesiac - 1]

    def czy_przestepny(self):
        if self.rok % 4 == 0:
            if self.rok % 100 == 0:
                if self.rok % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


class ZegaroKalendarz(Zegar, Kalendarz):
    def __init__(self, strefa_czasowa, rok, miesiac):
        Zegar.__init__(self, strefa_czasowa)
        Kalendarz.__init__(self, rok, miesiac)

    def widok_tygodnia(self):
        pierwszy_dzien = datetime.date(self.rok, self.miesiac, 1)
        pierwszy_dzien_tygodnia = pierwszy_dzien.weekday()  # Poniedziałek: 0, Wtorek: 1, ..., Niedziela: 6
        ilosc_dni = self.ile_dni()

        widok = ""
        for dzien in range(ilosc_dni):
            dzien_tygodnia = (pierwszy_dzien_tygodnia + dzien) % 7
            widok += datetime.date(self.rok, self.miesiac, dzien + 1).strftime("%d/%m/%Y") + " (" + self.nazwa_dnia(dzien_tygodnia) + ")\n"

        return widok

    def nazwa_dnia(self, numer_dnia):
        dni_tygodnia = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
        return dni_tygodnia[numer_dnia]


zegaro_kalendarz1 = ZegaroKalendarz("Europe/Warsaw", 2023, 6)
zegaro_kalendarz2 = ZegaroKalendarz("America/New_York", 2023, 6)
zegaro_kalendarz3 = ZegaroKalendarz("Asia/Tokyo", 2023, 6)

