start, end = int(input()), int(input())

if start > end:
    print(*range(start, end - 1, -1))
else:
    print(*range(start, end + 1))
