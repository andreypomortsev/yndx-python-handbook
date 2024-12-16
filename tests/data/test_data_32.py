a_test_data = [
    ("змееед\n", ("здме",), "first open test"),
    ("велосипед\n", ("исолвдеп",), "second open test"),
    ("ффффффффффффф\n", ("ф",), "one letter"),
    ("111111111111\n", ("1",), "one digit"),
    ("1122334455_6677_88_999\n", ("123456789_",), "multiple digits"),
    ("..//,,!!\n", ("./,!",), "punctuation"),
    (
        "12132 !! .s,dddf dwefllsjcb _ +=123\n",
        ("j+dfl3sc_w be,!21.=",),
        "all at once",
    ),
]

b_test_data = [
    ("змееед\nвелосипед\n", ("ед",), "first open test"),
    ("мама\nпапа\n", ("а",), "second open test"),
    ("21 \n34 ", ("",), "whitespace"),
    ("12345\n12345\n", ("12345",), "equal digits positive"),
    ("12345\n6789\n", ("",), "different digits negative"),
    ("!@#$%^&*()\n!@#$%^&*()\n", ("!@#$%^&*()",), "equal special chars"),
    (
        "!@#$2%4^s&*()\n!h@k#8$6%^&*()\n",
        ("!@#$%^&*()",),
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
            "зайка",
        ],
        "first open test",
    ),
    (
        "4\nзайка березка\n"
        "березка зайка\n"
        "березка елочка березка\n"
        "елочка елочка елочка\n",
        ["березка\nелочка\nзайка"],
        "second open test",
    ),
    (
        "1\nзайка березка "
        "березка зайка "
        "березка елочка березка "
        "елочка елочка елочка ",
        ["березка\nелочка\nзайка"],
        "one line",
    ),
]
d_test_data = [
    (
        "3\n2\nВасильев\nПетров\nВасечкин\nИванов\nМихайлов\n",
        "Таких нет",
        "first open test",
    ),
    (
        "3\n3\nИванов\n"
        "Петров\n"
        "Васечкин\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n",
        "3",
        "second open test",
    ),
    (
        "1\n5\nИванов\n"
        "Петрова\n"
        "Васечкина\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n",
        "1",
        "one from first group",
    ),
    (
        "5\n1\nИванова\n"
        "Петрова\n"
        "Васечкин\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n",
        "1",
        "one from second group",
    ),
]

e_test_data = [
    (
        "3\n2\nВасильев\nПетров\nВасечкин\nИванов\nМихайлов\n",
        "5",
        "first open test",
    ),
    (
        "3\n3\nИванов\n"
        "Петров\n"
        "Васечкин\n"
        "Иванов\n"
        "Петров\n"
        "Васечкин\n",
        "Таких нет",
        "second open test",
    ),
    (
        "0\n6\nИванов\n"
        "Петров\n"
        "Васечкин\n"
        "Иванова\n"
        "Петрова\n"
        "Васечкина\n",
        "6",
        "second porridge lovers",
    ),
    (
        "5\n0\nИванова\nПетрова\nВасечкин\nИванов\nПетров\n",
        "5",
        "first porridge lovers",
    ),
    (
        "3\n3\nИванов\n"
        "Иванов\n"
        "Петров\n"
        "Петров\n"
        "Васечкин\n"
        "Васечкин\n",
        "Таких нет",
        "second open test mixed",
    ),
]

f_test_data = [
    (
        "3\n2\nВасильев\nПетров\nВасечкин\nИванов\nМихайлов\n",
        "Васечкин\nВасильев\nИванов\nМихайлов\nПетров",
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
        "Таких нет",
        "second open test",
    ),
    (
        "5\n0\nИванова\nПетрова\nВасечкин\nИванов\nПетров\n",
        "Васечкин\nИванов\nИванова\nПетров\nПетрова",
        "first porridge lovers",
    ),
    (
        "0\n6\nИванов\n"
        "Петров\n"
        "Васечкин\n"
        "Иванова\n"
        "Петрова\n"
        "Васечкина\n",
        "Васечкин\nВасечкина\nИванов\nИванова\nПетров\nПетрова",
        "second porridge lovers",
    ),
]

