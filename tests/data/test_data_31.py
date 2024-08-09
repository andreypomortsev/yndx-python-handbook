a_test_data = [
    ("3\nарбуз\nбарабан\nворона\n", "YES\n", "first open test"),
    ("4\nаист\nвареник\nкузнечик\nалыча\n", "NO\n", "second open test"),
    ("1\nаист\n", "YES\n", "one line а yes"),
    ("1\nбелка\n", "YES\n", "one line б yes"),
    ("1\nворон\n", "YES\n", "one line в yes"),
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
