name = input()
price = int(input())
weight = int(input())
bill = int(input())
total = int(price * weight)
change = bill - total
print(
    f"""Чек
{name} - {weight}кг - {price}руб/кг
Итого: {total}руб
Внесено: {bill}руб
Сдача: {change}руб"""
)
