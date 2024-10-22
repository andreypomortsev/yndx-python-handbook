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
