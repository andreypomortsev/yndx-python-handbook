repeat = int(input())
phrase = input()

phrase_to_print = f'Я больше никогда не буду писать "{phrase}"!\n' * repeat

print(phrase_to_print, end="")
