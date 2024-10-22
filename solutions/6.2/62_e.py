import pandas as pd


def get_long(data: pd.Series, min_length: int = 5) -> pd.Series:
    return data[data >= min_length]
