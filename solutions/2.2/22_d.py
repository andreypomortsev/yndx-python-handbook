name_one = "Петя"
name_two = "Вася"
name_three = "Толя"

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

print(f"1. {name_one}")
print(f"2. {name_two}")
print(f"3. {name_three}")
