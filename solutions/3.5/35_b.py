from sys import stdin

height = 0
counter = 0

for line in stdin:
    _, before, after = line.rstrip("\n").split()
    height += float(after) - float(before)
    counter += 1

avg_height_gain = round(height / counter)
print(avg_height_gain)
