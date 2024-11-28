DEFAULT_ENCODING = {"encoding": "UTF-8"}

file_name = input()
tail = int(input())

lines = []

with open(file_name, "r", **DEFAULT_ENCODING) as file:
    while line := file.readline():
        lines.append(line)

print(*lines[-tail:], sep="")
