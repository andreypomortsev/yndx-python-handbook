number = int(input())

divisor = 2

while number > 1:
    while number % divisor == 0:
        print(divisor, end=" ")
        number //= divisor
        if divisor <= number:
            print("*", end=" ")
    divisor += 1
