number = int(input())

if not number:
    print(1)
else:
    for i in range(1, number):
        number *= i
    print(number)
