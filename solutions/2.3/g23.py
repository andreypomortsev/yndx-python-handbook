a = int(input())
b = int(input())

a_copy = int(a)
b_copy = int(b)

if not a:
    gcd = b
elif not b:
    gcd = a
else:
    while b:
        a, b = b, a % b
    gcd = a

lcm = (a_copy * b_copy) // gcd
print(lcm)
