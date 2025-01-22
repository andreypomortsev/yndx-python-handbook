DEFAULT_ENCODING = "UTF-8"
SIZE = 32

file_name = input()
tail = int(input()) + 1

with open(file_name, "rb") as file:
    file.seek(0, 2)
    pointer_location = file.tell()
    buffer = bytearray()

    read_lines = 0
    lines = []

    while pointer_location > 0 and read_lines <= tail + 1:
        chunk_size = min(pointer_location, SIZE)
        file.seek(pointer_location - chunk_size)
        pointer_location -= chunk_size

        chunk = file.read(chunk_size)
        chunk = chunk.replace(b"\r\n", b"\n")  # Windows to Unix

        buffer = chunk + buffer
        lines = buffer.split(b"\n")
        read_lines = len(lines)

        if read_lines >= tail + 1:
            break


for line in lines[-tail:]:
    line_to_print = line.decode(DEFAULT_ENCODING)
    print(line_to_print)
