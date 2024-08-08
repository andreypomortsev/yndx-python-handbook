number = input()
if number[:2] == number[2:][::-1]:
    print("YES")
else:
    print("NO")
