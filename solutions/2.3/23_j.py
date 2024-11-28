x = y = 0
is_direction = True

while (word := input()) != "СТОП":
    if is_direction:
        direction = word
        is_direction = False
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
        is_direction = True

print(x, y, sep="\n")
