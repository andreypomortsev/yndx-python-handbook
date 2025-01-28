import string

import pandas as pd


def length_stats(text: str) -> pd.Series:
    text = text.lower()

    # Удаление знаков препинания и цифр
    # Remove punctuation and digits
    translator = str.maketrans("", "", string.punctuation + string.digits)
    cleaned_text = text.translate(translator)

    words = cleaned_text.split()
    words_series = pd.Series(words)

    # Вычисление длин слов
    # Calculate word lengths
    word_lengths = words_series.str.len()

    # Удаление дубликатов и сортировка
    # Remove duplicates and sort
    word_lengths = word_lengths.groupby(words_series).max()

    return word_lengths
