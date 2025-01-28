n = int(input())

headers = [input() for _ in range(n)]
to_search = input().lower()

for header in headers:
    if to_search in header.lower():
        print(header)
