chars = input().split()
stack = []

for char in chars:
    # "-1".isdigit() returns False
    if char.lstrip("-").isdigit():
        stack.append(int(char))
    else:
        b = stack.pop()
        a = stack.pop()
        match char:
            case "+":
                result = a + b
            case "-":
                result = a - b
            case "*":
                result = a * b
        stack.append(result)

print(stack.pop())
