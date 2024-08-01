number_one = int(input())
number_two = int(input())
number_three = int(input())

first_one = number_one // 10
first_two = number_two // 10
first_three = number_three // 10

if first_one == first_two == first_three:
    print(first_one)
else:
    print(number_one % 10)
