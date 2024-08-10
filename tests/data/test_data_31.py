a_test_data = [
    ("3\nарбуз\nбарабан\nворона\n", "YES\n", "first open test"),
    ("4\nаист\nвареник\nкузнечик\nалыча\n", "NO\n", "second open test"),
    ("1\nаист\n", "YES\n", "one line a yes"),
    ("1\nбелка\n", "YES\n", "one line b yes"),
    ("1\nворон\n", "YES\n", "one line v yes"),
    ("1\nаист\n", "YES\n", "one line yes"),
    ("1\nмаист\n", "NO\n", "one line no"),
    (
        "12\n"
        "аист\nвареник\nбаран\n"
        "аист\nвареник\nбаран\n"
        "аист\nвареник\nбаран\n"
        "аист\nвареник\nбаран\n",
        "YES\n",
        "many lines yes",
    ),
    (
        "12\n"
        "аист\nвареник\nбаран\n"
        "аист\nвареник\nбаран\n"
        "аист\nвареник\nбаран\n"
        "аист\nвареник\nкабан\n",
        "NO\n",
        "many lines no",
    ),
]

b_test_data = [
    ("Привет\n", "П\nр\nи\nв\nе\nт\n", "first open test"),
    ("Питон\n", "П\nи\nт\nо\nн\n", "second open test"),
    (
        "Привет, Питон!\n",
        "П\nр\nи\nв\nе\nт\n,\n \nП\nи\nт\nо\nн\n!\n",
        "hello, python!",
    ),
    (
        "CaMeL CaSe StRiNg\n",
        "C\na\nM\ne\nL\n \nC\na\nS\ne\n \nS\nt\nR\ni\nN\ng\n",
        "camel case",
    ),
    (" \n", " \n", "whitespace"),
    ("12345\n", "1\n2\n3\n4\n5\n", "digits"),
    ("!@#$%^&*()\n", "!\n@\n#\n$\n%\n^\n&\n*\n(\n)\n", "special chars"),
]

c_test_data = [
    (
        "25\n"
        "3\n"
        "Начался саммит по глобальному потеплению\n"
        "Завтра Новый год!\n"
        "Python и Java конкурируют за звание самого популярного языка программирования\n",
        "Начался саммит по глоб...\n"
        "Завтра Новый год!\n"
        "Python и Java конкурир...\n",
        "first open test",
    ),
    (
        "17\n"
        "3\n"
        "Начался саммит по глобальному потеплению\n"
        "Завтра Новый год!\n"
        "Python и Java конкурируют за звание самого популярного языка программирования\n",
        "Начался саммит...\n" "Завтра Новый год!\n" "Python и Java ...\n",
        "equal to the threshold",
    ),
]
d_test_data = [
    (
        "Hello, world\nHello, @@@\n##Goodbye\n\n",
        "Hello, world\nGoodbye\n",
        "first open test",
    ),
    (
        "First Message\n"
        "##Second Message\n"
        "@@@Third Message##\n"
        "##Fourth Message@@@\n"
        "\n",
        "First Message\nSecond Message\n@@@Third Message##\n",
        "second open test",
    ),
    (
        "First ## Message\n"
        "##Second ##Message\n"
        "@@@Third Message##\n"
        "## Fourth Message @@@\n"
        "\n",
        "First ## Message\nSecond ##Message\n@@@Third Message##\n",
        "## in the middle",
    ),
    (
        "First Message\n"
        "###Comment\n"
        "@@@Third Message##\n"
        "##Fourth Message@@@\n"
        "\n",
        "First Message\n#Comment\n@@@Third Message##\n",
        "# three of 'em",
    ),
    (
        " \n"
        "### Comment\n"
        "@@@ Third Message ##\n"
        "##Fourth Message@@@\n"
        "\n",
        " \n# Comment\n@@@ Third Message ##\n",
        "whitespace",
    ),
]

