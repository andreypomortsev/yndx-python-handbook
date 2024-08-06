x, y = 0, 0
is_direction = False

while (word := input()) != "СТОП":
    if is_direction:
        direction = word
        is_direction = True
    else:
        steps = int(word)
        match direction:
            case "СЕВЕР":
                x += steps
            case "ЮГ":
                x -= steps
            case "ВОСТОК":
                y += steps
            case "ЗАПАД":
                y -= steps
        is_direction = False

print(x, y, sep="\n")
