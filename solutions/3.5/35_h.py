file_one = input()
file_two = input()
file_out = input()

with open(file_one, "r", encoding="UTF-8") as file:
    first_set = set()
    while line := file.readline():
        words = line.rstrip("\n").split()
        first_set.update(words)

with open(file_two, "r", encoding="UTF-8") as file:
    second_set = set()
    while line := file.readline():
        words = line.rstrip("\n").split()
        second_set.update(words)

unique_words = sorted(first_set ^ second_set)

with open(file_out, "w", encoding="UTF-8") as file_out:
    file_out.write("\n".join(unique_words))
