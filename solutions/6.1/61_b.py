import math
import sys

for line in sys.stdin:
    gcd = math.gcd(*map(int, line.split()))
    print(gcd)
