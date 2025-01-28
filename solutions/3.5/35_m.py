import ast
import json
from sys import stdin

DEFAULT_ENCODING = {"encoding": "UTF-8"}

json_file = input()
with open(json_file, "r+", **DEFAULT_ENCODING) as file:
    json_to_update = json.load(file)

    for line in stdin:
        key, value = line.rstrip("\n").split(" == ")
        try:
            value = ast.literal_eval(value)
        except (ValueError, SyntaxError):
            pass
        json_to_update[key] = value

    # Двигаем указатель в начало файла
    # Move the file pointer to the beginning of the file
    file.seek(0)

    # Записываем обновленное содержание в файл
    # Write the updated content to the file
    json.dump(json_to_update, file, ensure_ascii=False, indent=4)

    # Обрезаем все отсатки "старого файла"
    # Truncate all the remains of the "old file"
    file.truncate()
