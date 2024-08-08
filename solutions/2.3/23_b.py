banny_counter = 0

while (words := input()) != "Приехали!":
    banny_counter += "зайка" in words.lower()

print(banny_counter)
