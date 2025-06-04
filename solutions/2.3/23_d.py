start = int(input())
end = int(input())

if start > end:
    numbers = range(start, end - 1, -1)
else:
    numbers = range(start, end + 1)

last_number = len(numbers) - 1

for index, number in enumerate(numbers):
    if index == last_number:
        print(number)
    else:
        print(number, end=" ")
