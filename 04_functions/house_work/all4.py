def sprawdz_zakres(liczba, poczatek, koniec):
    if liczba >= poczatek and liczba <= koniec:
        return f"tak, liczba {liczba} znajduje się w zadanym zakresie"
    else:
        return f"nie, liczba {liczba} jest spoza zakresu"

poczatek = 10
koniec = 20
liczba = 15

wynik = sprawdz_zakres(liczba, poczatek, koniec)
print(wynik)
