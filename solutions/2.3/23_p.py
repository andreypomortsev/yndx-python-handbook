n = n_copy = int(input())

left = 10
is_palyndrome = True

while n_copy > 100:
    n_copy //= 10
    left *= 10

while left > 0:
    if n // left != n % 10:
        is_palyndrome = False
        break

    n = (n % left) // 10
    left //= 100

print("YES" if is_palyndrome else "NO")
