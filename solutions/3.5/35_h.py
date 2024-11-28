DEFAULT_ENCODING = {"encoding": "UTF-8"}
sets = []

for index in range(2):
    file_in = input()
    set_of_words = set()

    with open(file_in, "r", **DEFAULT_ENCODING) as file:
        while line := file.readline():
            words = line.rstrip("\n").split()
            set_of_words.update(words)

    sets.append(set_of_words)

sorted_unique_words = sorted(sets[0] ^ sets[1])

file_out = input()
with open(file_out, "w", **DEFAULT_ENCODING) as file_out:
    file_out.write("\n".join(sorted_unique_words))
