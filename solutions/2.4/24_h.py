n = int(input())

winner = None
max_sum = 0

for _ in range(n):
    name = input()
    number = int(input())
    sum_of_digits = 0

    while number:
        sum_of_digits += number % 10
        number //= 10

    if sum_of_digits >= max_sum:
        max_sum = sum_of_digits
        winner = name

print(winner)
