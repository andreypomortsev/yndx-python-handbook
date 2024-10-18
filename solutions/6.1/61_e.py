import math

point_one = tuple(map(float, input().split()))
r, theta = map(float, input().split())
point_two = r * math.cos(theta), r * math.sin(theta)

distance = math.dist(point_one, point_two)
print(distance)
