CHAR_RANGE = 1104
lines = []

while (line := input()) != "ФИНИШ":
    lines.extend(line.lower().split())

char_count = [0] * CHAR_RANGE

for word in lines:
    for char in word:
        char_count[ord(char)] += 1

max_count = 0
most_common_char = ""

for i in range(CHAR_RANGE):
    if char_count[i] > max_count:
        max_count = char_count[i]
        most_common_char = chr(i)

print(most_common_char)
