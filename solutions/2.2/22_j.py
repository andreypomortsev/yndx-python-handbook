password = int(input())

hundreds = password // 100
tens = password // 10 % 10
ones = password % 10

first_sum = tens + ones
second_sum = hundreds + tens

if first_sum < second_sum:
    first_sum, second_sum = second_sum, first_sum

condition = second_sum > 9
power = 1 + condition
multiplier = 10**power

answer = first_sum * multiplier + second_sum

print(answer)
