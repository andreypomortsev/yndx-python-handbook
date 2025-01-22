n = int(input())
porridge = [input() for _ in range(n)]
repeats = int(input())

counter = i = 0

while counter < repeats:
    print(porridge[i])
    counter += 1
    i += 1
    if i == n:
        i = 0
