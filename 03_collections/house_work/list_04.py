elements = []
n = int(input("Enter the number of elements: "))
if n % 2 != 0:
    print("Please enter an even number of elements!")
    exit()
for i in range(n):
    element = input("Enter an element: ")
    elements.append(element)
middle_index = n // 2
middle_element1 = elements[middle_index - 1]
middle_element2 = elements[middle_index]
if middle_element1 == middle_element2:
    print("The two middle elements are the same.")
else:
    print("The two middle elements are not the same.")
