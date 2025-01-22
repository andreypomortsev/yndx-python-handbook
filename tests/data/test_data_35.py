a_test_data = [
    ("1 2\n3 4 5\n6\n7 8 9 10\n", "55\n", "first open test"),
    ("-21\n-12\n-9\n", "-42\n", "all nagative few lines"),
    ("-21 -12 -9\n", "-42\n", "all nagative one line"),
    ("0\n0 0 0 0 0\n0 0\n", "0\n", "all zeros few lines"),
    ("0 0 0 0 0 0 0 0\n", "0\n", "all zeros one line"),
    ("-10\n1 2 3 3 0\n0 1\n", "0\n", "zero sum few lines"),
    ("-10 1 2 3 3 0 0 1\n", "0\n", "zero sum one line"),
    (
        "100000\n1000000 2004234 342312323 33123443234 34255645670\n313657870 429934584672731\n",
        "430002622836062\n",
        "big sum few lines",
    ),
    (
        "100000 1000000 2004234 342312323 33123443234 34255645670 313657870 429934584672731\n",
        "430002622836062\n",
        "big sum one line",
    ),
    ("-10\n\n\n\n10\n", "0\n", "zero sum empty lines"),
]

b_test_data = [
    ("Аня 160 162\nБоря 165 172\nВова 165 165\n", "3\n", "first open test"),
    (
        "Аня 161 165\nБоря 167 172\nВова 165 166\nДима 173 178\n",
        "4\n",
        "second open test",
    ),
    ("Аня 164 162\nБоря 165 163\nВова 165 165\n", "-1\n", "negative growth"),
    (
        "Аня 165 165\nБоря 172 172\nВова 166 166\nДима 178 178\n",
        "0\n",
        "zero growth",
    ),
    (
        "Аня 160.6 162.7\nБоря 159.9 163.1\nВова 165.1 165.9\n",
        "2\n",
        "float growth",
    ),
    (
        "Аня 160 162\nБоря 159 163\nВова 165 165\nLePricon 165 159",
        "0\n",
        "negative outlier",
    ),
    (
        "Аня 166 162\nБоря 156 153\nВова 165 163\nJamal 150 159",
        "0\n",
        "positive outlier",
    ),
]

# c_test_data такая же как и для 3.1 I

# d_test_data такая же как и для 3.1 K

e_test_data = [
    (
        "Анна Боря Вова\n"
        "Я последняя буква алфавита\n"
        "Дед строит шалаш\n"
        "Шалаш был хорош\n"
        "Дед слышит топот\n"
        "Ара залетел в шалаш\n",
        "Анна\nАра\nДед\nШалаш\nЯ\nв\nтопот\nшалаш\n",
        "first open test",
    ),
    (
        "Казак был рад\n"
        "Боб увидел Анну\n"
        "Семья любит Деда\n"
        "Ара летает\n"
        "Я иду к нему\n",
        "Ара\nБоб\nКазак\nЯ\nк\n",
        "palindrome and single letter test",
    ),
    (
        "Кот ходит по дому\nСобака лает\nПтица, а поет на дереве\n",
        "а\n",
        "single letter test",
    ),
    (
        "Радар Малам Карек\nКак дошел до топора\nЯ и он в арке\n",
        "Как\nМалам\nРадар\nЯ\nв\nи\n",
        "palindromes mixed length test",
    ),
    (
        "Дом Кот Лиса Окно\nБеседа на природе\nЧеловек идет по улице\n",
        "",
        "no palindrome, no single letter test",
    ),
]

# f_test_data такая же как и для 3.2 J

