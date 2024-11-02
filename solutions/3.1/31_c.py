max_length = int(input())
n = int(input())

for _ in range(n):
    sentence = input()
    if len(sentence) > max_length:
        print(f"{sentence[:max_length - 3]}...")
    else:
        print(sentence)
