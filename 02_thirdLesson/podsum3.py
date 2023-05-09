text = input("Wprowadź ciąg znaków: ")
lowercase_count = 0
uppercase_count = 0
digit_count = 0
special_count = 0
for char in text:
    if char.islower():
        lowercase_count += 1
    elif char.isupper():
        uppercase_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1
print("Ilość małych liter:", lowercase_count)
print("Ilość wielkich liter:", uppercase_count)
print("Ilość cyfr:", digit_count)
print("Ilość znaków specjalnych:", special_count)
