from collections import defaultdict


friends = defaultdict(set)
friends_2 = defaultdict(set)

while sp := input():
    one, two = sp.split()

    friends[one].add(two)
    friends[two].add(one)

for name, direct_friends in friends.items():
    friends_2[name] = set()

    for friend in direct_friends:
        friends_2[name].update(friends[friend])

    friends_2[name] -= direct_friends | {name}

for name, second_level_friends in sorted(friends_2.items()):
    print(f"{name}:", ", ".join(sorted(second_level_friends)))
