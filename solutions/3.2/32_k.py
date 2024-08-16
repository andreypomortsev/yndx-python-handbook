from collections import defaultdict

n = int(input())
last_names_counter = defaultdict(int)

for _ in range(n):
    last_name = input()
    last_names_counter[last_name] += 1

result = 0
for _, counter in last_names_counter.items():
    result += counter if counter > 1 else 0

print(result)
