from itertools import permutations, product

given_suit = input().strip()
pip_to_drop = input()

CARD_SUITS = {
    "буби": "бубен",
    "пики": "пик",
    "трефы": "треф",
    "черви": "червей",
}
suit = CARD_SUITS[given_suit]

pips_and_faces = list(map(str, range(2, 11)))
pips_and_faces += ["валет", "дама", "король", "туз"]
pips_and_faces.remove(pip_to_drop)

products = sorted(
    map(lambda x: " ".join(x), product(pips_and_faces, CARD_SUITS.values()))
)
counter = 0

for line in permutations(products, 3):
    if counter == 10:
        break
    elif any(suit in item for item in line):
        print(", ".join(sorted(line)))
        counter += 1
