num = int(input())
total = 0

while num > 0:
    total += num % 10
    num //= 10

print(total)
