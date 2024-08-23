from itertools import chain

n = int(input())

groceries = chain.from_iterable(input().split(", ") for _ in range(n))
sorted_groceries = sorted(groceries)

index = 1
for item in sorted_groceries:
    if item:
        print(f"{index}. {item}")
        index += 1
