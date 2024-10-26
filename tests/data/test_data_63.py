a_test_data = [
    ("Привет!", "first open test"),
    ("Сервер работает в штатном режиме", "second open test"),
    ("Learing requests is an important step\nSo, let's go!", "two lines"),
]

b_test_data = [
    ("127.0.0.1:5000", ("1", "2", "3", "0"), "6", "first open test"),
    ("127.0.0.1:8080", ("7", "3", "-5", "2", "0"), "7", "second open test"),
    (
        "127.0.0.1:8081",
        ("-7", "-3", "-5", "-2", "0"),
        "-17",
        "negative values",
    ),
    (
        "8.8.8.8:5000",
        ("7000", "21313", "0", "31245", "43522", "312324141"),
        "28313",
        "shifted end",
    ),
    ("127.0.0.1:8081", ("0", "-7", "-3", "-5", "-2", "0"), "0", "zero"),
]

c_test_data = [
    ("127.0.0.1:5000", [1, 2, "ошибка", 3], "6", "first open test"),
    ("127.0.0.1:8080", [7, 3, ["ошибка"], -5, 2], "7", "second open test"),
    (
        "127.0.0.1:8081",
        [["ошибка"], ("ошибка"), -7, -3, list("Error"), -5, -2],
        "-17",
        "negative values",
    ),
    (
        "8.8.8.8:5000",
        [7000, 21313, 0, 31245, 43522, 312324141],
        "312427221",
        "shifted end",
    ),
    (
        "127.0.0.1:8081",
        [
            17,
            ["ошибка"],
            ("ошибка"),
            ["ошибка"],
            ("ошибка"),
            ["ошибка"],
            ("ошибка"),
            ["ошибка"],
            ("ошибка"),
            -7,
            -3,
            -5,
            -2,
        ],
        "0",
        "zero",
    ),
    (
        "127.0.0.1:8081",
        [
            ["ошибка"],
            ("ошибка"),
            "ошибка",
            ("ошибка"),
            ["ошибка"],
            ("ошибка"),
            ["ошибка"],
            ("ошибка"),
        ],
        "0",
        "only errors",
    ),
]

d_test_data = [
    (
        "127.0.0.1:5000",
        "second",
        {"first": "1", "second": "2"},
        "2",
        "first open test",
    ),
    (
        "127.0.0.1:8080",
        "second",
        {"first": "1", "third": "3"},
        "No data",
        "second open test",
    ),
    (
        "127.0.0.1:8081",
        "another",
        {"first": "1", "second": "2", "another": "day"},
        "day",
        "another day",
    ),
    (
        "192.168.0.1:80",
        "226",
        {
            "655": "115",
            "26": "760",
            "282": "251",
            "229": "143",
            "755": "105",
            "693": "759",
            "914": "559",
            "90": "605",
            "433": "33",
            "31": "96",
            "224": "239",
            "518": "617",
            "28": "575",
            "204": "734",
            "666": "719",
            "559": "430",
            "226": "460",
            "604": "285",
            "829": "891",
            "7": "778",
            "826": "164",
            "715": "433",
            "349": "285",
            "160": "221",
            "981": "782",
            "345": "105",
            "95": "390",
            "100": "368",
            "868": "353",
            "619": "271",
        },
        "460",
        "numbers",
    ),
    (
        "192.168.0.1:80",
        "-883",
        {
            "-345": "130.1887434491704",
            "-430": "-175.38874728726867",
            "-299": "-106.95212175775367",
            "-137": "182.39156478331205",
            "-206": "-282.02255915883853",
            "-766": "217.40565226352905",
            "-968": "206.26480624709637",
            "-677": "-56.97746962689853",
            "-726": "-275.33805154897897",
            "-784": "276.9296009798979",
            "-35": "-310.9887588015635",
            "-103": "149.60564650638162",
            "-678": "-179.84508569384172",
            "-329": "7.002817496043395",
            "-595": "258.14931769505426",
            "-64": "100.58592403407786",
            "-531": "-225.3633994181238",
            "-729": "-227.59156862141035",
            "-748": "167.1126902464901",
            "-426": "32.78591827693044",
            "-731": "168.38592979122527",
            "-402": "-39.152116000606256",
            "-81": "62.07042780583918",
            "-592": "-82.44226052160178",
            "-776": "-228.2281883937779",
            "-479": "3.183098861837907",
            "-907": "174.1155077425335",
            "-952": "242.8704431582323",
            "-888": "-218.6788918082642",
            "-358": "-214.22255340169113",
            "-189": "125.09578527022974",
            "-568": "70.34648484661774",
            "-935": "-67.48169587096362",
            "-610": "70.02817496043394",
            "-521": "26.419720553254628",
            "-743": "314.4901675495852",
            "-434": "242.5521332720485",
            "-304": "151.51550582348438",
            "-883": "126.0507149287811",
        },
        "126.0507149287811",
        "negative numbers",
    ),
]

