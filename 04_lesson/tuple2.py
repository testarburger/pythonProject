my_tuple = (1, 2, 3, 4, 2, 5, 6, 5, 7, 8, 9, 9)
duplicates = []
for i in range(len(my_tuple)):
    for j in range(i + 1, len(my_tuple)):
        if my_tuple[i] == my_tuple[j] and my_tuple[i] not in duplicates:
            duplicates.append(my_tuple[i])

if len(duplicates) > 0:
    print("Powtarzające się elementy krotki to:")
    for item in duplicates:
        print(item)
else:
    print("Nie ma powtarzających się elementów w krotce.")
