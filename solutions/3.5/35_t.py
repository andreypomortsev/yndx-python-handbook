CHUNK_SIZE = 4096
sum_of_numbers = 0

with open("numbers.num", "rb") as file:
    while chunk := file.read(CHUNK_SIZE):
        for i in range(0, len(chunk) - 1, 2):
            # fmt: off
            two_bytes = chunk[i: i + 2]
            # fmt: on
            sum_of_numbers += int.from_bytes(two_bytes, byteorder="big")

print(sum_of_numbers & 0xFFFF)
