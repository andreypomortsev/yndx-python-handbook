TRANS_DICT = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "ZH",
    "З": "Z",
    "И": "I",
    "Й": "I",
    "К": "K",
    "Л": "L",
    "М": "M",
    "Н": "N",
    "О": "O",
    "П": "P",
    "Р": "R",
    "С": "S",
    "Т": "T",
    "У": "U",
    "Ф": "F",
    "Х": "KH",
    "Ц": "TC",
    "Ч": "CH",
    "Ш": "SH",
    "Щ": "SHCH",
    "Ы": "Y",
    "Э": "E",
    "Ю": "IU",
    "Я": "IA",
    "Ь": "",
    "Ъ": "",
}


with open("cyrillic.txt", "r", encoding="UTF-8") as file_in, open(
    "transliteration.txt", "w", encoding="UTF-8"
) as file_out:
    while cyrillic_line := file_in.readline():
        latin_text = []
        for char in cyrillic_line:
            trans_char = TRANS_DICT.get(char.upper(), char)
            if char.isupper():
                latin_text.append(trans_char.capitalize())
            else:
                latin_text.append(trans_char.lower())
        file_out.writelines(latin_text)
