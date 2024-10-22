import string

import pandas as pd


def length_stats(text: str) -> pd.Series:
    # Преобразование текста в нижний регистр
    text = text.lower()

    # Удаление знаков препинания и цифр
    translator = str.maketrans("", "", string.punctuation + string.digits)
    cleaned_text = text.translate(translator)

    # Разделение текста на слова и создание Series
    words = cleaned_text.split()
    words_series = pd.Series(words)

    # Вычисление длин слов
    word_lengths = words_series.str.len()

    # Удаление дубликатов и сортировка
    word_lengths = word_lengths.groupby(words_series).max()

    return word_lengths
