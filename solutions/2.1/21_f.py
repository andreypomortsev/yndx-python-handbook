name = input()
price = int(input())
weight = int(input())
bill = int(input())

total = price * weight
change = bill - total

answer = f"""Чек
{name} - {weight}кг - {price}руб/кг
Итого: {total}руб
Внесено: {bill}руб
Сдача: {change}руб"""

print(answer)
