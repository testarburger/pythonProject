# zmienną, ale mogła by być brana od użytkownika
abrakadabra = "abrakadabra"

# wyświetlenie znaków na pozycjach parzystych za pomocą pętli while
i = 0
while i < len(abrakadabra):
    if i % 2 == 0:
        print(abrakadabra[i])
    i += 1
# vs wyświetlenie znaków na pozycjach parzystych za pomocą pętli for 

for i in range(len(abrakadabra)):
    if i % 2 == 0:
        print(abrakadabra[i])

    # vs wyświetlenie znaków na pozycjach parzystych za pomocą pętli for, range "co 2" za pomocą range(start, stop, krok)

for i in range(0, len(abrakadabra), 2):
    print(abrakadabra[i])