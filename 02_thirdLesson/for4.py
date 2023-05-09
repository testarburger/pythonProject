def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input("Podaj liczbę naturalną (nie większą niż 8): "))
if n > 8:
    print("Błąd: Liczba nie może być większa niż 8.")
else:
    for i in range(n + 1):
        print(f"{i}! = {factorial(i)}")
