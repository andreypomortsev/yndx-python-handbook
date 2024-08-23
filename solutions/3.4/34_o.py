from itertools import chain, permutations

n = int(input())
groceries = chain.from_iterable(input().split(", ") for _ in range(n))
sorted_groceries = sorted(groceries)

for options in permutations(sorted_groceries, 3):
    print(" ".join(options))
