max_length = int(input()) - 3
n = int(input())

for _ in range(n):
    sentence = input()
    if len(sentence) > max_length + 3:
        print(f"{sentence[:max_length]}...")
    else:
        print(sentence)
