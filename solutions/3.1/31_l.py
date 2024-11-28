PORRIDGE = ["Манная", "Гречневая", "Пшённая", "Овсяная", "Рисовая"]
LENGTH = 5  # len(PORRIDGE)

n = int(input())

for i in range(n):
    print(PORRIDGE[i % LENGTH])
