SEARCH_WORD = "зайка"
closest_objects = set()

while surroundings := input().split():
    n = len(surroundings)
    for i in range(n):
        if surroundings[i] == SEARCH_WORD:
            if i > 0:
                closest_objects.add(surroundings[i - 1])
            if i < n - 1:
                closest_objects.add(surroundings[i + 1])

print("\n".join(closest_objects))
