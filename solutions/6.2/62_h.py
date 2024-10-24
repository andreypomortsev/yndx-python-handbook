import pandas as pd


def update(df: pd.DataFrame) -> pd.DataFrame:
    df_copy = df.copy()

    df_copy["average"] = df_copy.iloc[:, 1:].mean(axis=1)
    params = {"by": ["average", "name"], "ascending": [False, True]}

    return df_copy.sort_values(**params)
