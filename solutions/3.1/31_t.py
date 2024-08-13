import math

chars = input().split()
stack = []

for char in chars:
    if char.lstrip("-").isdigit():
        stack.append(int(char))
    else:
        match char:
            case "+":
                new_number = stack.pop() + stack.pop()
            case "-":
                new_number = stack.pop(-2) - stack.pop()
            case "*":
                new_number = stack.pop() * stack.pop()
            case "/":
                new_number = stack.pop(-2) // stack.pop()
            case "~":
                new_number = -stack.pop()
            case "!":
                new_number = math.factorial(stack.pop())
            case "#":
                new_number = stack[-1]
            case "@":
                three, one, two = stack[-3:]
                for _ in range(3):
                    stack.pop()
        match char:
            case "@":
                stack.extend((one, two, three))
            case _:
                stack.append(new_number)

print(stack.pop())
