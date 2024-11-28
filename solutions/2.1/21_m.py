children = int(input())
candy = int(input())

candy_per_child = candy // children
candy_left = candy % children

print(candy_per_child, candy_left, sep="\n")
