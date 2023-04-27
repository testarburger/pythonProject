evaluation1 = float(input("Give your first evaluation (0-10): "))
evaluation2 = float(input("Give your second evaluation (0-10): "))
evaluation3 = float(input("Give your third evaluation (0-10): "))
average_evaluation = (evaluation1 + evaluation2 + evaluation3) / 3

if average_evaluation > 7:
    print("Your average evaluation is:", average_evaluation, "- book is very well!")
elif average_evaluation >= 5 and average_evaluation <= 7:
    print("Your average evaluation is:", average_evaluation, "- book is average.")
else:
    print("Your average evaluation is:", average_evaluation, "- book is not worth the attention.")
