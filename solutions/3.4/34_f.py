from itertools import product

suits = ["пик", "треф", "бубен", "червей"]
pips_and_faces = list(range(2, 11))
pips_and_faces += ["валет", "дама", "король", "туз"]

suit_to_remove = input()
suits.remove(suit_to_remove)

for pip_or_face, suit in product(pips_and_faces, suits):
    print(pip_or_face, suit)
