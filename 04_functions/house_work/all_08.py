kraje = {
    'Polska': ['Sophia', 'Olivia', 'Zuzanna', 'Julia', 'Maja', 'Hanna', 'Lena', 'Alicja', 'Maria', 'Oliwia'],
    'Niemcy': ['Emma', 'Mia', 'Hannah', 'Emilia', 'Lina', 'Lea', 'Sophie', 'Marie', 'Mila', 'Leni'],
    'Wielka Brytania': ['Olivia', 'Amelia', 'Isla', 'Ava', 'Emily', 'Isabella', 'Mia', 'Poppy', 'Lily', 'Sophia'],
    'Francja': ['Emma', 'Louise', 'Jade', 'Alice', 'Chloe', 'Lina', 'Lea', 'Manon', 'Anna', 'Zoe'],
    'Hiszpania': ['Lucia', 'Marta', 'Sofia', 'Maria', 'Paula', 'Julia', 'Laura', 'Valeria', 'Alba', 'Emma'],
    'Włochy': ['Sofia', 'Giulia', 'Aurora', 'Alice', 'Greta', 'Emma', 'Beatrice', 'Ginevra', 'Vittoria', 'Adele'],
    'Holandia': ['Emma', 'Sophie', 'Mila', 'Julia', 'Tess', 'Lotte', 'Luna', 'Eva', 'Saar', 'Sara'],
    'Szwecja': ['Elsa', 'Alice', 'Maja', 'Lilly', 'Wilma', 'Ebba', 'Olivia', 'Alma', 'Agnes', 'Nellie'],
    'Norwegia': ['Nora', 'Emma', 'Sofie', 'Ella', 'Olivia', 'Maja', 'Emilie', 'Ida', 'Leah', 'Thea'],
    'Grecja': ['Sofia', 'Olivia', 'Maria', 'Eleni', 'Anna', 'Ioanna', 'Athina', 'Maria', 'Konstantina', 'Dimitra']
}

wszystkie_imiona = [imie for kraje_imiona in kraje.values() for imie in kraje_imiona]
imiona_wielokrotne = [imie for imie in wszystkie_imiona if wszystkie_imiona.count(imie) >= 3]
for imie in set(imiona_wielokrotne):
    print(imie)
