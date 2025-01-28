DEFAULT_ENCODING = {"encoding": "UTF-8"}
FILE_NAME = "secret.txt"

with open(FILE_NAME, "r", **DEFAULT_ENCODING) as file:
    while line := file.readline():
        hidden_word = []

        for char in line:
            code_point = ord(char)

            if code_point < 128:
                hidden_word.append(char)
            else:
                # Приемняем маску для получения младшего байта
                # Тот же эффект даст: code_point % 256
                # Apply mask to get lower byte
                # The same effect will give: code_point % 256
                lower_byte = code_point & 0xFF
                hidden_char = chr(lower_byte)
                hidden_word.append(hidden_char)

        print("".join(hidden_word), end="")
