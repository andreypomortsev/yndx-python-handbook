line_1 = input()
line_2 = input()
line_3 = input()

# Сначала сортируем строки по длине
# Sort by length
if line_1 > line_2:
    line_1, line_2 = line_2, line_1
if line_1 > line_3:
    line_1, line_3 = line_3, line_1
if line_2 > line_3:
    line_2, line_3 = line_3, line_2

# Проверяем, в какой строке есть слово "зайка"
# Check which line contains the word "зайка"
if "зайка" in line_1:
    answer = line_1
elif "зайка" in line_2:
    answer = line_2
else:
    answer = line_3

print(answer, len(answer))
