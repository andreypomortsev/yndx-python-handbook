n = int(input())
gcd = int(input())

for _ in range(1, n):
    current_number = int(input())
    a, b = gcd, current_number
    while b:
        a, b = b, a % b
    gcd = a

gcd = gcd if gcd > 0 else -gcd
print(gcd)
