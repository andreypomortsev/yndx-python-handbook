# Для прохождения тестов Яндекса в решении нельзя использовать
# множества тк в тестовых данных есть повторы
n = int(input())

counter = {}
most_popular = 0

for _ in range(n):
    point = tuple(map(lambda x: int(x) // 10, input().split()))

    if point not in counter:
        counter[point] = 0
    counter[point] += 1

    if counter[point] > most_popular:
        most_popular = counter[point]

print(most_popular)
