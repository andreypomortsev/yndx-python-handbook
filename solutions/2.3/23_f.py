a = int(input())
b = int(input())

if not a:
    print(b)
elif not b:
    print(a)
else:
    while b:
        a, b = b, a % b
    print(a)
