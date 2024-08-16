digits = input().split()

answer = []

for digit in digits:
    binary = bin(int(digit))[2:]
    digits = len(binary)
    units = sum(i == "1" for i in binary)
    zeros = digits - units
    answer.append({"digits": digits, "units": units, "zeros": zeros})

print(answer)
