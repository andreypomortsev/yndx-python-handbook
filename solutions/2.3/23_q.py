numbers = input()

for digit in numbers:
    if int(digit) % 2 != 0:
        print(digit, end="")
