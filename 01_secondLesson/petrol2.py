my_distance=int(input("Your distance"))
fuer_100=float (input ("Consumption per 100 kilometers"))
fuer_1=fuer_100/100
cost_1= float(input("Prise petrol"))
cost_trip=fuer_1*my_distance*cost_1
print(round(cost_trip,2))