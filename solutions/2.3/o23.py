n = int(input())
bunny_counter = 0

for _ in range(n):
    bunny_counter += "зайка" in input()

print(bunny_counter)
