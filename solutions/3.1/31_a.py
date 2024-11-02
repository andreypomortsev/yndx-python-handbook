n = int(input())

for _ in range(n):
    word = input()
    first_letter = word[0]
    if first_letter != "а" and first_letter != "б" and first_letter != "в":
        print("NO")
        break
else:
    print("YES")
