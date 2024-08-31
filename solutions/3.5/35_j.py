file_name = input()
tail = int(input())

lines = []

with open(file_name, "r", encoding="UTF-8") as file:
    while line := file.readline():
        lines.append(line)

print(*lines[-tail:], sep="")
