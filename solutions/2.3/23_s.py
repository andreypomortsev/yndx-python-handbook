low = 1
high = 1000
guess = (low + high) // 2
print(guess)

while (response := input()) != "Угадал!":
    match response:
        case "Больше":
            low = guess
        case "Меньше":
            high = guess
    guess = (low + high) // 2

    print(guess)
