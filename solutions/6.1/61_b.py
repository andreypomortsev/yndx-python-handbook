import math
import sys

gcds = [math.gcd(*map(int, line.split())) for line in sys.stdin]
print(*gcds, sep="\n")
