a = None
numbers = input().split()

for number in numbers:
    if a is None:
        a = int(number)
        continue

    b = int(number)
    while b:
        a, b = b, a % b

gcd = a if a > 0 else -a
print(gcd)
