from itertools import product

expression = input()

REPLACEMENTS = {
    "not": " not ",
    "~": " ~ ",
    "and": " and ",
    "or": " or ",
    "^": " ^ ",
    "->": " -> ",
    "(": " ( ",
    ")": " ) ",
}

# Очищаем выражение
for old_value, new_value in REPLACEMENTS.items():
    expression = expression.replace(old_value, new_value)

expression = expression.split()

PRECEDENCE = {
    "not": 5,
    "and": 4,
    "or": 3,
    "->": 2,
    "~": 2,
    "^": 2,
}

ASSOCIATIVITY = {
    "not": "right",
    "~": "left",
    "and": "left",
    "or": "left",
    "^": "left",
    "->": "left",
}

postfix_expression = []
operator_stack = []

for token in expression:
    if token.isupper():
        postfix_expression.append(token)
    elif token in PRECEDENCE:
        while (
            operator_stack
            and operator_stack[-1] != "("
            and (
                ASSOCIATIVITY[token] == "left"
                and PRECEDENCE[token] <= PRECEDENCE[operator_stack[-1]]
                or ASSOCIATIVITY[token] == "right"
                and PRECEDENCE[token] < PRECEDENCE[operator_stack[-1]]
            )
        ):
            postfix_expression.append(operator_stack.pop())
        operator_stack.append(token)
    elif token == "(":
        operator_stack.append(token)
    elif token == ")":
        while operator_stack and operator_stack[-1] != "(":
            postfix_expression.append(operator_stack.pop())
        if operator_stack and operator_stack[-1] == "(":
            operator_stack.pop()


while operator_stack:
    postfix_expression.append(operator_stack.pop())

unique_vars = sorted(set(filter(lambda x: x.isupper(), postfix_expression)))
repeats = len(unique_vars)

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
                case "~":
                    stack.append(operand_one == operand_two)
                case "->":
                    stack.append(not operand_one or operand_two)
                case "^":
                    stack.append(operand_one ^ operand_two)

    f = int(stack.pop())
    print(*vars, f)
