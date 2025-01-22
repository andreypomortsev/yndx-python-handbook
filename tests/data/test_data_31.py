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
        {
            'print("What is your name?")\n'
            "name = input()\n"
            'print(f"Hello, {name}!")\n',
            'print("What is your name?")\n'
            "name = input()\n"
            'print(f"Hello, {name}!")\n\n',
        },
        "first open test",
    ),
    (
        "# Мой первый цикл\n"
        "for i in range(10): # Считаем до 10\n"
        "    print(i) # выводим число\n"
        "\n",
        {
            "for i in range(10):\n    print(i)\n",
            "for i in range(10):\n    print(i)\n\n",
        },
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
        {
            "while (line := input()):\n"
            '    index = line.find("#")\n'
            "    if not index:\n"
            "        continue\n"
            "    if index > 0:\n"
            "        print(line[:index])\n"
            "    else:\n"
            "        print(line)\n",
            "while (line := input()):\n"
            '    index = line.find("#")\n'
            "    if not index:\n"
            "        continue\n"
            "    if index > 0:\n"
            "        print(line[:index])\n"
            "    else:\n"
            "        print(line)\n\n",
        },
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
        {
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
            "        print(line)\n\n",
        },
        "the right solution",
    ),
    (
        """print("вася") # ну не "петя" же \n\n""",
        {
            'print("вася")\n',
            'print("вася")\n\n',
        },
        "Nikolai's test",
    ),
    (
        're, stroka = "#", "#"\n'
        "while stroka != "
        ":\n"
        "    stroka = input()\n"
        "    t = stroka.split(re)\n"
        "    if not t[0].isspace() and len(t[0]) != 0:\n"
        "        print(t[0].rstrip())\n\n",
        {
            're, stroka = "#", "#"\n'
            "while stroka != "
            ":\n"
            "    stroka = input()\n"
            "    t = stroka.split(re)\n"
            "    if not t[0].isspace() and len(t[0]) != 0:\n"
            "        print(t[0].rstrip())\n",
            're, stroka = "#", "#"\n'
            "while stroka != "
            ":\n"
            "    stroka = input()\n"
            "    t = stroka.split(re)\n"
            "    if not t[0].isspace() and len(t[0]) != 0:\n"
            "        print(t[0].rstrip())\n\n",
        },
        "Valerii's test",
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

k_test_data = [
    (
        "3\nЯндекс выпустил задачник по программированию\n"
        "На соревнованиях по программированию победил любитель питона\n"
        "Как заказать Яндекс.Такси?!\n"
        "яндекс\n",
        "Яндекс выпустил задачник по программированию\n"
        "Как заказать Яндекс.Такси?!\n",
        "first open test",
    ),
    (
        "8\nсериал шерлок смотреть онлайн\n"
        "учебник питона\n"
        "мемы\n"
        "социальная сеть\n"
        "упражнения по питону\n"
        "кормовые мыши для питонов\n"
        "ответы егэ скачать бесплатно\n"
        "компьютерные мыши\n"
        "питон\n",
        "учебник питона\n"
        "упражнения по питону\n"
        "кормовые мыши для питонов\n",
        "second open test",
    ),
    (
        "8\nсериал шерлок смотреть онлайн\n"
        "учебник питона\n"
        "мемы\n"
        "социальная сеть\n"
        "упражнения по питону\n"
        "кормовые мыши для питонов\n"
        "ответы егэ скачать бесплатно\n"
        "компьютерные мыши\n"
        " \n",
        "сериал шерлок смотреть онлайн\n"
        "учебник питона\n"
        "социальная сеть\n"
        "упражнения по питону\n"
        "кормовые мыши для питонов\n"
        "ответы егэ скачать бесплатно\n"
        "компьютерные мыши\n",
        "in search of whitespace",
    ),
]

l_test_data = [
    ("3\n", "Манная\nГречневая\nПшённая\n", "first open test"),
    (
        "12\n",
        "Манная\n"
        "Гречневая\n"
        "Пшённая\n"
        "Овсяная\n"
        "Рисовая\n"
        "Манная\n"
        "Гречневая\n"
        "Пшённая\n"
        "Овсяная\n"
        "Рисовая\n"
        "Манная\n"
        "Гречневая\n",
        "second open test",
    ),
    (
        "1\n",
        "Манная\n",
        "one day",
    ),
    (
        "5\n",
        "Манная\nГречневая\nПшённая\nОвсяная\nРисовая\n",
        "five days",
    ),
    (
        "4\n",
        "Манная\nГречневая\nПшённая\nОвсяная\n",
        "four days",
    ),
    (
        "10\n",
        "Манная\n"
        "Гречневая\n"
        "Пшённая\n"
        "Овсяная\n"
        "Рисовая\n"
        "Манная\n"
        "Гречневая\n"
        "Пшённая\n"
        "Овсяная\n"
        "Рисовая\n",
        "two times the same",
    ),
]

m_test_data = [
    ("3\n2\n3\n4\n3\n", "8\n27\n64\n", "first open test"),
    (
        "5\n222222\n22222\n2222\n222\n22\n2\n",
        "49382617284\n493817284\n4937284\n49284\n484\n",
        "second open test",
    ),
    ("2\n5\n6\n2\n", "25\n36\n", "third open test"),
    ("4\n7\n8\n9\n10\n3\n", "343\n512\n729\n1000\n", "fourth open test"),
    ("1\n12345\n2\n", "152399025\n", "single number test"),
    (
        "3\n-2\n-3\n-4\n3\n",
        "-8\n-27\n-64\n",
        "first open test with negative nums odd power",
    ),
    ("3\n-2\n-3\n-4\n2\n", "4\n9\n16\n", "first open test with negative nums"),
]

n_test_data = [
    ("2 3 4\n3\n", {"8 27 64\n", "8 27 64", "8 27 64 "}, "first open test"),
    (
        "222222 22222 2222 222 22\n2\n",
        {
            "49382617284 493817284 4937284 49284 484\n",
            "49382617284 493817284 4937284 49284 484",
            "49382617284 493817284 4937284 49284 484 ",
        },
        "second open test",
    ),
    (
        "12345\n2\n",
        {"152399025\n", "152399025", "152399025 "},
        "single number",
    ),
    ("0\n3\n", {"0\n", "0", "0 "}, "zero in third"),
    ("1\n0\n", {"1\n", "1", "1 "}, "zero power one number"),
    (
        "-2 -3 -4\n3\n",
        {"-8 -27 -64\n", "-8 -27 -64", "-8 -27 -64 "},
        "negative numbers",
    ),
    (
        "0 1 2\n0\n",
        {"1 1 1\n", "1 1 1", "1 1 1 "},
        "zero power all numbers",
    ),
    (
        "999999999 888888888\n2\n",
        {
            "999999998000000001 790123455209876544\n",
            "999999998000000001 790123455209876544",
            "999999998000000001 790123455209876544 ",
        },
        "large numbers",
    ),
    (
        "123456789 987654321\n1\n",
        {
            "123456789 987654321\n",
            "123456789 987654321",
            "123456789 987654321 ",
        },
        "power of one",
    ),
    (
        "2 3 4\n-1\n",
        {
            "0.5 0.3333333333333333 0.25\n",
            "0.5 0.3333333333333333 0.25",
            "0.5 0.3333333333333333 0.25 ",
        },
        "negative power",
    ),
    ("4\n-1\n", {"0.25\n", "0.25", "0.25 "}, "negative power"),
    ("\n1\n", {"\n", "", " "}, "empty list"),
]

o_test_data = [
    ("12 42\n", "6\n", "first open test"),
    ("102 39 768\n", "3\n", "second open test"),
    ("-102 39 768\n", "3\n", "one negative"),
    ("48 180\n", "12\n", "common divisor test"),
    ("9 27 81\n", "9\n", "multiple common divisors test"),
    ("0 0\n", "0\n", "both zero test"),
    ("0 18\n", "18\n", "zero and positive number"),
    ("18 0\n", "18\n", "positive number and zero"),
    ("-18 -24\n", "6\n", "both negative"),
    ("18 -24\n", "6\n", "positive and negative"),
    ("24 -18\n", "6\n", "negative and positive"),
    ("1 1 1 1 1 1\n", "1\n", "all ones test"),
    ("0 0 0 0\n", "0\n", "all zeros test"),
    ("2 3 5 7 11\n", "1\n", "no common divisor test"),
    (
        "-2 -3 -5 -7 -11\n",
        "1\n",
        "negative numbers with no common divisor test",
    ),
    ("1024 2048 4096\n", "1024\n", "powers of two test"),
    ("9999991 99999931\n", "1\n", "large prime numbers test"),
    ("9999991 0\n", "9999991\n", "large prime and zero test"),
    (
        "9999991 99999931 999999937\n",
        "1\n",
        "multiple large prime numbers test",
    ),
    ("-9999991 -99999931\n", "1\n", "negative large prime numbers test"),
    ("12\n", "12\n", "single input"),
    ("0\n", "0\n", "single zero input"),
    ("-1234567890\n", "1234567890\n", "single large negative input"),
]

p_test_data = [
    (
        "144\n5\n"
        "Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана\n"
        "Благодаря ей он может регулировать громкость,\n"
        "показывая расстояние между большим и указательным пальцами.\n"
        "Для этого ему понадобилась веб-камера, знания Python и\n"
        "библиотека для работы с компьютерным зрением.\n",
        "Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана\n"
        "Благодаря ей он может регулировать громкость...\n",
        "first open test",
    ),
    (
        "121\n5\n"
        "Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана\n"
        "Благодаря ей он может регулировать громкость,\n"
        "показывая расстояние между большим и указательным пальцами.\n"
        "Для этого ему понадобилась веб-камера, знания Python и\n"
        "библиотека для работы с компьютерным зрением.\n",
        "Энтузиаст написал программу для управления громкостью с помощью жестов, чтоб не вставать с дивана\n"
        "Благодаря ей он может...\n",
        "second open test",
    ),
    (
        "71\n1\n"
        "Энтузиаст написал программу для управления громкостью с помощью жестов.\n",
        "Энтузиаст написал программу для управления громкостью с помощью жестов.\n",
        "exact length one line",
    ),
    (
        "71\n4\n"
        "Энтузиаст написал \n"
        "программу для управления \n"
        "громкостью \n"
        "с помощью жестов.\n",
        "Энтузиаст написал \n"
        "программу для управления \n"
        "громкостью \n"
        "с помощью жестов.\n",
        "exact length few lines",
    ),
    (
        "72\n1\n"
        "Энтузиаст написал программу для управления громкостью с помощью жестов.\n",
        "Энтузиаст написал программу для управления громкостью с помощью жестов.\n",
        "the title is lesser than the length one line",
    ),
    (
        "72\n4\n"
        "Энтузиаст написал \n"
        "программу для управления \n"
        "громкостью \n"
        "с помощью жестов.\n",
        "Энтузиаст написал \n"
        "программу для управления \n"
        "громкостью \n"
        "с помощью жестов.\n",
        "the title is lesser than the length few lines",
    ),
    (
        "70\n1\n"
        "Энтузиаст написал программу для управления громкостью с помощью жестов.\n",
        "Энтузиаст написал программу для управления громкостью с помощью жес...\n",
        "the title is larger than the length",
    ),
    ("10\n2\n12345\n123\n", "12345\n123\n", "Sergey Klochko's first test"),
    (
        "10\n7\n123\n\n\n\n\n\n1234567890\n",
        "123\n\n\n\n\n\n1234...\n",
        "Sergey Klochko's second test",
    ),
    ("4\n5\n1\n2\n3\n4\n5\n", "1...\n", "Sergey Klochko's third test"),
    ("3\n4\n1\n2\n3\n4\n", "...\n", "Nikolai's first test"),
    (
        "10\n2\n12345\n123456\n",
        "12345\n12...\n",
        "Valerii Glebov's first test",
    ),
    (
        "10\n2\n12345\n12345\n",
        "12345\n12345\n",
        "Valerii Glebov's second test",
    ),
]

q_test_data = [
    ("А роза упала на лапу Азора\n", "YES\n", "first open test"),
    ("Мама мыла раму\n", "NO\n", "second open test"),
    ("Race Car\n", "YES\n", "race car"),
    ("Race CarS\n", "NO\n", "race cars"),
    ("\n", "YES\n", "no input"),
    ("race truck\n", "NO\n", "two words"),
    ("racEcar\n", "YES\n", "racEcar"),
    ("12 21\n", "YES\n", "two numbers"),
]

r_test_data = [
    (
        "010000100001111111110111110000000000000011111111\n",
        "0 1\n"
        "1 1\n"
        "0 4\n"
        "1 1\n"
        "0 4\n"
        "1 9\n"
        "0 1\n"
        "1 5\n"
        "0 14\n"
        "1 8\n",
        "first open test",
    ),
    (
        "0110000000100001000\n",
        "0 1\n1 2\n0 7\n1 1\n0 4\n1 1\n0 3\n",
        "second open test",
    ),
    (
        "0000000000000000000\n",
        "0 19\n",
        "only zeros",
    ),
    (
        "0\n",
        "0 1\n",
        "one zero",
    ),
    (
        "1\n",
        "1 1\n",
        "one one",
    ),
    (
        "11111111111111111111\n",
        "1 20\n",
        "only ones",
    ),
    (
        "10101010101010101010\n",
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n"
        "1 1\n"
        "0 1\n",
        "mix of ones and zeros",
    ),
]

s_test_data = [
    ("7 2 3 * -\n", "1\n", "subtraction after multiplication"),
    ("10 15 - 7 *\n", "-35\n", "multiplication after subtraction"),
    ("10 15 - 7 * -215 -\n", "180\n", "subtraction with negative result"),
    ("10 15 - 7 * -215 +\n", "-250\n", "addition with negative operand"),
    ("3 4 +\n", "7\n", "simple addition"),
    (
        "15 7 1 1 + - * 3 * 2 1 1 + + -\n",
        "221\n",
        "complex expression with multiple operators",
    ),
    ("5 1 2 + 4 * + 3 -\n", "14\n", "nested operations"),
    ("0 3 *\n", "0\n", "multiplication by zero"),
    ("2 5 - -2 -\n", "-1\n", "handling of negative results in subtraction"),
]

t_test_data = [
    ("7 1 10 100 # * @ - + + ~\n", "-10016\n", "first open test"),
    ("10 15 - 7 *\n", "-35\n", "second open test"),
    (
        "10 # +\n",
        "20\n",
        "duplication of the top stack value followed by addition",
    ),
    ("1 2 3 @ * /\n", "0\n", "rotating top three elements of the stack"),
    ("5 3 4 * +\n", "17\n", "simple addition after multiplication"),
    ("6 2 /\n", "3\n", "simple division case"),
    ("4 !\n", "24\n", "factorial operation simple case"),
    ("-5 ~\n", "5\n", "negation of a negative number"),
    ("0 1 2 @ + -\n", "-1\n", "rotation of stack top three elements"),
    (
        "10 2 3 * + 4 -\n",
        "12\n",
        "complex operation with addition and subtraction",
    ),
    (
        "5 -1 2 + 4 * + 3 -\n",
        "6\n",
        "operation with addition, multiplication, and subtraction",
    ),
    (
        "500000000 300000000 4000000000 * -20 @ * -\n",
        "1200000010000000000\n",
        "complex operation with rotation and multiplication",
    ),
    ("7 4 7 - /\n", "-3\n", "rounding problem"),
]
