name_one = "Петя"
name_two = "Вася"
name_three = "Толя"

# Ширина подиума, всего три ступени: I, II, III
# Width of the podium, only three steps: I, II, III
WIDTH = 8

# Имена постоянные и длина 4
# Names are constant and have a length of 4
THIRD_NAME_LENGHT = 4

speed_one = float(input())
speed_two = float(input())
speed_three = float(input())

if speed_one < speed_two:
    speed_one, speed_two = speed_two, speed_one
    name_one, name_two = name_two, name_one

if speed_one < speed_three:
    speed_one, speed_three = speed_three, speed_one
    name_one, name_three = name_three, name_one

if speed_two < speed_three:
    speed_two, speed_three = speed_three, speed_two
    name_two, name_three = name_three, name_two

# Считаем отступы для форматирования третьего места по правому краю
# Counting spaces for the third place by the right edge
formatter = WIDTH * 3 - (WIDTH - THIRD_NAME_LENGHT) // 2

podium = f"""{name_one: ^24}
{name_two: ^{WIDTH}}
{name_three: >{formatter}}
{'II': ^{WIDTH}}{'I': ^{WIDTH}}{'III': ^{WIDTH}}"""

print(podium)
