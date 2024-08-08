n = int(input())

prime_nums_counter = 0

for _ in range(n):
    number = int(input())
    if number < 2:
        continue
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            break
    else:
        prime_nums_counter += 1

print(prime_nums_counter)
