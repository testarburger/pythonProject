# Pobieranie trzech liczb od użytkownika
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))
liczba3 = float(input("Podaj trzecią liczbę: "))

# Znajdowanie największej liczby
najwieksza = liczba1

if liczba2 > najwieksza:
    najwieksza = liczba2

if liczba3 > najwieksza:
    najwieksza = liczba3

# Wyświetlanie liczb od największej do najmniejszej
print("Liczby od największej do najmniejszej:")
if najwieksza == liczba1:
    print(najwieksza)
    if liczba2 >= liczba3:
        print(liczba2)
        print(liczba3)
    else:
        print(liczba3)
        print(liczba2)
elif najwieksza == liczba2:
    print(najwieksza)
    if liczba1 >= liczba3:
        print(liczba1)
        print(liczba3)
    else:
        print(liczba3)
        print(liczba1)
else:
    print(najwieksza)
    if liczba1 >= liczba2:
        print(liczba1)
        print(liczba2)
    else:
        print(liczba2)
        print(liczba1)
