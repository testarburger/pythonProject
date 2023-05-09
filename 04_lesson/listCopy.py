import copy
list1 = [[1, 2], [3, 4]]
list2 = copy.copy(list1)
list3 = copy.deepcopy(list1)

# zmiana wartości w oryginalnej liście
list1[0][1] = 5

print(list1)  # [[1, 5], [3, 4]]
print(list2)  # [[1, 5], [3, 4]]
print(list3)  # [[1, 2], [3, 4]]

