from collections import Counter

przedmioty = []
for i in range(5):
    print(f"Użytkownik {i+1}:")
    przedmioty_uzytkownika = []
    for j in range(4):
        przedmiot = input(f"Podaj przedmiot {j+1}: ")
        przedmioty_uzytkownika.append(przedmiot.lower().capitalize())
    przedmioty.append(przedmioty_uzytkownika)
wszystkie_przedmioty = [przedmiot for lista in przedmioty for przedmiot in lista]
licznik_przedmiotow = Counter(wszystkie_przedmioty)
najpopularniejszy_przedmiot = licznik_przedmiotow.most_common(1)[0][0]
print(f"Najpopularniejszy przedmiot to: {najpopularniejszy_przedmiot}")
