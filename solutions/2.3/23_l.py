number = int(input())
max_num = number % 10

while number:
    digit = number % 10
    if digit > max_num:
        max_num = digit
    number //= 10

print(max_num)
