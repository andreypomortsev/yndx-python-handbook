petya = 7
vasya = 6
petya, vasya = petya - 3 + 2, vasya + 3 + 5 - 2

n, m = int(input()), int(input())

petya += n
vasya += m

if petya > vasya:
    print("Петя")
elif petya < vasya:
    print("Вася")
else:
    print("Ровно")