g_test_data = [
    (
        "Hello world\n",
        ".... . .-.. .-.. ---\n.-- --- .-. .-.. -..",
        "first open test",
    ),
    (
        "Help me SOS\n",
        ".... . .-.. .--.\n-- .\n... --- ...",
        "second open test",
    ),
    (
        "Python3 is easy to learn\n",
        ".--. -.-- - .... --- -. ...--\n"
        ".. ...\n"
        ". .- ... -.--\n"
        "- ---\n"
        ".-.. . .- .-. -.",
        "words with a digit",
    ),
    (
        "9876543210\n",
        "----. ---.. --... -.... ..... ....- ...-- ..--- .---- -----",
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
        "-----",
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
        "Васечкин\nВасильев\nПетров",
        "first open test",
    ),
    (
        "3\n"
        "Иванов манная овсяная\n"
        "Петров манная овсяная\n"
        "Васечкин манная овсяная\n"
        "гречневая\n",
        "Таких нет",
        "second open test",
    ),
    (
        "3\n"
        "Иванов манная овсяная\n"
        "Петров манная гречневая\n"
        "Васечкин манная овсяная\n"
        "гречневая\n",
        "Петров",
        "one lover",
    ),
    (
        "1\n" "Васильев манная\nманная\n",
        "Васильев",
        "one line positive",
    ),
    (
        "1\n" "Васильев манная\nгречневая\n",
        "Таких нет",
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
            "белочка 2"
        ],
        "first open test",
    ),
    (
        "зайка березка\n"
        "березка зайка\n"
        "березка елочка березка\n"
        "елочка елочка елочка\n"
        "\n",
        ["зайка 2\nберезка 4\nелочка 4"],
        "second open test",
    ),
]

j_test_data = [
    ("Привет, мир!\n", "Privet, mir!", "first open test"),
    (
        "Я помню чудное мгновенье: Передо мной явилась ты, "
        "Как мимолетное виденье, Как гений чистой красоты.\n",
        "Ia pomniu chudnoe mgnovene: Peredo mnoi iavilas ty, "
        "Kak mimoletnoe videne, Kak genii chistoi krasoty.",
        "second open test",
    ),
    (
        "Щука — одна из самых распространенных и хорошо всем известных речных рыб. "
        "Щучье мясо плотное, у него легко узнаваемый вкус и аромат, немного отдающий тиной. "
        "Многие за это щуку не жалуют.\n",
        "Shchuka — odna iz samykh rasprostranennykh i khorosho vsem izvestnykh rechnykh ryb. "
        "Shchuche miaso plotnoe, u nego legko uznavaemyi vkus i aromat, nemnogo otdaiushchii tinoi. "
        "Mnogie za eto shchuku ne zhaluiut.",
        "Shc",
    ),
]

k_test_data = [
    (
        "6\n"
        "Иванов\n"
        "Петров\n"
        "Сидоров\n"
        "Петров\n"
        "Иванов\n"
        "Петров\n",
        "5",
        "first open test",
    ),
    ("3\n" "Иванов\nПетров\nСидоров\n", "0", "second open test"),
    (
        "12\n"
        "Иванов\n"
        "Петров\n"
        "Сидоров\n"
        "Петров\n"
        "Иванов\n"
        "Петров\n"
        "Trump\n"
        "Trump\n"
        "Петров\n"
        "Петров\n"
        "Красиков\n"
        "Петров\n",
        "10",
        "do not change the list",
    ),
]

