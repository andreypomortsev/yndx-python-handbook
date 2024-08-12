gcd = None

for number in input().split():
    if gcd is None:
        gcd = int(number)
        continue

    a, b = gcd, int(number)
    while b:
        a, b = b, a % b
    gcd = a

gcd = gcd if gcd > 0 else -gcd
print(gcd)
