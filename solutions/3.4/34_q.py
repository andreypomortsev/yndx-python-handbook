from itertools import combinations, product

given_suit = input()
pip_to_drop = input()
blueprint = input()

card_suits = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}
suit = card_suits[given_suit]

PIPS_AND_FACES = [
    "10",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "валет",
    "дама",
    "король",
    "туз",
]
PIPS_AND_FACES.remove(pip_to_drop)

all_possible_cards = list(product(PIPS_AND_FACES, card_suits.values()))
combinations_of_cards = combinations(all_possible_cards, 3)

flag = False

for combination in combinations_of_cards:
    formatted_combination = []
    suit_in_combination = False

    for card in combination:
        if not suit_in_combination:
            suit_in_combination = suit in card
        formatted_combination.append(" ".join(card))

    formatted_combination = ", ".join(formatted_combination)

    if flag and suit_in_combination:
        print(formatted_combination)
        break

    if formatted_combination == blueprint:
        flag = True
