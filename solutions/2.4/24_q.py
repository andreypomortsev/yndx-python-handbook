n = int(input())

number_of_palindroms = 0

for _ in range(n):
    number = int(input())
    number_copy = number
    reversed_number = 0

    while number_copy > 0:
        digit = number_copy % 10
        reversed_number = reversed_number * 10 + digit
        number_copy //= 10

    number_of_palindroms += number == reversed_number

print(number_of_palindroms)