e_test_data = [
    ("мама\n", "NO\n", "first open test"),
    ("анна\n", "YES\n", "second open test"),
    ("маммонт\n", "NO\n", "odd length"),
    ("\n", "YES\n", "no input"),
    ("race truck\n", "NO\n", "two words"),
    ("racecar\n", "YES\n", "race car"),
    ("Racecar\n", "NO\n", "Race car"),
    ("12 21\n", "YES\n", "two numbers"),
]

f_test_data = [
    (
        "3\nберезка елочка зайка волк березка\n"
        "сосна зайка сосна елочка зайка медведь\n"
        "сосна сосна сосна белочка сосна белочка\n",
        "3\n",
        "first open test",
    ),
    (
        "4\nзайка березка\n"
        "березка зайка\n"
        "березка елочка березка\n"
        "елочка елочка елочка\n",
        "2\n",
        "second open test",
    ),
    (
        "1\nзайка березка\n",
        "1\n",
        "one line with a bunny",
    ),
    (
        "1\nЗайка березка\n",
        "1\n",
        "one line with a Bunny",
    ),
    (
        "1\nЗАЙКА березка\n",
        "1\n",
        "one line with a BUNNY",
    ),
    (
        "1\nелочка сосна березка елочка\n",
        "0\n",
        "one line w/o a bunny",
    ),
    (
        "4\nзайка зайка\n"
        "зайка зайка зайка зайка зайка\n"
        "зайка зайка зайка зайка зайка зайка зайка зайка зайка\n"
        "зайка зайка зайка\n",
        "19\n",
        "all words are bunnies",
    ),
    (
        "4\nберезка березка березка березка березка березка березка\n"
        "березка березка березка березка березка\n"
        "березка березка березка березка березка березка березка березка березка\n"
        "березка березка березка\n",
        "0\n",
        "forest w/o bunnies",
    ),
    (
        "1\n \n",
        "0\n",
        "one whitespace line w/o bunny",
    ),
    (
        "3\n \n \nзайка\n",
        "1\n",
        "2 whitespace-lines one line with bunny",
    ),
]

g_test_data = [
    ("2 2\n", "4\n", "first open test"),
    ("-3 5\n", "2\n", "second open test"),
    ("3 -5\n", "-2\n", "second open test swap"),
    ("0 2\n", "2\n", "zero and positive"),
    ("10 0\n", "10\n", "positive and zero"),
    ("0 -2\n", "-2\n", "zero and negative"),
    ("-10 0\n", "-10\n", "negative and zero"),
    ("-3 -5\n", "-8\n", "two negative numbers"),
    ("0 0\n", "0\n", "two zeros"),
    ("10_000_000_001 9_999_999_999\n", "20000000000\n", "big numbers"),
]

h_test_data = [
    (
        "3\nберезка елочка зайка волк березка\n"
        "сосна зайка сосна елочка зайка медведь\n"
        "сосна сосна сосна белочка сосна белочка\n",
        "16\n7\nЗаек нет =(\n",
        "first open test",
    ),
    (
        "4\nзайка березка\n"
        "березка зайка\n"
        "березка елочка березка\n"
        "елочка елочка елочка\n",
        "1\n9\nЗаек нет =(\nЗаек нет =(\n",
        "second open test",
    ),
    (
        "4\nберезка березка\n"
        "березка березка\n"
        "березка елочка березка\n"
        "елочка елочка елочка\n",
        "Заек нет =(\nЗаек нет =(\nЗаек нет =(\nЗаек нет =(\n",
        "many rows no bunnies",
    ),
    (
        "5\nзайка\n"
        " зайка\n"
        "  зайка\n"
        "   зайка зайка зайка\n"
        "    зайка зайка зайка зайка\n",
        "1\n2\n3\n4\n5\n",
        "many rows whitespace beginnings bunnies",
    ),
    (
        "5\nзайка\n"
        "-зайка\n"
        "=+зайка\n"
        "!!!зайка зайка зайка\n"
        "....зайка зайка зайка зайка\n",
        "1\n2\n3\n4\n5\n",
        "many rows special char beginnings bunnies",
    ),
    ("1\n                   \n", "Заек нет =(\n", "long empty line"),
    ("2\n                   \nя_зайка", "Заек нет =(\n3\n", "tricky line"),
]

