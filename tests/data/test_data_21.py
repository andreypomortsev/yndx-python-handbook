b_test_data = [
    ("Ann", "Как Вас зовут?\nПривет, Ann\n", "first open test"),
    ("Bob", "Как Вас зовут?\nПривет, Bob\n", "second open test"),
    ("bob", "Как Вас зовут?\nПривет, bob\n", "print input bob lower"),
    ("\n", "Как Вас зовут?\nПривет, \n", "print empty input"),
    ("   ", "Как Вас зовут?\nПривет,    \n", "print whitespace input"),
]


c_test_data = [
    ("2 + 2 = 4", "2 + 2 = 4\n2 + 2 = 4\n2 + 2 = 4\n", "first open test"),
    ("2 * 2 = 4", "2 * 2 = 4\n2 * 2 = 4\n2 * 2 = 4\n", "second open test"),
    (" ", " \n \n \n", "whitespace input"),
    ("\n", "\n\n\n", "print empty input (enter \n)"),
]


d_test_data = [
    ("100", "5\n", "first open test"),
    ("1000", "905\n", "thousand"),
    ("95", "0\n", "without change"),
    ("1000000", "999905\n", "million"),
]


e_test_data = [
    ("2\n3\n10\n", "4\n", "first open test"),
    ("187\n43\n8041\n", "0\n", "second open test"),
    ("0\n43\n8041\n", "8041\n", "zero price"),
    ("10\n0\n1000\n", "1000\n", "zero weight"),
    ("1000000\n1000\n2000000000\n", "1000000000\n", "big numbers"),
]


f_test_data = [
    (
        "черешня\n2\n3\n10\n",
        {
            "Чек\nчерешня - 3кг - 2руб/кг\nИтого: 6руб\nВнесено: 10руб\nСдача: 4руб\n",  # noqa E501
            "Чек\n    черешня - 3кг - 2руб/кг\n    Итого: 6руб\n    Внесено: 10руб\n    Сдача: 4руб\n",  # noqa E501
        },
        "first open test",
    ),
    (
        "манго\n187\n43\n8041\n",
        {
            "Чек\nманго - 43кг - 187руб/кг\nИтого: 8041руб\nВнесено: 8041руб\nСдача: 0руб\n",  # noqa E501
            "Чек\n    манго - 43кг - 187руб/кг\n    Итого: 8041руб\n    Внесено: 8041руб\n    Сдача: 0руб\n",  # noqa E501
        },
        "second open test",
    ),
    (
        "Кирпичи\n187\n43\n108041\n",
        {
            "Чек\nКирпичи - 43кг - 187руб/кг\nИтого: 8041руб\nВнесено: 108041руб\nСдача: 100000руб\n",  # noqa E501
            "Чек\n    Кирпичи - 43кг - 187руб/кг\n    Итого: 8041руб\n    Внесено: 108041руб\n    Сдача: 100000руб\n",  # noqa E501
        },
        "briks capitalized",
    ),
    (
        "БаНаНы\n200\n0\n0\n",
        {
            "Чек\nБаНаНы - 0кг - 200руб/кг\nИтого: 0руб\nВнесено: 0руб\nСдача: 0руб\n",  # noqa E501
            "Чек\n    БаНаНы - 0кг - 200руб/кг\n    Итого: 0руб\n    Внесено: 0руб\n    Сдача: 0руб\n",  # noqa E501
        },
        "zero receipt",
    ),
    (
        "Черная Смородина\n500\n1\n1000\n",
        {
            "Чек\nЧерная Смородина - 1кг - 500руб/кг\nИтого: 500руб\nВнесено: 1000руб\nСдача: 500руб\n",  # noqa E501
            "Чек\n    Черная Смородина - 1кг - 500руб/кг\n    Итого: 500руб\n    Внесено: 1000руб\n    Сдача: 500руб\n",  # noqa E501
        },
        "two words product",
    ),
]


g_test_data = [
    ("1\n", "Купи слона!\n\n", "first open test"),
    ("3\n", "Купи слона!\nКупи слона!\nКупи слона!\n\n", "second open test"),
    ("0\n", "\n", "no elephants"),
    (
        "5\n",
        "Купи слона!\nКупи слона!\nКупи слона!\nКупи слона!\nКупи слона!\n\n",
        "five elephants",
    ),
    (
        "21\n",
        """Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!
Купи слона!

""",
        "lots of elephants",
    ),
]


