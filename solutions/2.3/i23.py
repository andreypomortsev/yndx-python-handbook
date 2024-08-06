number = int(input())

if number == 0:
    print(1)
else:
    for i in range(1, number):
        number *= i
    print(number)
