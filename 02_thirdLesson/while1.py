F = 0
while F <= 200:
    C = (5 / 9) * (F - 32)
    print(f"{F} stopni F = {C:.2f} stopni C")
    F += 20
print("*******")
for F in range(0, 201, 20):
    C = (5 / 9) * (F - 32)
    print(f"{F} stopni F = {C:.2f} stopni C")
