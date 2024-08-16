from collections import defaultdict

n = int(input())
last_names_counter = defaultdict(int)

for _ in range(n):
    last_name = input()
    last_names_counter[last_name] += 1

flag = True

for last_name, counter in sorted(last_names_counter.items()):
    if counter > 1:
        print(f"{last_name} - {counter}")
        flag = False

if flag:
    print("Однофамильцев нет")
