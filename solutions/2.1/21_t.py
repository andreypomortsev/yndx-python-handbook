total_weight = int(input())
price_tag = int(input())
price_one = int(input())
price_two = int(input())

first_batch = total_weight * (price_tag - price_two) // (price_one - price_two)
second_batch = total_weight - first_batch

print(first_batch, second_batch)
