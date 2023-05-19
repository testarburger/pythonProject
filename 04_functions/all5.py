poem= "Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce"
poem=poem.replace(",", "").replace(".", "")
wyrazy=poem.lower().split()
licznik={}
for wyraz in wyrazy:
    if wyraz in licznik:
        licznik[wyraz]+=1
    else:
        licznik[wyraz]=1
for wyraz, wystapienia in licznik.items():
    print(f"{wyraz}: {wystapienia}")