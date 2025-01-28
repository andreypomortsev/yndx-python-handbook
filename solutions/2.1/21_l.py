one = int(input())
two = int(input())

ones = (one % 10 + two % 10) % 10
tens = ((one // 10) % 10 + (two // 10) % 10) % 10
hundreds = (one // 100 + two // 100) % 10
result = ones + tens * 10 + hundreds * 100

print(result)