l_test_data = [
    (
        "6\n"
        "Иванов\n"
        "Петров\n"
        "Сидоров\n"
        "Петров\n"
        "Иванов\n"
        "Петров\n",
        "Иванов - 2\nПетров - 3",
        "first open test",
    ),
    (
        "3\nИванов\nПетров\nСидоров\n",
        "Однофамильцев нет",
        "second open test",
    ),
    (
        "1\nИванов Петров\n",
        "Однофамильцев нет",
        "double last name one line",
    ),
    (
        "2\nИванов Петров\nИванов Петров\n",
        "Иванов Петров - 2",
        "double last name two lines",
    ),
    (
        "4\nИванов Петров\nИванов Петров\nИванов\nИванов\n",
        "Иванов - 2\nИванов Петров - 2",
        "double last name mix",
    ),
    (
        "4\nИванов Ивонин\nИванов Ивонин\nИвонин\nИвонин\n",
        "Иванов Ивонин - 2\nИвонин - 2",
        "double last name mix sorting check",
    ),
    (
        "4\nИванов Петров\nИванов Петров\nИванов\nПетров\n",
        "Иванов Петров - 2",
        "double last name mix 2",
    ),
]

m_test_data = [
    (
        "5\n"
        "Овсянка\n"
        "Рис\n"
        "Суп\n"
        "Манная каша\n"
        "Рыба\n"
        "2\n"
        "3\n"
        "Рис\n"
        "Суп\n"
        "Рыба\n"
        "2\n"
        "Рис\n"
        "Рыба\n",
        "Манная каша\nОвсянка",
        "first open test",
    ),
    (
        "2\nРис\nКартошка\n2\n1\nРис\n1\nКартошка",
        "Готовить нечего",
        "nothing to cook",
    ),
]

n_test_data = [
    (
        "4\n"
        "Яблоки\n"
        "Хлеб\n"
        "Варенье\n"
        "Картошка\n"
        "3\n"
        "Тосты\n"
        "2\n"
        "Хлеб\n"
        "Варенье\n"
        "Яблочный Сок\n"
        "1\n"
        "Яблоки\n"
        "Яичница\n"
        "1\n"
        "Яйца\n",
        "Тосты\nЯблочный Сок",
        "first open test",
    ),
    (
        "1\nхлеб\n1\nбутерброд\n2\nмасло\nхлеб\n",
        "Готовить нечего",
        "second open test",
    ),
]

o_test_data = [
    (
        "5 8 12\n",
        str(
            [
                {"digits": 3, "units": 2, "zeros": 1},
                {"digits": 4, "units": 1, "zeros": 3},
                {"digits": 4, "units": 2, "zeros": 2},
            ]
        ),
        "first open test",
    ),
    (
        "13 2 7\n",
        str(
            [
                {"digits": 4, "units": 3, "zeros": 1},
                {"digits": 2, "units": 1, "zeros": 1},
                {"digits": 3, "units": 3, "zeros": 0},
            ]
        ),
        "second open test",
    ),
    ("0\n", str([{"digits": 1, "units": 0, "zeros": 1}]), "zero test"),
    (
        "123456 78 90\n",
        str(
            [
                {"digits": 17, "units": 6, "zeros": 11},
                {"digits": 7, "units": 4, "zeros": 3},
                {"digits": 7, "units": 4, "zeros": 3},
            ]
        ),
        "digits",
    ),
    (
        "100200230 3120310123120 312321321123 221412388341738 34242349258348392 "
        "221412388341738221412388341738 22141342423492583483922388341738\n",
        str(
            [
                {"digits": 27, "units": 17, "zeros": 10},
                {"digits": 42, "units": 22, "zeros": 20},
                {"digits": 39, "units": 19, "zeros": 20},
                {"digits": 48, "units": 26, "zeros": 22},
                {"digits": 55, "units": 31, "zeros": 24},
                {"digits": 98, "units": 48, "zeros": 50},
                {"digits": 105, "units": 53, "zeros": 52},
            ]
        ),
        "huge nums",
    ),
]

