name = input()
price = int(input())
weight = int(input())
bill = int(input())

total = weight * price
change = bill - total
price_line = f"{weight}кг * {price}руб/кг"
receipt_header = f"{'Чек':=^35}"

receipt = (
    f"{receipt_header}\n"
    f"Товар:{name: >29}\n"
    f"Цена:{price_line: >30}\n"
    f"Итого:{total: >26}руб\n"
    f"Внесено:{bill: >24}руб\n"
    f"Сдача:{change: >26}руб\n"
    f"{"":=^35}"
)
print(receipt)
