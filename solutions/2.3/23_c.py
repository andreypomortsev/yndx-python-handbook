start = int(input())
end = int(input())

for i in range(start, end + 1):
    if i == end:
        print(i)
    else:
        print(i, end=' ')