g_test_data = [
    (
        "numbers.txt",
        "1 2 3 4 5\n-5 -4 -3 -2 -1\n10 20\n20 10\n",
        "14\n9\n-5\n20\n60\n4.29\n",
        "first open test",
    ),
    (
        "digits",
        "1 2 3 4 5\n-5 -4 -3 -2 -1\n10 20\n20 10\n",
        "14\n9\n-5\n20\n60\n4.29\n",
        "file w/o extension",
    ),
    (
        "some file.txt",
        "1 2 3 4 5\n-5 -4 -3 -2 -1\n10 20\n20 10\n",
        "14\n9\n-5\n20\n60\n4.29\n",
        "two words file name",
    ),
    (
        "some file.txt",
        "0\n0\n0\n0\n0\n0\n0\n0\n",
        {"8\n0\n0\n0\n0\n0.0\n", "8\n0\n0\n0\n0\n0.00\n"},
        "zeros in several lines",
    ),
    (
        "some file.txt",
        "1000000 200000003 310020030000203 120310120310040130 212031031020031020\n",
        {
            "5\n5\n"
            "1000000\n"
            "212031031020031020\n"
            "332651171561071356\n"
            "6.653023431221427e+16\n",
            "5\n5\n"
            "1000000\n"
            "212031031020031020\n"
            "332651171561071356\n"
            "66530234312214272.00\n",
        },
        "big nums in a line",
    ),
    (
        "different_file.txt",
        "1000000\n200000003\n310020030000203\n120310120310040130\n212031031020031020\n",
        {
            "5\n5\n"
            "1000000\n"
            "212031031020031020\n"
            "332651171561071356\n"
            "6.653023431221427e+16\n",
            "5\n5\n"
            "1000000\n"
            "212031031020031020\n"
            "332651171561071356\n"
            "66530234312214272.00\n",
        },
        "big nums in a few lines",
    ),
    (
        "rational.txt",
        "1 2 3\n4 5 6 7\n8 9 10 11 12\n13 14 15 16 17\n\n\n1000\n",
        "18\n18\n1\n1000\n1153\n64.06\n",
        "few empty lines",
    ),
]

h_test_data = [
    (
        ("first.txt", "second.txt", "answer.txt"),
        (
            "кофе молоко\nчай печенье\nвелосипед\n",
            "кофе велосипед\nпряник жвачка весло\n",
        ),
        {
            "весло\nжвачка\nмолоко\nпеченье\nпряник\nчай\n",
            "весло\nжвачка\nмолоко\nпеченье\nпряник\nчай",
        },
        "first open test",
    ),
    (
        ("uno", "dos", "resultado"),
        (
            "кофе молоко\nчай печенье\nвелосипед\n",
            "кофе велосипед\nпряник жвачка весло\n",
        ),
        {
            "весло\nжвачка\nмолоко\nпеченье\nпряник\nчай\n",
            "весло\nжвачка\nмолоко\nпеченье\nпряник\nчай",
        },
        "first open tes file names w/o extensions",
    ),
    (
        ("1.log", "2.txt", "3.txt"),
        (
            "молоко\nчай печенье\nвелосипед\n",
            "кофе велосипед\nпряник жвачка весло\n",
        ),
        {
            "весло\nжвачка\nкофе\nмолоко\nпеченье\nпряник\nчай\n",
            "весло\nжвачка\nкофе\nмолоко\nпеченье\nпряник\nчай",
        },
        "all distinct",
    ),
    (
        ("1.log", "2.txt", "3.txt"),
        (
            "молоко\nчай печенье\nвелосипед\n",
            "\n",
        ),
        {
            "велосипед\nмолоко\nпеченье\nчай\n",
            "велосипед\nмолоко\nпеченье\nчай",
        },
        "one empty file",
    ),
    (
        ("1.log", "2.txt", "3.txt"),
        (
            "\n",
            "кофе велосипед\nпряник жвачка весло\n",
        ),
        {
            "велосипед\nвесло\nжвачка\nкофе\nпряник\n",
            "велосипед\nвесло\nжвачка\nкофе\nпряник",
        },
        "another empty file",
    ),
    (
        ("temp.log", "temp2.txt", "temp3.txt"),
        (
            "\n",
            "\n",
        ),
        {"\n", ""},
        "two empty files",
    ),
]

