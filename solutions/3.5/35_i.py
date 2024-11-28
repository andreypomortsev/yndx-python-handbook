DEFAULT_ENCODING = {"encoding": "UTF-8"}

file_to_clean = input()
clean_file = input()

with (
    open(file_to_clean, "r", **DEFAULT_ENCODING) as file_in,
    open(clean_file, "w", **DEFAULT_ENCODING) as file_out,
):
    while line := file_in.readline():
        words = line.replace("\t", "").split()
        if words:
            file_out.write(" ".join(words) + "\n")
