name = input()
price = int(input())
weight = int(input())
bill = int(input())
total = weight * price
change = bill - total
price_line = f"{weight}кг * {price}руб/кг"

# Считаем пробелы для выравнивания
name_spaces = 35 - len(name) - len("Товар:")
price_line_spaces = 35 - len(price_line) - len("Цена:")
total_spaces = 35 - len(str(total)) - len("Итого:") - len("руб")
bill_spaces = 35 - len(str(bill)) - len("Внесено:") - len("руб")
change_spaces = 35 - len(str(change)) - len("Сдача:") - len("руб")

receipt = f"""{"Чек".center(35, '=')}
Товар:{' ' * name_spaces}{name}
Цена:{' ' * price_line_spaces}{price_line}
Итого:{' ' * total_spaces}{total}руб
Внесено:{' ' * bill_spaces}{bill}руб
Сдача:{' ' * change_spaces}{change}руб
{'=' * 35}"""

print(receipt)
