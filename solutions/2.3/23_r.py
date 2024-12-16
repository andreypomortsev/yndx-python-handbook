number = int(input())

divisor = 2

while number > 1:
    while number % divisor == 0:
        print(divisor, end="")
        number //= divisor
        if number > 1:
            print(" ", end="")
        if divisor <= number:
            print("*", end=" ")

    if divisor == 2:
        divisor = 3
    elif divisor == 3:
        divisor = 5
    else:
        divisor += 2 if divisor % 6 == 5 else 4
