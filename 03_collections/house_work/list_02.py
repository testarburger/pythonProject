numbers = []
for i in range(10):
    number = int(input("Enter a number: "))
    numbers.append(number)
print("Odd numbers:")
for number in numbers:
    if number % 2 != 0:
        print(number)
