quote = "Honesty is the first chapter in the book of wisdom."
print(len(quote))
st = quote.split()[-1]
print(st.replace('.',''))
print(quote[:len(quote)//2])
print(quote[len(quote)-1:])
half = quote[len(quote)//2:]
print(half)
print(half.replace(" ","")[::3])
print(quote[::2])
print(quote[::-1])
print(quote.replace('wisdom', 'friendship'))
