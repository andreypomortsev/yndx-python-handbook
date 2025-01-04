from itertools import product

PRECEDENCE = {"not": 3, "and": 2, "or": 1}
UNIQUE_VARS = ["a", "b", "c"]
REPEATS = 3

expression = input()

postfix_expression = []
operators = []
tokens = expression.split()

for token in tokens:
    if len(token) == 1:
        postfix_expression.append(token)
    elif token == "not":
        operators.append(token)
    elif token in PRECEDENCE:
        while operators and (PRECEDENCE[operators[-1]] >= PRECEDENCE[token]):
            postfix_expression.append(operators.pop())
        operators.append(token)

while operators:
    postfix_expression.append(operators.pop())

print(*UNIQUE_VARS, "f")

for vars in product(range(2), repeat=REPEATS):
    variable_to_value = dict(zip((UNIQUE_VARS), vars))
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

    f = stack.pop()
    print(*vars, int(f))
