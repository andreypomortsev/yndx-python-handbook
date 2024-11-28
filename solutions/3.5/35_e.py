from sys import stdin

words = set()
for line in stdin:
    words |= set(line.rstrip("\n").split())

for word in sorted(words):
    length = len(word)
    if length == 1:
        print(word)
    else:
        left_index = 0
        right_index = length - 1

        while left_index < right_index:
            if word[left_index].lower() != word[right_index].lower():
                break
            left_index += 1
            right_index -= 1
        else:
            print(word)