i_test_data = [
    (
        "# Моя первая супер-пупер программа\n"
        'print("What is your name?") #  Как тебя зовут?\n'
        "name = input() #  Сохраняем имя\n"
        'print(f"Hello, {name}!") #  Здороваемся# Конец моей супер-пупер программы\n'
        "\n",
        'print("What is your name?")\n'
        "name = input()\n"
        'print(f"Hello, {name}!")\n',
        "first open test",
    ),
    (
        "# Мой первый цикл\n"
        "for i in range(10): # Считаем до 10\n"
        "    print(i) # выводим число\n"
        "\n",
        "for i in range(10):\n    print(i)\n",
        "second open test",
    ),
    (
        "while (line := input()):\n"
        '    index = line.find("#")\n'
        "    if not index:\n"
        "        continue\n"
        "    if index > 0:\n"
        "        print(line[:index])\n"
        "    else:\n"
        "        print(line)\n\n",
        "while (line := input()):\n"
        '    index = line.find("#")\n'
        "    if not index:\n"
        "        continue\n"
        "    if index > 0:\n"
        "        print(line[:index])\n"
        "    else:\n"
        "        print(line)\n",
        "a wrong solution",
    ),
    (
        "# Верное решение\n"
        "while line := input():\n"
        '    index = line.find("#") # Я надеюсь\n'
        "    if index == -1:\n"
        "        print(line)\n"
        "        continue\n"
        "    if not index:\n"
        "        continue\n"
        "    stack = "
        "\n"
        "    flag = False\n"
        "    for i in range(len(line)):\n"
        "        char = line[i]\n"
        """        if char in "\"'":\n"""
        "            if not stack:\n"
        "                stack += char\n"
        "            elif char == stack[-1]:\n"
        "                stack = stack[:-1]\n"
        "        if char == '#' and not stack:\n"
        '            print(f"{line[:i].rstrip()}")\n'
        "            flag = True\n"
        "            break\n"
        "    if not flag:\n"
        "        print(line)\n\n",
        "while line := input():\n"
        '    index = line.find("#")\n'
        "    if index == -1:\n"
        "        print(line)\n"
        "        continue\n"
        "    if not index:\n"
        "        continue\n"
        "    stack = "
        "\n"
        "    flag = False\n"
        "    for i in range(len(line)):\n"
        "        char = line[i]\n"
        """        if char in "\"'":\n"""
        "            if not stack:\n"
        "                stack += char\n"
        "            elif char == stack[-1]:\n"
        "                stack = stack[:-1]\n"
        "        if char == '#' and not stack:\n"
        '            print(f"{line[:i].rstrip()}")\n'
        "            flag = True\n"
        "            break\n"
        "    if not flag:\n"
        "        print(line)\n",
        "the right solution",
    ),
    (
        """print("вася") # ну не "петя" же \n\n""",
        'print("вася")\n',
        "Nikolai's test",
    ),
]

j_test_data = [
    ("Баобаб\nБелка\nБобы\nФИНИШ\n", "б\n", "first open test"),
    (
        "Финики Фокачча Зайка\n"
        "Филин Фосфор Светофор\n"
        "Фехтовальщик Форма\n"
        "ФИНИШ\n",
        "ф\n",
        "second open test",
    ),
    ("Финиш\nФИНИш\nфиниш\nфф\nФИНИШ\n", "и\n", "it's not finish yet"),
    ("вввв\nбббб\nаааа\nФИНИШ\n", "а\n", "tie"),
    ("      \n     \nАААААА\nФИНИШ\n", "а\n", "whitespaces and A"),
]
