n = int(input())

number_of_polindroms = 0

for _ in range(n):
    number = input()
    length = len(number)
    mid = length // 2
    mid_odd = mid + length % 2
    check = number[:mid] == number[mid_odd:][::-1]
    number_of_polindroms += check

print(number_of_polindroms)
