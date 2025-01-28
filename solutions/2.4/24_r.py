t = int(input())

# t = n * (n + 1) / 2
# n = ((1 + 8*t)**0.5 - 1) / 2
numerator_n = (1 + 8 * t) ** 0.5 - 1

# Нам нужно округлить n вверх
# We need to round n up
n = int((numerator_n + 1) // 2)

counter = 1
formatter = 0

# Считаем значение formatter чтобы избежать создания доп строки
# Calculate the value of formatter to avoid creating an additional string
for i in range(n + 1):
    row_length = 0
    for j in range(i):
        if counter <= t:
            row_length += len(str(counter)) + (j > 0)
            counter += 1
    formatter = max(formatter, row_length)

counter = 1
for i in range(n + 1):
    row = ""
    for j in range(i):
        if counter <= t:
            if not row:
                row = str(counter)
            else:
                row = f"{row} {counter}"
        counter += 1
    if row:
        print(f"{row:^{formatter}}")
