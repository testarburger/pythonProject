def oblicz_bmi(waga, wzrost):
    bmi = waga / (wzrost * wzrost)
    return bmi

def ocen_bmi(bmi):
    if bmi < 18.5:
        return "Niedowaga"
    elif bmi < 25:
        return "Waga normalna"
    elif bmi < 30:
        return "Nadwaga"
    else:
        return "Otyłość"

waga = float(input("Podaj swoją wagę (w kg): "))
wzrost = float(input("Podaj swój wzrost (w metrach): "))

bmi = oblicz_bmi(waga, wzrost)
ocena = ocen_bmi(bmi)

print(f"Twoje BMI wynosi: {bmi:.2f}")
print(f"Ocena BMI: {ocena}")
