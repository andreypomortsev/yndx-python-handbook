LENGTH = 26  # Длина английского алфавита
ENGLISH_Z = ord("z")  # 122

shift = int(input()) % LENGTH

with (
    open("public.txt", "r", encoding="UTF-8") as file_in,
    open("private.txt", "w", encoding="UTF-8") as file_out,
):
    while line := file_in.readline():
        encrypted_line = []

        for char in line:
            if char.isalpha():
                code_point = ord(char.lower())
                shifted_code_point = code_point + shift

                if shifted_code_point > ENGLISH_Z:
                    shifted_code_point -= LENGTH

                new_char = chr(shifted_code_point)

                if char.isupper():
                    new_char = new_char.upper()
            else:
                new_char = char

            encrypted_line.append(new_char)

        file_out.write("".join(encrypted_line))
