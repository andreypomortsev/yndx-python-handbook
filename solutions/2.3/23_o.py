n = int(input())
bunny_counter = 0

for _ in range(n):
    surroundings = input()
    bunny_counter += "зайка" in surroundings

print(bunny_counter)
