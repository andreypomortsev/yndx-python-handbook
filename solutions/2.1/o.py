hours = int(input())
minutes = int(input())
delivery_time = int(input())

if delivery_time < 60:
    minutes += delivery_time
elif delivery_time > 60:
    hours += delivery_time // 60
    minutes += delivery_time % 60
else:
    hours += 1

if minutes >= 60:
    hours += minutes // 60
    minutes = minutes % 60

if hours > 23:
    hours %= 24

print(f"{hours:02d}:{minutes:02d}")  # noqa E231
