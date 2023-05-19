#Napisać funkcję, która sprawdza czy liczba jest parzysta.
def even_function(odd):
    if odd%2 == 0:
        return print("Your number is even")
    else:
        return print("Your number is odd")

even_function(int(input("Give your number-->")))