p_test_data = [
    (
        "березка елочка зайка волк березка\n"
        "сосна зайка сосна елочка зайка медведь\n"
        "сосна сосна сосна белочка сосна белочка\n"
        "\n",
        ["волк\nелочка\nмедведь\nсосна"],
        "first open test",
    ),
    (
        "зайка березка\n"
        "березка зайка\n"
        "березка елочка березка\n"
        "елочка елочка елочка\n"
        "\n",
        "березка",
        "second open test",
    ),
    (
        "зайка березка\n"
        "березка зайка\n"
        "березка елочка березка\n"
        "зайка зайка зайка\n"
        "\n",
        ["березка\nзайка"],
        "three bunnies in a line",
    ),
    (
        "зайка березка\n"
        "березка зайка\n"
        "зайка обрыв река зайка мангуст Морти зайка\n"
        "\n",
        ["березка\nобрыв\nрека\nмангуст\nМорти"],
        "all in one place",
    ),
]

q_test_data = [
    (
        "Иванов Петров\n"
        "Иванов Сергеев\n"
        "Васильев Петров\n"
        "Сергеев Яковлев\n"
        "Петров Кириллов\n"
        "Петров Яковлев\n"
        "\n",
        "Васильев: Иванов, Кириллов, Яковлев\n"
        "Иванов: Васильев, Кириллов, Яковлев\n"
        "Кириллов: Васильев, Иванов, Яковлев\n"
        "Петров: Сергеев\n"
        "Сергеев: Петров\n"
        "Яковлев: Васильев, Иванов, Кириллов",
        "first open test",
    ),
    (
        "Николай Фёдор\n"
        "Николай Женя\n"
        "Фёдор Женя\n"
        "Фёдор Илья\n"
        "Илья Фёдор\n"
        "\n",
        "Женя: Илья\nИлья: Женя, Николай\nНиколай: Илья\nФёдор:",
        "second open test",
    ),
]

