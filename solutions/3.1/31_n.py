list_of_numbers = input().split()
power = int(input())

for number in list_of_numbers:
    powered_number = int(number) ** power
    print(powered_number, end=" ")
