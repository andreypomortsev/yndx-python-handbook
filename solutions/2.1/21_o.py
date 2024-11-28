hours = int(input())
minutes = int(input())
delivery_time = int(input())

hours += delivery_time // 60
minutes += delivery_time % 60

hours += minutes // 60
minutes = minutes % 60

hours %= 24

print(f"{hours:02d}:{minutes:02d}")
