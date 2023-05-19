# Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)
def wypisz_parzyste(lista):
    for i in lista:
        if i % 2 == 0:
            print(i)
moja_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wypisz_parzyste(moja_lista)