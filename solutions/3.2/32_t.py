numbers = sorted(set(map(int, input().split(";"))))
n = len(numbers)

for i in range(n):
    co_primes = []
    for j in range(n):
        a, b = numbers[i], numbers[j]
        if a > 1 < b and i != j:
            while b:
                a, b = b, a % b
            if a == 1:
                co_primes.append(str(numbers[j]))

    if co_primes:
        answer = f"{numbers[i]} - {", ".join(co_primes)}"
        print(answer)
