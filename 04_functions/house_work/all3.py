def maximum_of(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
x = 10
y = 5
z = 7
maximum = maximum_of(x, y, z)
print(f"Największa wartość: {maximum}")
