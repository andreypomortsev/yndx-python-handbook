str_number = input()

number = int(str_number)
ones = number % 10
tens = number % 100 // 10
hundreds = number % 1000 // 100
thousands = number // 1000

if thousands == ones and tens == hundreds:
    print("YES")
else:
    print("NO")
