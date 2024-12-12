number = number_copy = int(input())

leftmost = 10
is_palyndrome = True

while number_copy > 100:
    number_copy //= 10
    leftmost *= 10

while leftmost > 0:
    if number // leftmost != number % 10:
        is_palyndrome = False
        break

    number = (number % leftmost) // 10
    leftmost //= 100

print("YES" if is_palyndrome else "NO")
