DEFAULT_ENCODING = {"encoding": "UTF-8"}

file_name = input()

array = []
counter = positives = total_sum = 0
minimum = float("inf")
maximum = float("-inf")

with open(file_name, "r", **DEFAULT_ENCODING) as file:
    while line := file.readline():
        for number in line.split():
            number = int(number)
            positives += number > 0
            minimum = min(minimum, number)
            maximum = max(maximum, number)
            total_sum += number
            counter += 1

avg = total_sum / counter

print(counter, positives, minimum, maximum, total_sum, f"{avg:.2f}", sep="\n")
