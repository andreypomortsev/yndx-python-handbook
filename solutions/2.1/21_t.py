weight = int(input())
price_tag = int(input())
price_one = int(input())
price_two = int(input())

x = (price_tag * weight - price_two * weight) // (price_one - price_two)
print(x, weight - x)
