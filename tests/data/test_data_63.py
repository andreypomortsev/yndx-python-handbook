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