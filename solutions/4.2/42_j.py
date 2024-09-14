def secret_replace(text: str, **replaces) -> str:
    repeats = {}
    encoded = []

    for char in text:
        if char in replaces:
            if char not in repeats:
                repeats[char] = 0
            elif repeats[char] < len(replaces[char]) - 1:
                repeats[char] += 1
            else:
                repeats[char] = 0

            encoded_char_index = repeats[char]
            encoded_char = replaces[char][encoded_char_index]
            encoded.append(encoded_char)

        else:
            encoded.append(char)

    return "".join(encoded)
