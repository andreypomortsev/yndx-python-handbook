password = int(input())

hundreds = password // 100
tens = password // 10 % 10
ones = password % 10

first_sum = tens + ones
second_sum = hundreds + tens

if first_sum > second_sum:
    print(f"{first_sum}{second_sum}")
else:
    print(f"{second_sum}{first_sum}")
