n = int(input())

winner, max_number = None, 0

for _ in range(n):
    name = input()
    number = int(input())
    sum_of_digits = 0

    while number > 0:
        sum_of_digits += number % 10
        number //= 10

    if sum_of_digits >= max_number:
        max_number = sum_of_digits
        winner = name

print(winner)