i_test_data = [
    (
        ("first.txt", "second.txt"),
        """\
очень 		 плохо форматированный       текст


ну		ну	
прямо

очень-очень

	""",
        {
            "очень плохо форматированный текст\nнуну\nпрямо\nочень-очень\n",
            "очень плохо форматированный текст\nнуну\nпрямо\nочень-очень",
        },
        "first open test",
    ),
    (
        ("2", "1"),
        """\
очень 		 плохо форматированный       текст


ну		ну	
прямо

очень-очень

	""",
        {
            "очень плохо форматированный текст\nнуну\nпрямо\nочень-очень\n",
            "очень плохо форматированный текст\nнуну\nпрямо\nочень-очень",
        },
        "first open test file name w/o extensions",
    ),
    (
        ("input.log", "output.txt"),
        """\
очень 		 плохо форматированный       текст


ну		ну	
прямо

очень	-очень

	к	о	н	е	ц	 !""",
        {
            "очень плохо форматированный текст\nнуну\nпрямо\nочень-очень\nконец !\n",
            "очень плохо форматированный текст\nнуну\nпрямо\nочень-очень\nконец !",
        },
        "tab separated word",
    ),
    (
        ("input.log", "output.txt"),
        """\
s 		            
t
a
r
t



	к	о	н	е	ц	 !""",
        {
            "s\nt\na\nr\nt\nконец !\n",
            "s\nt\na\nr\nt\nконец !",
        },
        "lines separated word",
    ),
]

j_test_data = [
    (
        "some_file.txt",
        "1 строка\n2 строка\n3 строка\n4 строка\n5 строка\n",
        "2",
        {
            "4 строка\n5 строка\n\n",
            "4 строка\n5 строка\n",
            "4 строка\n5 строка",
        },
        "first open test",
    ),
    (
        "temp",
        "1 строка\n2 строка\n3 строка\n4 строка\n5 строка\n",
        "5",
        {
            "1 строка\n2 строка\n3 строка\n4 строка\n5 строка\n\n",
            "1 строка\n2 строка\n3 строка\n4 строка\n5 строка\n",
            "1 строка\n2 строка\n3 строка\n4 строка\n5 строка",
        },
        "all file",
    ),
    (
        "empty.txt",
        "\n\n\n\n\n",
        "5",
        {
            "\n\n\n\n\n\n",
            "\n\n\n\n\n",
            "\n\n\n\n",
        },
        "all empty lines file",
    ),
    (
        "empty-last_line.txt",
        "1 строка\n2 строка\n3 строка\n\n4 строка\n5 строка\n\n",
        "4",
        {
            "\n4 строка\n5 строка\n\n\n",
            "\n4 строка\n5 строка\n\n",
            "\n4 строка\n5 строка\n",
        },
        "few empty plus text",
    ),
]

