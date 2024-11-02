chars = input().split()
stack = []

for char in chars:
    if char.lstrip("-").isdigit():
        stack.append(int(char))

    elif char == "~":
        stack.append(-stack.pop())

    elif char == "!":
        factorial = 1
        for i in range(1, stack.pop() + 1):
            factorial *= i
        stack.append(factorial)

    elif char == "#":
        stack.append(stack[-1])

    elif char == "+":
        stack.append(stack.pop() + stack.pop())

    elif char == "*":
        stack.append(stack.pop() * stack.pop())

    elif char == "-":
        b, a = stack.pop(), stack.pop()
        stack.append(a - b)

    elif char == "/":
        b, a = stack.pop(), stack.pop()
        stack.append(a // b)

    elif char == "@":
        stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]

print(stack.pop())
