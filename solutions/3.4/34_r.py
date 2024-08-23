from itertools import product

expression = input()

PRECEDENCE = {"or": 1, "and": 2, "not": 3}
postfix_expression = []
operators = []

tokens = expression.split()

for token in tokens:
    if token in {"and", "or"}:
        while operators and PRECEDENCE[operators[-1]] >= PRECEDENCE[token]:
            postfix_expression.append(operators.pop())
        operators.append(token)
    elif token == "not":
        operators.append(token)
    elif len(token) == 1:
        postfix_expression.append(token)


while operators:
    postfix_expression.append(operators.pop())

print("a b c f")

for vars in product(range(2), repeat=3):
    variable_to_value = dict(zip(("a", "b", "c"), vars))

    stack = []

    for token in postfix_expression:
        if len(token) == 1:
            stack.append(variable_to_value[token])
        elif token == "not":
            stack.append(not stack.pop())
        else:
            operand_two = stack.pop()
            operand_one = stack.pop()
            match token:
                case "and":
                    stack.append(operand_one and operand_two)
                case "or":
                    stack.append(operand_one or operand_two)

    f = stack[0]

    print(*vars, int(f))
