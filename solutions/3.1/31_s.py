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
        stack.append(new_number)

print(stack.pop())
