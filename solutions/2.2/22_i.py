name_one = input()
name_two = input()
name_three = input()

if name_one > name_two:
    name_one, name_two = name_two, name_one
if name_one > name_three:
    name_one, name_three = name_three, name_one

print(name_one)
