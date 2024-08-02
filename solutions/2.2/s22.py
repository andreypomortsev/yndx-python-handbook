x = float(input())
y = float(input())
flag = True

# Вычисляем расстояние между заданной точкой и центром окружности (0, 0)
distance = (x**2 + y**2) ** 0.5

# Проверяем, больше ли расстояние, чем радиус
if distance > 10:
    flag = False
    print("Вы вышли в море и рискуете быть съеденным акулой!")

elif (-7 <= x <= 5) and y <= 0:
    # 0.25 коэффициент из f(x) = (1/4)(x + 7)(x - 5)
    # -1 x-координат вертекса
    # -9 y-координат вертекса
    parabola_y = 0.25 * (x - (-1)) ** 2 + (-9)
    if y >= parabola_y:
        flag = False
        print("Опасность! Покиньте зону как можно скорее!")

elif (0 <= x <= 5) and (0 <= y <= 5):
    # Проверяем, меньше/равно ли расстояние, чем радиус
    if distance <= 5:
        flag = False
        print("Опасность! Покиньте зону как можно скорее!")

elif (-7 <= x <= 0) and (0 <= y <= 5):
    # Вычисляем коэффициент наклона гипотенузы
    # Используем формулу m = (y2 - y1) / (x2 - x1),
    # где x1, y1 = (-7, 0), а x2, y2 = (-4, 5)
    slope = (5 - 0) / (-4 - (-7))

    # Используем формулу b = y - m * x, где (x2, y2) - точка на линии
    # а m - коэффициент наклона
    intercept = 5 - slope * (-4)

    # Вычисляем y-координату для заданной x-координаты
    y_on_hypotenuse = slope * x + intercept

    # Сравниваем заданную y-координату с y-координатой на гипотенузе
    if (-4 <= x <= 0) or y <= y_on_hypotenuse:
        flag = False
        print("Опасность! Покиньте зону как можно скорее!")
if flag:
    print("Зона безопасна. Продолжайте работу.")
