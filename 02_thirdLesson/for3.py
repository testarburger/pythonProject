previous_sum = 0
for i in range(1, 11):
    current_sum = previous_sum + i
    print(current_sum)
    previous_sum = current_sum
