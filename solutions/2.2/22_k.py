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

is_beautiful = digit_one + digit_three == digit_two * 2

print("YES" if is_beautiful else "NO")
