n = int(input())

for _ in range(n):
    items = input()
    banny_index = items.find("зайка") + 1
    if banny_index:
        print(banny_index)
    else:
        print("Заек нет =(")
