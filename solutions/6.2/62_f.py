import pandas as pd


def best(journ: pd.DataFrame) -> pd.DataFrame:
    mask = (journ.iloc[:, 1:] > 3).all(axis=1)

    return journ[mask]
