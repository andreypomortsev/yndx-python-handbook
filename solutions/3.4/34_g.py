from itertools import combinations

n = int(input())
players = (input() for _ in range(n))
for player_one, player_two in combinations(players, 2):
    print(f"{player_one} - {player_two}")
