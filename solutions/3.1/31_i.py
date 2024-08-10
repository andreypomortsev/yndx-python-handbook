while line := input():
    index = line.find("#")

    if index == -1:
        print(line)
        continue
    if not index:
        continue

    stack = ""
    flag = False

    for i in range(len(line)):
        char = line[i]
        if char in "\"'":
            if not stack:
                stack += char
            elif char == stack[-1]:
                stack = stack[:-1]

        if char == "#" and not stack:
            print(f"{line[:i].rstrip()}")
            flag = True
            break

    if not flag:
        print(line)