k_test_data = [
    (
        ("numbers.txt", "statistics.json"),
        "1 2 3 4 5\n-5 -4 -3 -2 -1\n10 20\n20 10\n",
        {
            "count": 14,
            "positive_count": 9,
            "min": -5,
            "max": 20,
            "sum": 60,
            "average": 4.29,
        },
        "first open test",
    ),
    (
        ("numbers.txt", "statistics.json"),
        "1 2 3 4 5 -5 -4 -3 -2 -1 10 20 20 10\n",
        {
            "count": 14,
            "positive_count": 9,
            "min": -5,
            "max": 20,
            "sum": 60,
            "average": 4.29,
        },
        "first open test one line",
    ),
    (
        ("numbers.txt", "statistics.json"),
        "1 2 3 4 5\n-5 -4 -3 -2 -1\n10 20\n-20 -10\n",
        {
            "count": 14,
            "positive_count": 7,
            "min": -20,
            "max": 20,
            "sum": 0,
            "average": 0.0,
        },
        "average 0",
    ),
    (
        ("1.txt", "2.json"),
        "1 2 3 4 5 -5 -4 -3 -2 -1 10 20 -20 -10\n",
        {
            "count": 14,
            "positive_count": 7,
            "min": -20,
            "max": 20,
            "sum": 0,
            "average": 0.0,
        },
        "one line average 0",
    ),
    (
        ("numbers.txt", "statistics.json"),
        "\n-5 -4 -3 -2 -1\n\n-20 -10\n",
        {
            "count": 7,
            "positive_count": 0,
            "min": -20,
            "max": -1,
            "sum": -45,
            "average": -6.43,
        },
        "only negative numbers",
    ),
    (
        ("only positive numbers.txt", "num-statistics.json"),
        "\n5 4 3 2 1\n\n20 10\n",
        {
            "count": 7,
            "positive_count": 7,
            "min": 1,
            "max": 20,
            "sum": 45,
            "average": 6.43,
        },
        "only positive numbers",
    ),
    (
        ("only positive numbers.txt", "num-statistics.json"),
        "0 0 0 0 0 0 0 0\n5 4 3 2 1\n\n20 10\n",
        {
            "count": 15,
            "positive_count": 7,
            "min": 0,
            "max": 20,
            "sum": 45,
            "average": 3.0,
        },
        "positive numbers and zeros",
    ),
    (
        ("zeros", "indeed.json"),
        "0 0 0 0 0 0 0 0\n-5 -4 -3 -2 -1\n\n-20 -10\n",
        {
            "count": 15,
            "positive_count": 0,
            "min": -20,
            "max": 0,
            "sum": -45,
            "average": -3.0,
        },
        "negative numbers and zeros",
    ),
    (
        ("one_negative_num", "indeed.json"),
        "-10\n",
        {
            "count": 1,
            "positive_count": 0,
            "min": -10,
            "max": -10,
            "sum": -10,
            "average": -10.0,
        },
        "one negative number",
    ),
    (
        ("one_positive_num.log", "indeed.json"),
        "330\n",
        {
            "count": 1,
            "positive_count": 1,
            "min": 330,
            "max": 330,
            "sum": 330,
            "average": 330.0,
        },
        "one positive number",
    ),
]

