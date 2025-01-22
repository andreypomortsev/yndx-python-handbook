import math
import sys

gcds = [str(math.gcd(*map(int, line.split()))) for line in sys.stdin]
print("\n".join(gcds), sep="\n")
