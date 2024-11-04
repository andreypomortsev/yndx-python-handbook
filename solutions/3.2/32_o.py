digits = map(int, input().split())

answer = []

for digit in digits:
    binary = bin(digit)[2:]
    digits = len(binary)
    units = binary.count("1")
    zeros = digits - units
    answer.append({"digits": digits, "units": units, "zeros": zeros})

print(answer)