l_test_data = [
    (
        ("numbers.txt", "even.txt", "odd.txt", "eq.txt"),
        "650975472 591084323 629700 1504180 577023\n"
        "8460612246 42161437 29409368 58531725 5725268 2198001838\n"
        "796451 69358 7195510 975628465 9756641\n"
        "44200289 126541 979391 93479581 291170 28987042 86139603\n",
        (
            "629700 1504180\n"
            "8460612246 29409368 5725268 2198001838\n"
            "975628465\n"
            "44200289 28987042\n",
            "650975472 591084323 577023\n"
            "58531725\n"
            "796451 69358 7195510 9756641\n"
            "979391 93479581 291170\n",
            "\n42161437\n\n126541 86139603\n",
        ),
        "first open test",
    ),
    (
        ("1", "2", "3", "RESULT"),
        "1\n2\n3\n\n4\n",
        (
            "\n2\n\n\n4\n",
            "1\n\n3\n\n\n",
            "\n\n\n\n\n",
        ),
        "one empty line single nums",
    ),
    (
        ("input.txt", "even.txt", "odd.txt", "eq.txt"),
        "650975472 591084323 629700 1504180 577023\n"
        "8460612246 42161437 29409368 58531725 5725268 2198001838\n\n"
        "796451 69358 7195510 975628465 9756641\n"
        "44200289 126541 979391 93479581 291170 28987042 86139603\n",
        (
            "629700 1504180\n"
            "8460612246 29409368 5725268 2198001838\n\n"
            "975628465\n"
            "44200289 28987042\n",
            "650975472 591084323 577023\n"
            "58531725\n\n"
            "796451 69358 7195510 9756641\n"
            "979391 93479581 291170\n",
            "\n42161437\n\n\n126541 86139603\n",
        ),
        "one empty line big nums",
    ),
    (
        ("input", "even.txt", "odd.txt", "eq.txt"),
        "3223244435694 0 0 0 0\n"
        "111111 333333 3333333 333330000000\n"
        "100 2200144\n",
        (
            "3223244435694 0 0 0 0\n" "333330000000\n" "100 2200144\n",
            "\n" "111111 333333 3333333\n" "\n",
            "\n\n\n",
        ),
        "even or odd nums",
    ),
    (
        ("input", "even", "odd.txt", "eq.txt"),
        "21 21 21 21\n"
        "36 67 89 90\n"
        "12\n"
        "29\n"
        "90\n"
        "98\n"
        "21\n"
        "16\n"
        "9023\n",
        (
            "\n\n\n\n\n\n\n\n\n",
            "\n\n\n\n\n\n\n\n\n",
            "21 21 21 21\n"
            "36 67 89 90\n"
            "12\n"
            "29\n"
            "90\n"
            "98\n"
            "21\n"
            "16\n"
            "9023\n",
        ),
        "equal nums",
    ),
    (
        ("input", "even", "odd.txt", "eq.txt"),
        "2 62 26 24\n"
        "436 267 892 290\n"
        "212\n"
        "292\n"
        "904\n"
        "698\n"
        "216\n"
        "616\n"
        "90238\n",
        (
            "2 62 26 24\n"
            "436 267 892 290\n"
            "212\n"
            "292\n"
            "904\n"
            "698\n"
            "216\n"
            "616\n"
            "90238\n",
            "\n\n\n\n\n\n\n\n\n",
            "\n\n\n\n\n\n\n\n\n",
        ),
        "all even nums",
    ),
    (
        ("input", "even.log", "odd", "equal"),
        "231 13623 23136 31924\n"
        "43576 27967 97892 27909\n"
        "29253 7521279\n"
        "698335 29253\n"
        "90455 6165533\n"
        "698335 2925312111\n"
        "216535 7521279\n"
        "6165533 6165533\n"
        "902385353\n",
        (
            "\n\n\n\n\n\n\n\n\n",
            "231 13623 23136 31924\n"
            "43576 27967 97892 27909\n"
            "29253 7521279\n"
            "698335 29253\n"
            "90455 6165533\n"
            "698335 2925312111\n"
            "216535 7521279\n"
            "6165533 6165533\n"
            "902385353\n",
            "\n\n\n\n\n\n\n\n\n",
        ),
        "all odd nums",
    ),
]

m_test_data = [
    (
        "data.json",
        "one == один\ntwo == два\nthree == три\n",
        {"one": 1, "three": 2},
        {"one": "один", "three": "три", "two": "два"},
        "first open test",
    ),
    (
        "another_data.json",
        "21 == двадцать-один\n",
        {"21": 1, "three": 2},
        {"21": "двадцать-один", "three": 2},
        "one line",
    ),
    (
        "yet_another_data.json",
        "' ' == empty string\n",
        {"21": 21, "three": 2},
        {"' '": "empty string", "21": 21, "three": 2},
        "add a value",
    ),
    (
        "fancy_data.json",
        'language_info == {"name": "python", "user": None}\n'
        'metadata == {"kernelspec": {"name": "python3", "display_name": "Python 3"}}\n',
        {
            "type": "notebook",
            "metadata": {
                "kernelspec": {"name": "python3", "display_name": "Python 3"},
                "language_info": {"name": "python"},
            },
        },
        {
            "type": "notebook",
            "metadata": {
                "kernelspec": {"name": "python3", "display_name": "Python 3"}
            },
            "language_info": {"name": "python", "user": None},
        },
        "moving jsons",
    ),
    (
        "yet_another_data.json",
        "' ' == ['empty string']\n",
        {"21": 21, "three": 2},
        {"' '": ["empty string"], "21": 21, "three": 2},
        "add a list as a value",
    ),
]