h_test_data = [
    (
        "2\nКупи слона!\n",
        """Я больше никогда не буду писать "Купи слона!"!
Я больше никогда не буду писать "Купи слона!"!\n""",
        "first open test",
    ),
    (
        "3\nПопка дурак!\n",
        """Я больше никогда не буду писать "Попка дурак!"!
Я больше никогда не буду писать "Попка дурак!"!
Я больше никогда не буду писать "Попка дурак!"!
""",
        "second open test",
    ),
    (
        "1\nLet's Rock!",
        """Я больше никогда не буду писать "Let's Rock!"!\n""",
        "single quote",
    ),
    ('1\n"\n', 'Я больше никогда не буду писать """!\n', "double quote"),
    (
        "3\nIt's movin'",
        """Я больше никогда не буду писать "It's movin'"!
Я больше никогда не буду писать "It's movin'"!
Я больше никогда не буду писать "It's movin'"!\n""",
        "single quotes",
    ),
]


i_test_data = [
    ("2\n2\n", "2\n", "first open test"),
    ("10\n10\n", "50\n", "second open test"),
    ("1\n1\n", "0\n", "only child"),
    ("10080\n1\n", "5040\n", "long week with one child"),
    ("10080\n80\n", "403200\n", "long week with children"),
]


k_test_data = [
    (
        "1234\n",
        "2143\n",
        "first open test",
    ),
    ("1412\n", "4121\n", "second open test"),
    ("1001\n", "0110\n", "zeros inside"),
    ("1000\n", "0100\n", "thousand"),
    ("0000\n", "0000\n", "all zeros"),
]


l_test_data = [
    ("123\n99\n", "112\n", "first open test"),
    ("405\n839\n", "234\n", "second open test"),
    ("9\n2\n", "1\n", "nine two"),
    ("369\n741\n", "0\n", "filty trick"),
    ("111\n899\n", "900\n", "more than thousand"),
    ("0\n899\n", "899\n", "one zero"),
    ("345\n0\n", "345\n", "another zero"),
    ("0\n0\n", "0\n", "everything is zero"),
    ("99\n2\n", "91\n", "ones check"),
    ("429\n590\n", "919\n", "tens check"),
    ("533\n566\n", "99\n", "hundreds check"),
    ("123\n123\n", "246\n", "normal add"),
]


m_test_data = [
    ("3\n100\n", "33\n1\n", "first open test"),
    ("20\n500\n", "25\n0\n", "second open test"),
    ("100\n0\n", "0\n0\n", "many kids zero candies"),
    ("0\n741\n", "0\n741\n", "no children many candies"),
    ("0\n0\n", "0\n0\n", "no children no candies"),
    ("24\n25\n", "1\n1\n", "more candies"),
    ("25\n24\n", "0\n24\n", "more children"),
    ("1_000_000_000\n3_333_333_333\n", "3\n333333333\n", "big party"),
]


n_test_data = [
    ("1\n2\n3\n", "5\n", "first open test"),
    ("1\n1\n1\n", "3\n", "equal with ones"),
    ("10\n10\n10\n", "21\n", "equal with tens"),
    ("9\n3\n7\n", "17\n", "more reds than blues"),
    ("7\n3\n9\n", "17\n", "more blues than reds"),
    ("19\n300\n19\n", "39\n", "a lot of greens blue and red are equal"),
    (
        "10_000_000_000\n3_333_333_333\n3_333_333_333\n",
        "13333333334\n",
        "big numbers",
    ),
    ("0\n3\n33\n", "34\n", "zero reds"),
    ("31\n3\n0\n", "32\n", "zero blues"),
    ("0\n3\n0\n", "1\n", "all greens"),
]


o_test_data = [
    ("8\n0\n65\n", "09:05\n", "first open test"),
    ("10\n15\n2752\n", "08:07\n", "second open test"),
    ("23\n59\n0\n", "23:59\n", "zero delivery time"),
    ("23\n59\n1\n", "00:00\n", "fast delivery time"),
    ("23\n59\n1_000_000_000\n", "10:39\n", "very long delivery time"),
    ("19\n20\n60\n", "20:20\n", "check hours"),
    ("23\n20\n41\n", "00:01\n", "check midnight"),
    ("19\n20\n39\n", "19:59\n", "check minutes"),
    ("23\n21\n1441\n", "23:22\n", "a few days long delivery"),
    ("00\n01\n1440\n", "00:01\n", "next day delivery"),
    ("20\n00\n240\n", "00:00\n", "at midnight"),
]
