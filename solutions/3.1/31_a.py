ALLOWED_LETTERS = ["а", "б", "в"]

n = int(input())

for _ in range(n):
    word = input()
    first_letter = word[0]
    if first_letter not in ALLOWED_LETTERS:
        print("NO")
        break
else:
    print("YES")
