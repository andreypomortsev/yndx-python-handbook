CHAR_RANGE = 1104
lines = []

while (line := input()) != "ФИНИШ":
    lines.append(line.lower())

long_line = "".join(lines)
char_count = [0] * CHAR_RANGE

for char in long_line:
    char_count[ord(char)] += 1

most_common_char = ""
max_count = 0

for i in range(CHAR_RANGE):
    if i == 32:  # chr(32) = " "
        continue
    if char_count[i] > max_count:
        max_count = char_count[i]
        most_common_char = chr(i)

print(most_common_char)
