n = int(input())
first_turn = input()

for _ in range(n - 1):
    name = input()
    if name < first_turn:
        first_turn = name

print(first_turn)
