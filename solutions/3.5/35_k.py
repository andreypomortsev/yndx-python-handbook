import json

DEFAULT_ENCODING = {"encoding": "UTF-8"}

file_name = input()
file_output = input()

counter = 0
positive_count = 0
total_sum = 0
minimum = float("inf")
maximum = float("-inf")

with open(file_name, "r", **DEFAULT_ENCODING) as file:
    while line := file.readline():
        for number in line.split():
            number = int(number)
            positive_count += number > 0
            total_sum += number
            minimum = min(minimum, number)
            maximum = max(maximum, number)
            counter += 1

average = round(total_sum / counter, 2)

json_like = {
    "count": counter,
    "positive_count": positive_count,
    "min": minimum,
    "max": maximum,
    "sum": total_sum,
    "average": average,
}

with open(file_output, "w", **DEFAULT_ENCODING) as json_file:
    json.dump(json_like, json_file, indent=4)
