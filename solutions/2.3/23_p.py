number = number_copy = int(input())

leftmost = 10
is_palyndrome = "YES"

while number_copy > 100:
    number_copy //= 10
    leftmost *= 10

while leftmost > 1:
    if number // leftmost != number % 10:
        is_palyndrome = "NO"
        break

    number = (number % leftmost) // 10
    leftmost //= 100

print(is_palyndrome)
