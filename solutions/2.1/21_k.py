num = int(input())

ones = num % 10
tens = num % 100 // 10
hundreds = num // 100 % 10
thousands = num // 1000

result = hundreds * 1000 + thousands * 100 + ones * 10 + tens

print(f"{result:04}")
