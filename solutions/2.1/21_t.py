weight = int(input())
price_tag = int(input())
price_one = int(input())
price_two = int(input())

x = weight * (price_tag - price_two) // (price_one - price_two)
print(x, weight - x)
