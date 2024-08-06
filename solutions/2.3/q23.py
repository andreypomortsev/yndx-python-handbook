numbers = int(input())

clean_number = 0
position = 1

while numbers > 0:
    digit = numbers % 10
    if digit % 2 != 0:
        clean_number += digit * position
        position *= 10
    numbers //= 10

print(clean_number)
