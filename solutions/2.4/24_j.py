num = int(input())
print("А Б В")

for share_one in range(1, num - 1):
    for share_two in range(1, num - share_one):
        share_three = num - share_one - share_two
        print(share_one, share_two, share_three)
