a = float(input())
b = float(input())
c = float(input())

if not a:
    if not b and not c:  # a == b == c == 0
        print("Infinite solutions")
    elif not b and c:  # a == b == 0 and c != 0
        print("No solution")
    else:  # a == 0 and b != 0 линейное уравнение
        print(round(-c / b, 2))
else:
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        root1 = round((-b + discriminant**0.5) / (2 * a), 2)
        root2 = round((-b - discriminant**0.5) / (2 * a), 2)
        if not discriminant:
            print(root2)
        elif root1 < root2:  # Условие выполняется при a < 0
            print(root1, root2)
        else:
            print(root2, root1)
    else:  # Дискриминант меньше 0
        print("No solution")
