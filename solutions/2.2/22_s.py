x = float(input())
y = float(input())

# Вычисляем расстояние между заданной точкой и центром окружности (0, 0)
# Calculate the distance between the given point and the center (0, 0)
distance = (x**2 + y**2) ** 0.5

# Проверяем, больше ли расстояние, чем радиус
# Check if the distance is greater than the radius
in_sea = distance > 10

is_safe = True

if (-7 <= x <= 5) and y <= 0:
    # f(x) = 0.25(x + 7)(x - 5)
    # x = -1, y = -9 the vertex of the parabola
    parabola_y = 0.25 * (x - (-1)) ** 2 + (-9)
    is_safe = y < parabola_y

elif (0 <= x <= 5) and (0 <= y <= 5):
    # Проверяем, меньше/равно ли расстояние, чем радиус
    # Check if the distance is less than or equal to the radius
    is_safe = distance > 5

elif (-7 <= x <= 0) and (0 <= y <= 5):
    # Вычисляем коэффициент наклона гипотенузы
    # Используем формулу m = (y2 - y1) / (x2 - x1),
    # где x1, y1 = (-7, 0), а x2, y2 = (-4, 5)
    # Calculate the slope of the hypotenuse
    slope = (5 - 0) / (-4 - (-7))

    # Используем формулу b = y - m * x, где (x2, y2) - точка на линии
    # m - коэффициент наклона
    # Calculate the y-intercept for the hypotenuse
    intercept = 5 - slope * (-4)

    # Вычисляем y-координату для заданной x-координаты
    # Calculate the y-coordinate for the given x-coordinate
    y_on_hypotenuse = slope * x + intercept

    # Сравниваем заданную y-координату с y-координатой на гипотенузе
    # Compare the given y-coordinate with the y-coordinate on the hypotenuse
    is_safe = not ((-4 <= x <= 0) or y <= y_on_hypotenuse)

if in_sea:
    print("Вы вышли в море и рискуете быть съеденным акулой!")
elif is_safe:
    print("Зона безопасна. Продолжайте работу.")
else:
    print("Опасность! Покиньте зону как можно скорее!")
