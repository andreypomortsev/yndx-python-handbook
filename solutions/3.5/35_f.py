DEFAULT_ENCODING = {"encoding": "UTF-8"}
TRANS_DICT = {
    "А": "A",
    "Б": "B",
    "В": "V",
    "Г": "G",
    "Д": "D",
    "Е": "E",
    "Ё": "E",
    "Ж": "Zh",
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
    "Х": "Kh",
    "Ц": "Tc",
    "Ч": "Ch",
    "Ш": "Sh",
    "Щ": "Shch",
    "Ы": "Y",
    "Э": "E",
    "Ю": "Iu",
    "Я": "Ia",
    "Ь": "",
    "Ъ": "",
}

with (
    open("cyrillic.txt", "r", **DEFAULT_ENCODING) as file_in,
    open("transliteration.txt", "w", **DEFAULT_ENCODING) as file_out,
):
    while cyrillic_line := file_in.readline():
        latin_text = []
        for char in cyrillic_line:
            trans_char = TRANS_DICT.get(char.upper(), char)
            if char.isupper():
                latin_text.append(trans_char)
            else:
                latin_text.append(trans_char.lower())
        file_out.writelines(latin_text)
