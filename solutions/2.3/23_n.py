number = int(input())
is_prime = True

if number <= 1:
    is_prime = False
elif number <= 3:
    is_prime = True
elif number % 2 == 0 or number % 3 == 0:
    is_prime = False
elif is_prime:
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            is_prime = False
            break
        i += 6

if is_prime:
    print("YES")
else:
    print("NO")
