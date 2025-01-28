point_a = int(input())
point_b = int(input())
speed = int(input())

distance = ((point_b - point_a) ** 2) ** 0.5
time_to_destination = distance / speed

print(f"{time_to_destination:.2f}")
