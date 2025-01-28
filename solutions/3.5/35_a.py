from sys import stdin

sum_of_numbers = 0

for line in stdin:
    sum_of_numbers += sum(map(int, line.rstrip("\n").split()))

print(sum_of_numbers)
