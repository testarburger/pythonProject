mapa= {
    "dom":["szkola" , "bar", "kosciol"],
    "szkola":["dom", "szpital"],
    "kosciol":["dom", 'bar', 'kino'],
    'bar':['kosciol', 'szpital'],
    'szpital':['bar', 'kino', 'teatr'],
    'kono':['kosciol', 'teatr'],
    'teatr':['szpital', 'kino']
}
def dostepne_miejsca(miejsce):
    if miejsce not in mapa:
        print("Nie ma takiego miejsca")
    else:
        dostepne = mapa[miejsce]
        if len(dostepne)==0:
            print('Nie ma sciezki ad', miejsce )
        else:
            print('Mozna przejsc ad', miejsce, 'do nastepnych miejsc')
            for miejsce in dostepne:
                print(miejsce)


miejsce = input('Napisz miejsce')
dostepne_miejsca(miejsce)