e_test_data = [
    (
        "127.0.0.1:5000",
        "/first\n/third\n",
        {"/first": [1, 2, 3], "/second": [2, 4, 6], "/third": [3, 6, 9]},
        "24",
        "first open test",
    ),
    (
        "127.0.0.1:8080",
        "/second\n",
        {"/first": [1, 2, 3], "/second": [2, 4, 6], "/third": [3, 6, 9]},
        "12",
        "second open test",
    ),
    (
        "127.0.0.1:5000",
        "/long/second/path\n/first\n/third\n",
        {
            "/first": [1, 2, 3],
            "/long/second/path": [2, 4, 6],
            "/third": [3, 6, 9],
        },
        "36",
        "all paths",
    ),
    (
        "127.0.0.1:8080",
        "/first\n",
        {"/first": (1, 2, 3), "/second": (2, 4, 6), "/third": (3, 6, 9)},
        "6",
        "tuples",
    ),
    (
        "127.0.0.1:8080",
        "/first\n",
        {
            "/first": (-1, -2, -3),
            "/second": (-2, -4, -6),
            "/third": (-3, -6, -9),
        },
        "-6",
        "tuples with negative values",
    ),
    (
        "127.0.0.1:8080",
        "/first\n",
        {"/first": (0, 0, 0), "/second": (2, 4, 6), "/third": (3, 6, 9)},
        "0",
        "tuples with zeros",
    ),
    (
        "127.0.0.1:5000",
        "/long/second/path\n/first\n/third\n",
        {"/first": [1], "/long/second/path": [6], "/third": [6]},
        "13",
        "all paths with one element",
    ),
]

f_test_data = [
    (
        "127.0.0.1:5000",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Иванов Василий\nИванов Виктор\nПетрова Елизавета",
        "first open test",
    ),
    (
        "127.0.0.1:8080",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Иванов Василий\nИванов Виктор\nПетрова Елизавета",
        "different port",
    ),
    (
        "192.168.0.1:8080",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Иванов Василий\nИванов Виктор\nПетрова Елизавета",
        "different ip",
    ),
    (
        "127.0.0.1:8080",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
            {
                "id": 4,
                "username": "fourth",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Иванов Василий\nИванов Виктор\nИванов Виктор\nПетрова Елизавета",
        "repeated names",
    ),
    (
        "127.0.0.1:8080",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
        ],
        "Петрова Елизавета",
        "one name",
    ),
    (
        "127.0.0.1:8080",
        [],
        "",
        "empty return",
    ),
]

g_test_data = [
    (
        "127.0.0.1:5000",
        2,
        "Письмо для: {email}\n"
        "Здравствуйте, {last_name} {first_name}\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!\n",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Письмо для: vas.ivanov@server.none\n"
        "Здравствуйте, Иванов Василий\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!",
        "first open test",
    ),
    (
        "127.0.0.1:8080",
        2,
        "Письмо для: {email}\n"
        "Здравствуйте, {last_name} {first_name}\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!\n",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Письмо для: vas.ivanov@server.none\n"
        "Здравствуйте, Иванов Василий\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!",
        "different port",
    ),
    (
        "8.8.8.8:8080",
        2,
        "Письмо для: {email}\n"
        "Здравствуйте, {last_name} {first_name}\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!\n",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Письмо для: vas.ivanov@server.none\n"
        "Здравствуйте, Иванов Василий\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!",
        "different ip",
    ),
    (
        "127.0.0.1:8080",
        1,
        "Письмо для: {email}\n"
        "Здравствуйте, {last_name} {first_name}\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!\n",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Письмо для: e.petrova@server.none\n"
        "Здравствуйте, Петрова Елизавета\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!",
        "different user id",
    ),
    (
        "127.0.0.1:8080",
        4,
        "Письмо для: {email}\n"
        "Здравствуйте, {last_name} {first_name}\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!\n",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Пользователь не найден",
        "No user found",
    ),
    (
        "127.0.0.1:8080",
        4,
        "Письмо для: {email}\n"
        "Здравствуйте, {last_name} {first_name}\n"
        "Мы рады сообщить вам о предстоящей акции!\n"
        "Все подробности на нашем сайте\n"
        "С уважением, команда тестового сервера!\n",
        [],
        "Пользователь не найден",
        "No user found empty response",
    ),
    (
        "127.0.0.1:8080",
        1,
        "Письмо для: {email}\n"
        "Здравствуйте, {username}\n"
        "Мы обнаружили подозрительную активность на Вашем аккаунте и временно его заморозили.\n"
        "Все подробности на нашем сайте: https://www.linkedin.com/in/andreypomortsev/\n"
        "С уважением, команда тестового сервера!\n",
        [
            {
                "id": 1,
                "username": "first",
                "last_name": "Петрова",
                "first_name": "Елизавета",
                "email": "e.petrova@server.none",
            },
            {
                "id": 2,
                "username": "second",
                "last_name": "Иванов",
                "first_name": "Василий",
                "email": "vas.ivanov@server.none",
            },
            {
                "id": 3,
                "username": "third",
                "last_name": "Иванов",
                "first_name": "Виктор",
                "email": "vik.ivanov@server.none",
            },
        ],
        "Письмо для: e.petrova@server.none\n"
        "Здравствуйте, first\n"
        "Мы обнаружили подозрительную активность на Вашем аккаунте и временно его заморозили.\n"
        "Все подробности на нашем сайте: https://www.linkedin.com/in/andreypomortsev/\n"
        "С уважением, команда тестового сервера!",
        "different message",
    ),
]

