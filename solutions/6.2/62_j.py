from typing import Callable

import numpy as np
import pandas as pd


def values(
    func: Callable[[int | float], float], start: float, end: float, step: float
) -> pd.Series:
    indecies = np.arange(start, end + step, step)
    values = np.vectorize(func)(indecies)
    return pd.Series(values, index=indecies)


def min_extremum(data: pd.Series) -> float:
    min_index = np.argmin(data.values)
    return data.index[min_index]


def max_extremum(data: pd.Series) -> float:
    max_index = np.argmax(data.values)
    return data.index[max_index]
