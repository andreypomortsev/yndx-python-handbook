start, end, step = map(float, input().split())
flag = step > 0

while True:
    if flag and start > end:
        break
    elif not flag and start < end:
        break
    print(f"{start:.2f}")
    start += step
