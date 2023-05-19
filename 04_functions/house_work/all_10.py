N = int(input("Podaj liczbę N: "))

slownik = {}

for liczba in range(1, N+1):
    slownik[liczba] = liczba * liczba

print("Wygenerowany słownik:")
print(slownik)
