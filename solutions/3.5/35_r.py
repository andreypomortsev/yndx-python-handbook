import os

file_name = input()
file_size = os.path.getsize(file_name)

UNITS = ("Б", "КБ", "МБ", "ГБ")
unit_index = 0

while file_size >= 1024 and unit_index < 3:
    file_size /= 1024
    unit_index += 1

if file_size > int(file_size):
    file_size = int((file_size + 1) // 1)

print(f"{file_size:.0f}{UNITS[unit_index]}")
