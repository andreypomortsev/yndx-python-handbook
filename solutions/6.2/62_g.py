import pandas as pd


def need_to_work_better(journ: pd.DataFrame) -> pd.DataFrame:
    mask = (journ.iloc[:, 1:] == 2).any(axis=1)
    return journ[mask]
