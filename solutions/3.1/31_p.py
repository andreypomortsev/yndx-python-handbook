max_length = int(input()) - 3  # Поправка на ...
n = int(input())

headlines = []
all_lengths = 0
cum_length = 0

for _ in range(n):
    line = input()
    headlines.append(line)
    all_lengths += len(line)

for line in headlines:
    cum_length += len(line)
    if all_lengths <= max_length + 3:
        print(line)
    elif all_lengths >= cum_length >= max_length:
        index = (max_length + (cum_length == max_length)) - cum_length
        print(f"{line[:index]}...")
        break
    else:
        print(line)
