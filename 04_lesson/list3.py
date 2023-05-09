lista = input("Podaj listę liczb całkowitych, oddzielając je przecinkami: ").split(",")
lista = [int(l) for l in lista]
if lista[0] == lista[-1]:
    print("Pierwszy i ostatni element są takie same.")
else:
    print("Pierwszy i ostatni element nie są takie same.")

