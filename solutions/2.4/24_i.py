n = int(input())

for _ in range(n):
    number = int(input())
    max_number = float("-inf")

    while number > 0:
        digit = number % 10
        if digit > max_number:
            max_number = digit
        number //= 10

    print(max_number, end="")