n_test_data = [
    (
        ("users.json", "updates.json"),
        (
            [
                {"name": "Ann", "address": "Flower st."},
                {
                    "name": "Bob",
                    "address": "Summer st.",
                    "phone": "+7 (123) 456-78-90",
                },
            ],
            [
                {
                    "name": "Ann",
                    "address": "Awesome st.",
                    "phone": "+7 (098) 765-43-21",
                },
                {"name": "Bob", "address": "Winter st."},
            ],
        ),
        {
            "Ann": {
                "address": "Flower st.",
                "phone": "+7 (098) 765-43-21",
            },
            "Bob": {
                "address": "Winter st.",
                "phone": "+7 (123) 456-78-90",
            },
        },
        "first open test",
    ),
    (
        ("1.json", "2.json"),
        (
            [
                {"name": "Ann", "address": "Flower st."},
                {"name": "Vova", "address": "Bunker st."},
                {
                    "name": "Bob",
                    "address": "Summer st.",
                    "phone": "+7 (123) 456-78-90",
                },
            ],
            [
                {
                    "name": "Ann",
                    "address": "Awesome st.",
                    "phone": "+7 (098) 765-43-21",
                },
                {"name": "Bob", "address": "Winter st."},
                {
                    "name": "Vova",
                    "phone": "+ 31 (0)70 515 8515",
                    "address": "Oude Waalsdorperweg st.",
                },
            ],
        ),
        {
            "Ann": {
                "address": "Flower st.",
                "phone": "+7 (098) 765-43-21",
            },
            "Bob": {
                "address": "Winter st.",
                "phone": "+7 (123) 456-78-90",
            },
            "Vova": {
                "address": "Oude Waalsdorperweg st.",
                "phone": "+ 31 (0)70 515 8515",
            },
        },
        "more users",
    ),
]

o_test_data = [
    (
        "4\n12\n3\n100\n0\n",
        [
            {
                "points": 10,
                "tests": [
                    {"input": "2 2", "pattern": "4"},
                    {"input": "4 3", "pattern": "7"},
                ],
            },
            {
                "points": 30,
                "tests": [
                    {"input": "2 1", "pattern": "3"},
                    {"input": "25 4", "pattern": "29"},
                    {"input": "3 -3", "pattern": "0"},
                ],
            },
        ],
        "25\n",
        "first open test",
    ),
    (
        "12\n4\n7\n3\n29\n0\n987\n229\n100\n2210\n",
        [
            {
                "points": 60,
                "tests": [
                    {"input": "22 -2", "pattern": "12"},
                    {"input": "2 2", "pattern": "4"},
                    {"input": "4 3", "pattern": "7"},
                ],
            },
            {
                "points": 30,
                "tests": [
                    {"input": "2 1", "pattern": "3"},
                    {"input": "25 4", "pattern": "29"},
                    {"input": "3 -3", "pattern": "0"},
                ],
            },
            {
                "points": 4,
                "tests": [
                    {"input": "32 12", "pattern": "987"},
                    {"input": "235 -114", "pattern": "229"},
                    {"input": "30 -93", "pattern": "100"},
                    {"input": "1093 34343", "pattern": "2210"},
                ],
            },
        ],
        "94\n",
        "nailed it!",
    ),
    (
        "120\n40\n70\n30\n290\n90\n9807\n2029\n10\n210\n",
        [
            {
                "points": 60,
                "tests": [
                    {"input": "22 -2", "pattern": "12"},
                    {"input": "2 2", "pattern": "4"},
                    {"input": "4 3", "pattern": "7"},
                ],
            },
            {
                "points": 30,
                "tests": [
                    {"input": "2 1", "pattern": "3"},
                    {"input": "25 4", "pattern": "29"},
                    {"input": "3 -3", "pattern": "0"},
                ],
            },
            {
                "points": 4,
                "tests": [
                    {"input": "32 12", "pattern": "987"},
                    {"input": "235 -114", "pattern": "229"},
                    {"input": "30 -93", "pattern": "100"},
                    {"input": "1093 34343", "pattern": "2210"},
                ],
            },
        ],
        "0\n",
        "failed it!",
    ),
    (
        "4\n",
        [
            {
                "points": 100,
                "tests": [
                    {"input": "2 2", "pattern": "4"},
                ],
            }
        ],
        "100\n",
        "very important test passed",
    ),
    (
        "4\n",
        [
            {
                "points": 100,
                "tests": [
                    {"input": "2 2", "pattern": "24"},
                ],
            }
        ],
        "0\n",
        "very important test failed",
    ),
]

