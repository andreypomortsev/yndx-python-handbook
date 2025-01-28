side_a = float(input())
side_b = float(input())
side_c = float(input())

if side_c < side_a:
    side_c, side_a = side_a, side_c
if side_c < side_b:
    side_c, side_b = side_b, side_c

sum_of_a_b_squares = side_a**2 + side_b**2
c_square = side_c**2

epsilon = 1e-9

# Из-за погрешности вычислений, сравнивать числа нужно с погрешностью
# Due to the error of calculations, numbers should be compared with an error
if abs(c_square - sum_of_a_b_squares) < epsilon:
    print("100%")
elif c_square < sum_of_a_b_squares:
    print("крайне мала")
else:
    print("велика")
