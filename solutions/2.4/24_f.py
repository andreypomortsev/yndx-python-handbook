n = int(input())
a = int(input())

for _ in range(1, n):
    b = int(input())
    while b:
        a, b = b, a % b

gcd = a if a > 0 else -a
print(gcd)