p_test_data = [
    (
        "Мама мыла РАМУ\nfirst.txt\nsecond.txt\n",
        (
            "В этом файле говорится    о том что МАМА   \nмылА\nРаму\n",
            "А в этом не говорится",
        ),
        "first.txt\n",
        "first open test",
    ),
    (
        "Where am I\nsecond.txt\nfirst.txt\n",
        (
            "В этом файле говорится    о том что МАМА   \nмылА\nРаму\n",
            "А в этом не говорится",
        ),
        "404. Not Found\n",
        "404",
    ),
    (
        "Where am I\nsecond.txt\nfirst.txt\none more\nanother.log\none_more.csv\nemptyfile.txt\n",
        (
            "В этом файле говорится    о том что МАМА   \nмылА\nРаму\n",
            "А в этом не говорится",
            "where can I&nbsp;find\na cup of coffee\n\n\n\n at 10 AM\n",
            "Where&nbsp;am&nbsp;I",
            "&nbsp;&nbsp;&nbsp;&nbsp;",
            "\n\n\n\n\n\n\n\n\n\n",
        ),
        "another.log\n",
        "&nbsp; test",
    ),
    (
        "Where am I\nsecond.txt\nfirst.txt\none more\nfew_lines.log\none_more.csv\nemptyfile.txt\n",
        (
            "В этом файле говорится    о том что МАМА   \nмылА\nРаму\n",
            "А в этом не говорится",
            "where can I&nbsp;find\na cup of coffee\n\n\n\n at 10 AM\n",
            "Where\nam\n\n\n\n\n\n\nI\n",
            "&nbsp;&nbsp;&nbsp;&nbsp;",
            "\n\n\n\n\n\n\n\n\n\n",
        ),
        "few_lines.log\n",
        "a few lines phrase test",
    ),
    (
        "Where am I\ntab_lines.log\n",
        ("Where\tam\tI\t",),
        "tab_lines.log\n",
        "tab delimiter test",
    ),
    (
        "Where am I\ntab_lines.log\nanother.log\nthird\n",
        (
            "Where\tam\tI\t",
            "Where\tam\tI\t",
            "Where\tam\tI\t",
        ),
        "tab_lines.log\nanother.log\nthird\n",
        "the phrase in every sentence",
    ),
    (
        "Where am I\ntab_lines.log\n",
        ("WherE\naM\n\ni\n",),
        "tab_lines.log\n",
        "CaMeLcAsE test",
    ),
]

q_test_data = [
    ("᥈୥ᙬᱬᝯ, ᭷ᝯ୲੬๤!", {"Hello, world!", "Hello, world!\n"}, "first open test"),
    (
        "䥉†䑄楩獳汬楩歫敥†瑴潯†睷牲楩瑴敥†瑴敥獳瑴獳†晦潯牲†瑴桨楩獳†敥硸敥牲捣楩獳敥",
        {
            "I Dislike to write tests for this exercise",
            "I Dislike to write tests for this exercise\n",
        },
        "chinesse",
    ),
    (
        "I Dislike to write tests for this exercise!",
        {
            "I Dislike to write tests for this exercise!",
            "I Dislike to write tests for this exercise!\n",
        },
        "english",
    ),
    ("", {"", "\n"}, "empty"),
    (
        "乎潯ਊ煱畵楩敥牲潯ਊ灰牲潯扢慡牲ਊ敥獳瑴敥ਊ灰牲潯扢汬敥浭慡⸮ਊ",
        {
            "No\nquiero\nprobar\neste\nproblema.",
            "No\nquiero\nprobar\neste\nproblema.\n",
        },
        "spanish",
    ),
]

