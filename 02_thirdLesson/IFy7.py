weight = int(input('Your weight'))
height = float(input('Your height'))
bmi= weight/(height**2)
if bmi<18.5:
    print("Underweight")
elif bmi>18.5 and bmi<25:
    print("Correct weight")
elif bmi>25 and bmi<30:
    print("Overweight")
else:
    print("Obesity")