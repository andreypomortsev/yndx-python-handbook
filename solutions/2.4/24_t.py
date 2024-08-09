number = int(input())
best_base = 2
max_sum = 0

for base in range(2, 11):
    temp_number = number
    new_number = 0
    multiplier = 1
    sum_digits = 0

    while temp_number > 0:
        new_number += multiplier * (temp_number % base)
        multiplier *= 10
        temp_number //= base

    while new_number > 0:
        sum_digits += new_number % 10
        new_number //= 10

    sum_digits += new_number % 10

    if sum_digits > max_sum:
        max_sum = sum_digits
        best_base = base

print(best_base)
