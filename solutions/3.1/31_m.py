n = int(input())

numbers = [int(input()) for _ in range(n)]
power = int(input())

for number in numbers:
    powered_number = number**power
    print(powered_number)
