counter = {}

while surroundings := input().split():
    for thing in surroundings:
        if thing not in counter:
            counter[thing] = 0
        counter[thing] += 1

sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

for key, value in sorted_counter:
    print(key, value)
