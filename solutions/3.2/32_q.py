# Теория Графов
from collections import defaultdict

friends = defaultdict(set)
friends_2 = defaultdict(set)

while sp := input():
    one, two = sp.split()

    friends[one].add(two)
    friends[two].add(one)

for name, direct_friends in friends.items():
    for friend in direct_friends:
        friends_2[name].update(friends[friend])

    friends_2[name] -= direct_friends | {name}

for name, second_level_friends in sorted(friends_2.items()):
    str_of_friends = ", ".join(sorted(second_level_friends))
    print(f"{name}: {str_of_friends}")
