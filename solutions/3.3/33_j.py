[
    word
    for word in words.split()
    if len(
        [
            char
            for char in word
            if char.lower()
            in {
                "а",
                "я",
                "у",
                "ю",
                "о",
                "ё",
                "э",
                "е",
                "и",
                "ы",
                "a",
                "e",
                "i",
                "o",
                "u",
                "y",
            }
        ]
    )
    > 2
]
