from sys import stdin

DEFAULT_ENCODING = {"encoding": "UTF-8"}

searching_phrase = input().lower()
not_found = True

for file_name in stdin:
    file_name = file_name[:-1]

    with open(file_name, "r", **DEFAULT_ENCODING) as file:
        clean_list = []

        while line := file.readline():
            clean_line = " ".join(line.replace("&nbsp;", " ").split())
            if clean_line:
                clean_list.append(clean_line)

    clean_text = " ".join(clean_list).lower()

    if searching_phrase in clean_text:
        print(file_name)
        not_found = False

if not_found:
    print("404. Not Found")
