number = int(input())

digit_one = number % 10
digit_two = number % 100 // 10
digit_three = number // 100

if digit_one < digit_two:
    digit_one, digit_two = digit_two, digit_one
if digit_one < digit_three:
    digit_one, digit_three = digit_three, digit_one
if digit_two < digit_three:
    digit_two, digit_three = digit_three, digit_two

if digit_three > 0:
    minimum = digit_three * 10 + digit_two
elif digit_two == digit_three == 0:
    minimum = digit_one * 10
else:
    minimum = digit_two * 10

maximum = digit_one * 10 + digit_two

print(minimum, maximum)
