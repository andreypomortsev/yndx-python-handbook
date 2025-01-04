BYTES = 2
sum_of_numbers = 0

with open("numbers.num", "rb") as file:
    while chunk := file.read(BYTES):
        sum_of_numbers += int.from_bytes(chunk, byteorder="big")

print(sum_of_numbers % 256**BYTES)
