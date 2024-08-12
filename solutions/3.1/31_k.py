n = int(input())

# Сначала собираем все заголовки
# Так как поисковой запрос идет в последней строке
headers = [input() for _ in range(n)]

# Поисковой запрос
to_search = input().lower()

for header in headers:
    if to_search in header.lower():
        print(header)
