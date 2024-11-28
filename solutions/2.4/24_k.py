n = int(input())

prime_nums_counter = 0

for _ in range(n):
    number = int(input())

    if number <= 1:
        continue
    elif number <= 3:
        prime_nums_counter += 1
    elif number % 2 == 0 or number % 3 == 0:
        continue
    else:
        i = 5
        sqrt = int(number**0.5) + 1
        while i <= sqrt:
            if number % i == 0 or number % (i + 2) == 0:
                is_prime = False
                break
            i += 6
        else:
            prime_nums_counter += 1

print(prime_nums_counter)
