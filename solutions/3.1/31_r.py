binary = input()

last_char = binary[0]
counter = 1

for i in range(1, len(binary)):
    if binary[i] != last_char:
        print(last_char, counter)
        last_char = binary[i]
        counter = 1
    else:
        counter += 1

print(last_char, counter)
