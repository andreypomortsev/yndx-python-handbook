import pandas as pd


def cheque(price_list: pd.Series, **products) -> pd.DataFrame:
    return (
        pd.DataFrame({"product": price_list.index, "price": price_list.values})
        .merge(
            pd.Series(products, name="number"),
            left_on="product",
            right_index=True,
        )
        .sort_values("product", ascending=True)
        .assign(cost=lambda x: x["price"] * x["number"])
        .reset_index(drop=True)
    )


def discount(cheque: pd.DataFrame) -> pd.DataFrame:
    cheque_c = cheque.copy()  # By default deep = True
    mask = cheque_c["number"] > 2

    cheque_c["cost"] = cheque_c["cost"].astype(float)
    cheque_c.loc[mask, "cost"] *= 0.5

    return cheque_c
