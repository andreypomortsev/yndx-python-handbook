n = int(input())
first_turn = None

for _ in range(n):
    name = input()
    if not first_turn:
        first_turn = name
    elif name < first_turn:
        first_turn = name

print(first_turn)
