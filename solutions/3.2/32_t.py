numbers = sorted(set(map(int, input().split("; "))))
n = len(numbers)

for i in range(n):
    co_primes = []
    for j in range(n):
        if i != j:
            a, b = numbers[i], numbers[j]
            while b:
                a, b = b, a % b
            if a == 1:
                co_primes.append(numbers[j])

    if co_primes:
        print(f"{numbers[i]} - ", end="")
        print(*co_primes, sep=", ")
