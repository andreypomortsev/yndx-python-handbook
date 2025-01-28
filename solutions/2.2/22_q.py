a = float(input())
b = float(input())
c = float(input())

if not a:
    if not b and not c:  # a == b == c == 0
        print("Infinite solutions")
    elif not b and c:  # a == b == 0 and c != 0
        print("No solution")
    else:  # a == 0 and b != 0 a linear equation
        print(round(-c / b, 2))
else:
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        root_one = round((-b + discriminant**0.5) / (2 * a), 2)
        root_two = round((-b - discriminant**0.5) / (2 * a), 2)
        if not discriminant:  # discriminant = 0
            print(root_two)
        elif root_one < root_two:  # When a < 0
            print(root_one, root_two)
        else:
            print(root_two, root_one)
    else:  # discriminant < 0
        print("No solution")
