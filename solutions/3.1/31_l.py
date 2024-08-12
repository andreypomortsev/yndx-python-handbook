PORRIDGE = ("Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая")

n = int(input())

number_of_porridge = len(PORRIDGE)
quotient = n // number_of_porridge
remainder = n % number_of_porridge

for i in range(quotient):
    print(*PORRIDGE, sep="\n")

if remainder:
    print(*PORRIDGE[:remainder], sep="\n")
