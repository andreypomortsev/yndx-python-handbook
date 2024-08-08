n, m = int(input()), int(input())

ENDS = "\n "
prod_nm = n * m
array = range(1, prod_nm + 1)
formatter = 0

while prod_nm > 0:
    formatter += 1
    prod_nm //= 10

for num in array:
    print(f"{num:>{formatter}}", end=ENDS[bool(num % m)])
