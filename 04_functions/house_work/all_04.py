number = list(range(1, 11))
table = []
for i in number:
    row = [i * j for j in number]
    table.append(row)
for row in table:
    print(row)