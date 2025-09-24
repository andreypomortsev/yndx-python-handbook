score = 0


def move(player: str, number: int) -> None:
    global score

    if player == "Петя":
        score += number
        return
    if player == "Ваня":
        score -= number
        return


def game_over() -> str:
    global score

    if score > 0:
        return "Петя"
    elif score < 0:
        return "Ваня"
    else:
        return "Ничья"
