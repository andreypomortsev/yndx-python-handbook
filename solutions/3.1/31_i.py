while line := input():
    stack = []
    flag = False

    for i in range(len(line)):
        char = line[i]

        if char == "#":
            if not i:  # Проверяем не начинается ли строка с коммента
                flag = True
                break
            if not stack:  # Только потом проверяем стэк
                print(f"{line[:i].rstrip()}")
                flag = True
                break

        if char in ["'", '"']:
            if not stack:
                stack.append(char)
            elif char == stack[-1]:
                stack.pop()

    if not flag:
        print(line)
