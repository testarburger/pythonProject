def fibonacci_sequence(n):
    sequence = [0, 1]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence

n = int(input("Podaj liczbę elementów ciągu Fibonacciego: "))
fibonacci = fibonacci_sequence(n)
print(f"Ciąg Fibonacciego dla n = {n}: {fibonacci}")