r_test_data = [
    (
        "9\n"
        "10 18\n"
        "17 15\n"
        "25 21\n"
        "0 21\n"
        "1 16\n"
        "25 29\n"
        "24 24\n"
        "8 26\n"
        "10 20\n",
        "3",
        "first open test",
    ),
    ("3\n12 113\n114 15\n16 117\n", "2", "second open test"),
    (
        "200\n"
        "133469997 299443892\n"
        "8106615 92220857\n"
        "879077582 791707817\n"
        "32289992 121114986\n"
        "331297123 186104757\n"
        "947868745 338744547\n"
        "249272880 348702667\n"
        "959340635 167095659\n"
        "290583194 312579811\n"
        "599102619 169442633\n"
        "309242131 799618226\n"
        "44440549 824124532\n"
        "105226830 679523710\n"
        "216688500 112581760\n"
        "470383119 517169761\n"
        "450919992 767533153\n"
        "805075635 623157648\n"
        "975253130 791902504\n"
        "109189082 211392991\n"
        "381813995 383303155\n"
        "79982482 666465061\n"
        "541431400 983835947\n"
        "272995500 229011606\n"
        "857249986 580226027\n"
        "535202298 370821856\n"
        "398970673 146590349\n"
        "440542580 99493406\n"
        "839953951 352597408\n"
        "949057798 757738337\n"
        "978804340 216130467\n"
        "639662553 660824683\n"
        "481432418 4326143\n"
        "982349778 138675373\n"
        "534937952 597879036\n"
        "897058374 947794641\n"
        "963170280 679194422\n"
        "64119520 635769983\n"
        "519106289 562075292\n"
        "965443288 372114227\n"
        "937133463 936977677\n"
        "837377654 848544239\n"
        "199985762 287877822\n"
        "972432744 333551459\n"
        "162287034 363519061\n"
        "130883786 112641185\n"
        "604875124 925395331\n"
        "923248777 67450213\n"
        "612578896 432265439\n"
        "54081868 652583690\n"
        "462353060 15298271\n"
        "439476384 334862528\n"
        "927403667 920719025\n"
        "192169745 399010215\n"
        "67579573 281966055\n"
        "23828692 366973901\n"
        "996821648 342897087\n"
        "91654393 610143361\n"
        "969595884 144762852\n"
        "534982185 89797998\n"
        "58519905 417933989\n"
        "227169670 57798573\n"
        "153396935 306211730\n"
        "383609066 979773664\n"
        "628479316 138123453\n"
        "227461761 195662501\n"
        "891538842 114695134\n"
        "176070604 180879846\n"
        "124001187 299766004\n"
        "889577528 189502725\n"
        "366059056 755302643\n"
        "695560305 323736283\n"
        "287510482 292700563\n"
        "677700301 467699065\n"
        "473852917 614711601\n"
        "134059899 978571995\n"
        "763073254 892306409\n"
        "819694011 120683322\n"
        "523886186 239360521\n"
        "554824656 158405869\n"
        "288058043 672701861\n"
        "949555471 736187039\n"
        "591614384 244220449\n"
        "30556349 380496536\n"
        "10045919 4139485\n"
        "208373927 784879548\n"
        "546461603 763680120\n"
        "221548726 80420740\n"
        "236838526 463063674\n"
        "609210701 967003140\n"
        "786444423 419933358\n"
        "254903693 454867612\n"
        "163371954 231718403\n"
        "219189484 948649566\n"
        "640000064 998117724\n"
        "681155048 766171797\n"
        "128793008 306819954\n"
        "764339396 127768540\n"
        "127994930 956999560\n"
        "460127762 880713850\n"
        "137074473 951150645\n"
        "133469997 299443892\n"
        "8106615 92220857\n"
        "879077582 791707817\n"
        "32289992 121114986\n"
        "331297123 186104757\n"
        "947868745 338744547\n"
        "249272880 348702667\n"
        "959340635 167095659\n"
        "290583194 312579811\n"
        "599102619 169442633\n"
        "309242131 799618226\n"
        "44440549 824124532\n"
        "105226830 679523710\n"
        "216688500 112581760\n"
        "470383119 517169761\n"
        "450919992 767533153\n"
        "805075635 623157648\n"
        "975253130 791902504\n"
        "109189082 211392991\n"
        "381813995 383303155\n"
        "79982482 666465061\n"
        "541431400 983835947\n"
        "272995500 229011606\n"
        "857249986 580226027\n"
        "535202298 370821856\n"
        "398970673 146590349\n"
        "440542580 99493406\n"
        "839953951 352597408\n"
        "949057798 757738337\n"
        "978804340 216130467\n"
        "639662553 660824683\n"
        "481432418 4326143\n"
        "982349778 138675373\n"
        "534937952 597879036\n"
        "897058374 947794641\n"
        "963170280 679194422\n"
        "64119520 635769983\n"
        "519106289 562075292\n"
        "965443288 372114227\n"
        "937133463 936977677\n"
        "837377654 848544239\n"
        "199985762 287877822\n"
        "972432744 333551459\n"
        "162287034 363519061\n"
        "130883786 112641185\n"
        "604875124 925395331\n"
        "923248777 67450213\n"
        "612578896 432265439\n"
        "54081868 652583690\n"
        "462353060 15298271\n"
        "439476384 334862528\n"
        "927403667 920719025\n"
        "192169745 399010215\n"
        "67579573 281966055\n"
        "23828692 366973901\n"
        "996821648 342897087\n"
        "91654393 610143361\n"
        "969595884 144762852\n"
        "534982185 89797998\n"
        "58519905 417933989\n"
        "227169670 57798573\n"
        "153396935 306211730\n"
        "383609066 979773664\n"
        "628479316 138123453\n"
        "227461761 195662501\n"
        "891538842 114695134\n"
        "176070604 180879846\n"
        "124001187 299766004\n"
        "889577528 189502725\n"
        "366059056 755302643\n"
        "695560305 323736283\n"
        "287510482 292700563\n"
        "677700301 467699065\n"
        "473852917 614711601\n"
        "134059899 978571995\n"
        "763073254 892306409\n"
        "819694011 120683322\n"
        "523886186 239360521\n"
        "554824656 158405869\n"
        "288058043 672701861\n"
        "949555471 736187039\n"
        "591614384 244220449\n"
        "30556349 380496536\n"
        "10045919 4139485\n"
        "208373927 784879548\n"
        "546461603 763680120\n"
        "221548726 80420740\n"
        "236838526 463063674\n"
        "609210701 967003140\n"
        "786444423 419933358\n"
        "254903693 454867612\n"
        "163371954 231718403\n"
        "219189484 948649566\n"
        "640000064 998117724\n"
        "681155048 766171797\n"
        "128793008 306819954\n"
        "764339396 127768540\n"
        "127994930 956999560\n"
        "460127762 880713850\n"
        "137074473 951150645\n",
        "2",
        "big nums with repeated values, like in Yandex tests",
    ),
]

