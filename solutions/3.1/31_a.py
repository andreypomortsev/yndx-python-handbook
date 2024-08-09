CHARS = {"а", "б", "в"}
n = int(input())

for _ in range(n):
    word = input()
    if word[0].lower() not in CHARS:
        print("NO")
        break
else:
    print("YES")
