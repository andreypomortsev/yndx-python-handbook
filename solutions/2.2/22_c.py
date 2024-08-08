petya_speed = float(input())
vasya_speed = float(input())
tolya_speed = float(input())

if petya_speed < vasya_speed > tolya_speed:
    print("Вася")
elif vasya_speed < petya_speed > tolya_speed:
    print("Петя")
else:
    print("Толя")
