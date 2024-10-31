a = int(input())
b = int(input())

ab_prod = a * b

while b:
    a, b = b, a % b

lcm = ab_prod // a
print(lcm)