h_test_data = [
    (
        (
            "127.0.0.1:5000",
            "fourth",
            "Петров",
            "Кирилл",
            "k.petrov@server.none",
        ),
        {
            "username": "fourth",
            "last_name": "Петров",
            "first_name": "Кирилл",
            "email": "k.petrov@server.none",
        },
        "first open test",
    ),
    (
        (
            "127.0.0.1:8081",
            "fourth",
            "Петров",
            "Кирилл",
            "k.petrov@server.none",
        ),
        {
            "username": "fourth",
            "last_name": "Петров",
            "first_name": "Кирилл",
            "email": "k.petrov@server.none",
        },
        "different port",
    ),
    (
        (
            "192.168.0.1:5000",
            "fourth",
            "Петров",
            "Кирилл",
            "k.petrov@server.none",
        ),
        {
            "username": "fourth",
            "last_name": "Петров",
            "first_name": "Кирилл",
            "email": "k.petrov@server.none",
        },
        "different ip",
    ),
    (
        (
            "127.0.0.1:5000",
            "fourth",
            "Петров",
            "Кирилл",
            "k.petrov@server.none",
        ),
        {
            "username": "fourth",
            "last_name": "Петров",
            "first_name": "Кирилл",
            "email": "k.petrov@server.none",
        },
        "first user",
    ),
    (
        (
            "192.168.0.1:5000",
            "first",
            "Петрова",
            "Елизавета",
            "e.petrova@server.none",
        ),
        {
            "username": "first",
            "last_name": "Петрова",
            "first_name": "Елизавета",
            "email": "e.petrova@server.none",
        },
        "different user",
    ),
]

i_test_data = [
    (
        (
            "127.0.0.1:5000",
            "2",
            "username=ivanov_vasily",
            "email=ivanov_vasily@server.none",
        ),
        {
            "username": "ivanov_vasily",
            "email": "ivanov_vasily@server.none",
        },
        "first open test",
    ),
    (
        (
            "127.0.0.1:8080",
            "2",
            "username=ivanov_vasily",
            "email=ivanov_vasily@server.none",
        ),
        {
            "username": "ivanov_vasily",
            "email": "ivanov_vasily@server.none",
        },
        "different port",
    ),
    (
        (
            "192.168.0.1:5000",
            "2",
            "username=ivanov_vasily",
            "email=ivanov_vasily@server.none",
        ),
        {
            "username": "ivanov_vasily",
            "email": "ivanov_vasily@server.none",
        },
        "different ip",
    ),
    (
        (
            "192.168.0.1:5000",
            "2",
            "username=first",
            "last_name=Петрова",
            "first_name=Елизавета",
            "email=e.petrova@server.none",
        ),
        {
            "username": "first",
            "last_name": "Петрова",
            "first_name": "Елизавета",
            "email": "e.petrova@server.none",
        },
        "all fields",
    ),
    (
        (
            "192.168.0.1:5000",
            "2",
            "username=new_first",
        ),
        {
            "username": "new_first",
        },
        "change username",
    ),
    (
        (
            "192.168.0.1:5000",
            "2",
            "last_name=Петрова",
        ),
        {
            "last_name": "Петрова",
        },
        "change last name",
    ),
    (
        (
            "192.168.0.1:5000",
            "2",
            "first_name=Елизавета",
        ),
        {
            "first_name": "Елизавета",
        },
        "change first name",
    ),
    (
        ("192.168.0.1:5000", "2", "email=e.petrova@server.none"),
        {"email": "e.petrova@server.none"},
        "change email",
    ),
]

j_test_data = [
    (("127.0.0.1:5000", "2"), "first open test"),
    (("127.0.0.1:8080", "2"), "different port"),
    (("192.168.0.1:5000", "2"), "different ip"),
    (("192.168.0.1:5000", "1"), "different user_id"),
]
