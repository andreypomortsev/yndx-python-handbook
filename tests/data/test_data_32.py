a_test_data = [
    ("змееед\n", ("здме\n",), "first open test"),
    ("велосипед\n", ("исолвдеп\n",), "second open test"),
    ("ффффффффффффф\n", ("ф\n",), "one letter"),
    ("111111111111\n", ("1\n",), "one digit"),
    ("1122334455 66 77 88 999\n", ("123456789 \n",), "multiple digits"),
    ("..//,,!!\n", ("./,!\n",), "punctuation"),
    (
        "12132 !! .s,dddf dwefllsjcb _ +=123\n",
        ("j+dfl3sc_w be,!21.=\n",),
        "all at once",
    ),
]

b_test_data = [
    ("змееед\nвелосипед\n", ("ед\n",), "first open test"),
    ("мама\nпапа\n", ("а\n",), "second open test"),
    ("21 \n34 ", (" \n",), "whitespace"),
    ("12345\n12345\n", ("12345\n",), "equal digits positive"),
    ("12345\n6789\n", ("\n",), "different digits negative"),
    ("!@#$%^&*()\n!@#$%^&*()\n", ("!@#$%^&*()\n",), "equal special chars"),
    (
        "!@#$2%4^s&*()\n!h@k#8$6%^&*()\n",
        ("!@#$%^&*()\n",),
        "noisy special chars",
    ),
]

c_test_data = [
    (
        "3\n"
        "березка елочка зайка волк березка\n"
        "сосна зайка сосна елочка зайка медведь\n"
        "сосна сосна сосна белочка сосна белочка\n",
        [
            "сосна\n"
            "березка\n"
            "волк\n"
            "елочка\n"
            "медведь\n"
            "белочка\n"
            "зайка\n",
        ],
        "first open test",
    ),
    (
        "4\nзайка березка\n"
        "березка зайка\n"
        "березка елочка березка\n"
        "елочка елочка елочка\n",
        ["березка\nелочка\nзайка\n"],
        "second open test",
    ),
]
d_test_data = [
    (
        "3\n2\nВасильев\nПетров\nВасечкин\nИванов\nМихайлов\n",
        "Таких нет\n",
        "first open test",
    ),
    (
        "3\n3\nИванов\n"
        "Петров\n"
        "Васечкин\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n",
        "3\n",
        "second open test",
    ),
]

e_test_data = [
    (
        "3\n2\nВасильев\nПетров\nВасечкин\nИванов\nМихайлов\n",
        "5\n",
        "first open test",
    ),
    (
        "3\n3\nИванов\n"
        "Петров\n"
        "Васечкин\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n",
        "Таких нет\n",
        "second open test",
    ),
    (
        "0\n6\nИванов\n"
        "Петров\n"
        "Васечкин\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n",
        "6\n",
        "second porridge lovers",
    ),
    (
        "5\n0\nИванов\nПетров\nВасечкин\nИванов\nПетров\n",
        "5\n",
        "first porridge lovers",
    ),
]

f_test_data = [
    (
        "3\n2\nВасильев\nПетров\nВасечкин\nИванов\nМихайлов\n",
        "Васечкин\nВасильев\nИванов\nМихайлов\nПетров\n",
        "first open test",
    ),
    (
        "3\n3\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n",
        "Таких нет\n",
        "second open test",
    ),
]

g_test_data = [
    (
        "Hello world\n",
        ".... . .-.. .-.. ---\n.-- --- .-. .-.. -..\n",
        "first open test",
    ),
    (
        "Help me SOS\n",
        ".... . .-.. .--.\n-- .\n... --- ...\n",
        "second open test",
    ),
    (
        "Python3 is easy to learn\n",
        ".--. -.-- - .... --- -. ...--\n"
        ".. ...\n"
        ". .- ... -.--\n"
        "- ---\n"
        ".-.. . .- .-. -.\n",
        "words with a digit",
    ),
    (
        "9876543210\n",
        "----. ---.. --... -.... ..... ....- ...-- ..--- .---- -----\n",
        "digits one line",
    ),
    (
        "9 8 7 6 5 4 3 2 1 0\n",
        "----.\n"
        "---..\n"
        "--...\n"
        "-....\n"
        ".....\n"
        "....-\n"
        "...--\n"
        "..---\n"
        ".----\n"
        "-----\n",
        "digits with spaces line",
    ),
]

h_test_data = [
    (
        "5\n"
        "Васильев манная\n"
        "Петров манная\n"
        "Васечкин манная\n"
        "Иванов овсяная\n"
        "Михайлов овсяная\n"
        "манная\n",
        "Васечкин\nВасильев\nПетров\n",
        "first open test",
    ),
    (
        "3\n"
        "Иванов манная овсяная\n"
        "Петров манная овсяная\n"
        "Васечкин манная овсяная\n"
        "гречневая\n",
        "Таких нет\n",
        "second open test",
    ),
    (
        "1\n" "Васильев манная\nманная\n",
        "Васильев\n",
        "one line positive",
    ),
    (
        "1\n" "Васильев манная\nгречневая\n",
        "Таких нет\n",
        "one line negative",
    ),
]

i_test_data = [
    (
        "березка елочка зайка волк березка\n"
        "сосна зайка сосна елочка зайка медведь\n"
        "сосна сосна сосна белочка сосна белочка\n"
        "\n",
        [
            "березка 2\n"
            "елочка 2\n"
            "зайка 3\n"
            "волк 1\n"
            "сосна 6\n"
            "медведь 1\n"
            "белочка 2\n"
        ],
        "first open test",
    ),
    (
        "зайка березка\n"
        "березка зайка\n"
        "березка елочка березка\n"
        "елочка елочка елочка\n"
        "\n",
        ["зайка 2\nберезка 4\nелочка 4\n"],
        "second open test",
    ),
]

j_test_data = [
    ("Привет, мир!\n", "Privet, mir!\n", "first open test"),
    (
        "Я помню чудное мгновенье: Передо мной явилась ты, "
        "Как мимолетное виденье, Как гений чистой красоты.\n",
        "Ia pomniu chudnoe mgnovene: Peredo mnoi iavilas ty, "
        "Kak mimoletnoe videne, Kak genii chistoi krasoty.\n",
        "second open test",
    ),
    (
        "Я помню чудное мгновенье: Передо мной явилась ты, "
        "Как мимолетное виденье, Как гений чистой красоты.\n",
        "Ia pomniu chudnoe mgnovene: Peredo mnoi iavilas ty, "
        "Kak mimoletnoe videne, Kak genii chistoi krasoty.\n",
        "second open test",
    ),
    (
        "Щука — одна из самых распространенных и хорошо всем известных речных рыб. "
        "Щучье мясо плотное, у него легко узнаваемый вкус и аромат, немного отдающий тиной. "
        "Многие за это щуку не жалуют.\n",
        "Shchuka — odna iz samykh rasprostranennykh i khorosho vsem izvestnykh rechnykh ryb. "
        "Shchuche miaso plotnoe, u nego legko uznavaemyi vkus i aromat, nemnogo otdaiushchii tinoi. "
        "Mnogie za eto shchuku ne zhaluiut.\n",
        "Shc",
    ),
]
