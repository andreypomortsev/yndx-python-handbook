import math


side_a = float(input())
side_b = float(input())
side_c = float(input())

# Вычисляем косинус каждого угла, используя Закон Косинусов
cos_angle_a = (side_b**2 + side_c**2 - side_a**2) / (2 * side_b * side_c)
cos_angle_b = (side_c**2 + side_a**2 - side_b**2) / (2 * side_c * side_a)
cos_angle_c = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)

# Вычисляем углы в радианах
angle_a_in_radians = math.acos(cos_angle_a)
angle_b_in_radians = math.acos(cos_angle_b)
angle_c_in_radians = math.acos(cos_angle_c)

# Преобразуем углы в градусы
angle_a = angle_a_in_radians * 180 / math.pi
angle_b = angle_b_in_radians * 180 / math.pi
angle_c = angle_c_in_radians * 180 / math.pi

if angle_b < angle_a > angle_c:
    max_angle = angle_a
elif angle_a < angle_b > angle_c:
    max_angle = angle_b
else:
    max_angle = angle_c

if max_angle == 90:
    print("100%")
elif max_angle < 90:
    print("крайне мала")
else:
    print("велика")
