numbers_file = input()
even_file = input()
odd_file = input()
eq_file = input()

with (
    open(numbers_file, "r", encoding="UTF-8") as file_in,
    open(even_file, "w", encoding="UTF-8") as even_out,
    open(odd_file, "w", encoding="UTF-8") as odd_out,
    open(eq_file, "w", encoding="UTF-8") as equal_out,
):

    while line := file_in.readline():
        even_list, odd_list, equal_list = [], [], []
        for str_number in line.split():
            length = len(str_number)
            even, odd = 0, 0

            for i in range(length):
                digit = int(str_number[i])

                even += digit % 2 == 0
                odd += digit % 2 != 0

            if even == odd:
                equal_list.append(str_number)
            elif even > odd:
                even_list.append(str_number)
            else:
                odd_list.append(str_number)

        even_out.write(f"{' '.join(even_list)}\n")
        odd_out.write(f"{' '.join(odd_list)}\n")
        equal_out.write(f"{' '.join(equal_list)}\n")
