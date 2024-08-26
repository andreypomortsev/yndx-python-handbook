from sys import stdin

headers = [line.rstrip("\n") for line in stdin]
searching_word = headers.pop().lower()

for header in headers:
    if searching_word in header.lower():
        print(header)