r_test_data = [
    ("file.txt\n", 67, "67Б", "first open test"),
    ("another_file.txt\n", 193, "193Б", "second open test"),
    ("temp.log\n", 1023, "1023Б", "almost Kb"),
    ("empty.sql\n", 1024, "1КБ", "one Kb"),
    ("query.sql\n", 102400, "100КБ", "Kb"),
    ("procedures.sql\n", 1047552, "1023КБ", "almost Mb"),
    ("photo.jpg\n", 1048576, "1МБ", "one Mb"),
    ("photo.raw\n", 138412032, "132МБ", "few Mb"),
    ("photo.mpeg\n", 138412037, "133МБ", "a few Mb more"),
    ("photos.tar\n", 1072693248, "1023МБ", "1023 Mb"),
    ("a_file.mp4\n", 1073741824, "1ГБ", "one Gb"),
    ("another_file.mp4\n", 20401094656, "19ГБ", "few Gb"),
    ("another_file.avro\n", 1099511627776, "1024ГБ", "1024 Gb"),
]

s_test_data = [
    ("3\n", "Hello, world!", "Khoor, zruog!", "first open test"),
    (
        "-10\n",
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "QRSTUVWXYZABCDEFGHIJKLMNOP",
        "second open test",
    ),
    ("0\n", "Hello, world!", "Hello, world!", "zero shift"),
    ("26\n", "Hello, world!", "Hello, world!", "26 shift"),
    ("-26\n", "Hello, world!", "Hello, world!", "-26 shift"),
    ("0\n", "Hello,\nworld!", "Hello,\nworld!", "zero shift two line"),
    ("26\n", "Hello,\nworld!", "Hello,\nworld!", "26 shift two lines"),
    ("-26\n", "Hello,\nworld!", "Hello,\nworld!", "-26 shift two lines"),
    (
        "-30\n",
        "abcdefghijklmnopqrstuvwxyz",
        "wxyzabcdefghijklmnopqrstuv",
        "big negative shift",
    ),
    (
        "-4\n",
        "abcdefghijklmnopqrstuvwxyz",
        "wxyzabcdefghijklmnopqrstuv",
        "small negative shift",
    ),
    (
        "4\n",
        "abcdefghijklmnopqrstuvwxyz",
        "efghijklmnopqrstuvwxyzabcd",
        "small positive shift",
    ),
    (
        "30\n",
        "abcdefghi\njklmnopqrstuvwxyz",
        "efghijklm\nnopqrstuvwxyzabcd",
        "big positive shift",
    ),
]

t_test_data = [
    (
        b"".join(
            map(lambda x: x.to_bytes(2, byteorder="big"), [1, 2, 3, 4, 5])
        ),
        "15\n",
        "first open test",
    ),
    (
        bytes.fromhex("00ff0101"),
        "512\n",
        "second open test",
    ),
    (
        int(0).to_bytes(2, byteorder="big"),
        "0\n",
        "zero",
    ),
    (
        int(65535).to_bytes(2, byteorder="big"),
        "65535\n",
        "16 bit",
    ),
    (
        b"".join(
            map(
                lambda x: x.to_bytes(2, byteorder="big"),
                [60000, 5000, 500, 30, 6],
            )
        ),
        "0\n",
        "cut to 0",
    ),
    (
        b"\x00\x01" * 65536,
        "0\n",
        "long file to zero",
    ),
]
