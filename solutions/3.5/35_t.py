BYTES = 2
sum_of_numbers = 0

with open("numbers.num", "rb") as file:
    while chunk := file.read(BYTES):
        sum_of_numbers += int.from_bytes(chunk, byteorder="big")

# Make sure that the sum of numbers is not bigger than 2 bytes
sum_of_numbers %= 256**BYTES
print(sum_of_numbers)
