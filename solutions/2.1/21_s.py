name = input()
price = int(input())
weight = int(input())
bill = int(input())

total = weight * price
change = bill - total
price_line = f"{weight}кг * {price}руб/кг"

receipt = f"""{"Чек":=^35}
Товар:{name: >29}
Цена:{price_line: >30}
Итого:{total: >26}руб
Внесено:{bill: >24}руб
Сдача:{change: >26}руб
{"":=^35}"""

print(receipt)
