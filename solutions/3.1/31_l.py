PORRIDGE = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]

n = int(input())

number_of_porridge = len(PORRIDGE)

for i in range(n):
    print(PORRIDGE[i % number_of_porridge])
