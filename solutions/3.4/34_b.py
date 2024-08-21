first_group = input().split(", ")
second_group = input().split(", ")

for child_one, child_two in zip(first_group, second_group):
    print(f"{child_one} - {child_two}")
