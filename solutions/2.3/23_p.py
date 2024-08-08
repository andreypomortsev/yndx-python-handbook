number = int(input())

number_copy = number
reversed_number = 0

while number_copy > 0:
    digit = number_copy % 10
    reversed_number = reversed_number * 10 + digit
    number_copy //= 10

is_palindrome = number == reversed_number

if is_palindrome:
    print("YES")
else:
    print("NO")