s_test_data = [
    (
        "3\n"
        "Аня: кукла, машинка, кукла, домик\n"
        "Боря: машинка, зайчик\n"
        "Вова: кубики, машинка\n",
        ["домик\nзайчик\nкубики\nкукла"],
        "first open test",
    ),
    (
        "3\n" "Аня: кукла\n" "Боря: машинка\n" "Вова: кубики\n",
        ["кубики\nкукла\nмашинка"],
        "poor kids",
    ),
]

t_test_data = [
    (
        "2; 3; 4; 5; 6; 7; 8; 9; 10; 11; 12; 13; 14; 15; 16; 17; 18; 19; 20\n",
        "2 - 3, 5, 7, 9, 11, 13, 15, 17, 19\n"
        "3 - 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20\n"
        "4 - 3, 5, 7, 9, 11, 13, 15, 17, 19\n"
        "5 - 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19\n"
        "6 - 5, 7, 11, 13, 17, 19\n"
        "7 - 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20\n"
        "8 - 3, 5, 7, 9, 11, 13, 15, 17, 19\n"
        "9 - 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20\n"
        "10 - 3, 7, 9, 11, 13, 17, 19\n"
        "11 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20\n"
        "12 - 5, 7, 11, 13, 17, 19\n"
        "13 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20\n"
        "14 - 3, 5, 9, 11, 13, 15, 17, 19\n"
        "15 - 2, 4, 7, 8, 11, 13, 14, 16, 17, 19\n"
        "16 - 3, 5, 7, 9, 11, 13, 15, 17, 19\n"
        "17 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20\n"
        "18 - 5, 7, 11, 13, 17, 19\n"
        "19 - 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20\n"
        "20 - 3, 7, 9, 11, 13, 17, 19",
        "first open test",
    ),
    (
        "7; 2; 2; 12; 14; 7; 2; 49\n",
        "2 - 7, 49\n" "7 - 2, 12\n" "12 - 7, 49\n" "49 - 2, 12",
        "second open test",
    ),
    (
        "17; 23; 19; 29; 31; 37; 41\n",
        "17 - 19, 23, 29, 31, 37, 41\n"
        "19 - 17, 23, 29, 31, 37, 41\n"
        "23 - 17, 19, 29, 31, 37, 41\n"
        "29 - 17, 19, 23, 31, 37, 41\n"
        "31 - 17, 19, 23, 29, 37, 41\n"
        "37 - 17, 19, 23, 29, 31, 41\n"
        "41 - 17, 19, 23, 29, 31, 37",
        "prime numbers",
    ),
    (
        "8; 9; 25; 27; 49\n",
        "8 - 9, 25, 27, 49\n"
        "9 - 8, 25, 49\n"
        "25 - 8, 9, 27, 49\n"
        "27 - 8, 25, 49\n"
        "49 - 8, 9, 25, 27",
        "non-prime numbers",
    ),
    (
        "1; 2; 1; 4; 8; 16; 32\n",
        "",
        "powers of 2",
    ),
]
