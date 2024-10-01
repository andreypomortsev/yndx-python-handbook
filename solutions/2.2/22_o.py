number_one = int(input())
number_two = int(input())

digit_one = number_one % 10
digit_two = number_one // 10
digit_three = number_two % 10
digit_four = number_two // 10

# Ищем максимумы и минимумы
if digit_one < digit_two:
    digit_one, digit_two = digit_two, digit_one

if digit_three < digit_four:
    digit_three, digit_four = digit_four, digit_three

# Ищем максимум
if digit_one < digit_three:
    digit_one, digit_three = digit_three, digit_one

# Ищем минимум
if digit_two < digit_four:
    digit_two, digit_four = digit_four, digit_two


hundreds = digit_one * 100
tens = ((digit_two + digit_three) % 10) * 10
units = digit_four

answer = hundreds + tens + units

print(answer)
