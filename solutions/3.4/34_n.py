from itertools import permutations

n = int(input())
athletes = sorted([input() for _ in range(n)])
number_of_places = min(n, 3)

for top_3_or_less in permutations(athletes, number_of_places):
    print(", ".join(top_3_or_less))
