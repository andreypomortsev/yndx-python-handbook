n = int(input())
banny_counter = 0

for _ in range(n):
    items = input().split()
    for item in items:
        banny_counter += "зайка" == item.lower()

print(banny_counter)
