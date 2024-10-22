import string

import pandas as pd


def length_stats(text: str) -> tuple:
    text = text.lower()

    translator = str.maketrans("", "", string.punctuation + string.digits)
    cleaned_text = text.translate(translator)

    sorted_list = sorted(cleaned_text.split())

    dicts = {
        "even": {word: len(word) for word in sorted_list if not len(word) % 2},
        "odd": {word: len(word) for word in sorted_list if len(word) % 2},
    }

    odd = pd.Series(dicts["odd"], dtype="int64")
    even = pd.Series(dicts["even"], dtype="int64")

    return odd, even
