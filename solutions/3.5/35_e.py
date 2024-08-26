from sys import stdin

words = set()
for line in stdin:
    words |= set(line.rstrip("\n").split())

for word in sorted(words):
    length = len(word)
    if length == 1:
        print(word)
    else:
        mid = length // 2
        if word[:mid].lower() == word[mid + length % 2 :][::-1].lower():
            print(word)
