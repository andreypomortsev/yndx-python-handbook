n = int(input())
total = 0

for _ in range(n):
    number = int(input())
    while number:
        total += number % 10
        number //= 10

print(total)
