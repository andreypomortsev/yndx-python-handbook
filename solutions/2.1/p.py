point_a = int(input())
point_b = int(input())
speed = int(input())
distance = ((point_b - point_a) ** 2) ** 0.5
time_to_point_b = distance / speed
print(f"{time_to_point_b:.2f}")
