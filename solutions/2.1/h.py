repeat, phrase = int(input()), input()
phrase_to_print = f'Я больше никогда не буду писать "{phrase}"!\n' * repeat
print(phrase_to_print.rstrip("\n"))
