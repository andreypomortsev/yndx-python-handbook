n = int(input())

for _ in range(n):
    number = int(input())
    max_digit = float("-inf")

    while number:
        digit = number % 10
        if digit > max_digit:
            max_digit = digit
        number //= 10

    print(max_digit, end="")
