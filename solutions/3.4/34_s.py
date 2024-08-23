from itertools import product

PRECEDENCE = {"or": 1, "and": 2, "not": 3}

expression = input()

unique_vars = sorted({var for var in expression.split() if var.isupper()})
repeats = len(unique_vars)
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
    elif token.isupper():
        postfix_expression.append(token)


while operators:
    postfix_expression.append(operators.pop())

print(*unique_vars, "F")
for vars in product(range(2), repeat=repeats):
    variable_to_value = dict(zip(unique_vars, vars))

    stack = []

    for token in postfix_expression:
        if token.isupper():
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
