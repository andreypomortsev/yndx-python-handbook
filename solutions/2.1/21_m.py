children = int(input())
candies = int(input())
if children:
    candies_per_child = candies // children
    candies_left = candies - candies_per_child * children
else:
    candies_left = candies
    candies_per_child = children
print(candies_per_child, candies_left, sep="\n")
