a_test_data = [
    (
        "Аня\nхорошо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, Аня!\n"
        "Как дела?\n"
        "Я за вас рада!\n",
        "first open test",
    ),
    (
        "Боря\nплохо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, Боря!\n"
        "Как дела?\n"
        "Всё наладится!\n",
        "second open test",
    ),
    (
        "\nхорошо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, !\n"
        "Как дела?\n"
        "Я за вас рада!\n",
        "empty name good",
    ),
    (
        "\nплохо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, !\n"
        "Как дела?\n"
        "Всё наладится!\n",
        "empty name bad",
    ),
    (
        " \nхорошо\n",
        "Как Вас зовут?\n"
        "Здравствуйте,  !\n"
        "Как дела?\n"
        "Я за вас рада!\n",
        "whitespace good",
    ),
    (
        " \nплохо\n",
        "Как Вас зовут?\n"
        "Здравствуйте,  !\n"
        "Как дела?\n"
        "Всё наладится!\n",
        "whitespace bad",
    ),
    (
        "CaMeL\nхорошо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, CaMeL!\n"
        "Как дела?\n"
        "Я за вас рада!\n",
        "CaMeLcAsE good",
    ),
    (
        "CaMeL\nплохо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, CaMeL!\n"
        "Как дела?\n"
        "Всё наладится!\n",
        "CaMeLcAsE bad",
    ),
    (
        "Баба Яга\nхорошо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, Баба Яга!\n"
        "Как дела?\n"
        "Я за вас рада!\n",
        "double name good",
    ),
    (
        "Баба Яга\nплохо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, Баба Яга!\n"
        "Как дела?\n"
        "Всё наладится!\n",
        "double name bad",
    ),
]


b_test_data = [
    ("10\n5\n", "Петя\n", "first open test"),
    ("5\n7\n", "Вася\n", "second open test"),
    ("0\n5\n", "Вася\n", "zero speed one"),
    ("10\n0\n", "Петя\n", "zero speed two"),
    ("4.99\n4\n", "Петя\n", "float speed one"),
    ("10\n10.01\n", "Вася\n", "float speed two"),
    ("10.02\n10.01\n", "Петя\n", "float first greater"),
    ("10.01\n10.02\n", "Вася\n", "float second greater"),
    ("10.000000002\n10.000000001\n", "Петя\n", "float first bit greater"),
    ("10.000000001\n10.000000002\n", "Вася\n", "float second bit greater"),
]


c_test_data = [
    ("10\n5\n7\n", "Петя\n", "first open test"),
    ("5\n7\n10\n", "Толя\n", "second open test"),
    ("5\n10\n7\n", "Вася\n", "vasya wins"),
    ("10.3\n10.2\n10.1\n", "Петя\n", "float petya wins"),
    ("10.1\n10.2\n10.3\n", "Толя\n", "float tolya wins"),
    ("10.1\n10.3\n10.2\n", "Вася\n", "float vasya wins"),
    (
        "0.0000000000000003\n0.0000000000000002\n0.0000000000000001\n",
        "Петя\n",
        "small float petya wins",
    ),
    (
        "0.0000000000000001\n0.0000000000000002\n0.0000000000000003\n",
        "Толя\n",
        "small float tolya wins",
    ),
    (
        "0.0000000000000001\n0.0000000000000003\n0.0000000000000002\n",
        "Вася\n",
        "small float vasya wins",
    ),
    (
        "0.0000000000000003\n0\n0\n",
        "Петя\n",
        "small float and zeros petya wins",
    ),
    (
        "0\n0\n0.0000000000000003\n",
        "Толя\n",
        "small float and zeros tolya wins",
    ),
    (
        "0\n0.0000000000000003\n0\n",
        "Вася\n",
        "small float and zeros vasya wins",
    ),
    (
        "10000000000000003\n10000000000000002\n10000000000000001\n",
        "Петя\n",
        "huge int petya wins",
    ),
    (
        "10000000000000001\n10000000000000002\n10000000000000003\n",
        "Толя\n",
        "huge int tolya wins",
    ),
    (
        "10000000000000001\n10000000000000003\n10000000000000002\n",
        "Вася\n",
        "huge int vasya wins",
    ),
]


d_test_data = [
    (
        "10\n5\n7\n",  # Скорости: Петя Вася Толя
        {
            "1. Петя\n2. Толя\n3. Вася\n",
            "1. Петя\n    2. Толя\n    3. Вася\n",
            "1. Петя\n    2. Толя\n    3. Вася",
        },
        "first open test",
    ),
    (
        "10\n7\n5\n",
        {
            "1. Петя\n2. Вася\n3. Толя\n",
            "1. Петя\n    2. Вася\n    3. Толя\n",
            "1. Петя\n    2. Вася\n    3. Толя",
        },
        "first open test 2-3 swap",
    ),
    (
        "5\n7\n10\n",
        {
            "1. Толя\n2. Вася\n3. Петя\n",
            "1. Толя\n    2. Вася\n    3. Петя\n",
            "1. Толя\n    2. Вася\n    3. Петя",
        },
        "second open test",
    ),
    (
        "7\n5\n10\n",
        {
            "1. Толя\n2. Петя\n3. Вася\n",
            "1. Толя\n    2. Петя\n    3. Вася\n",
            "1. Толя\n    2. Петя\n    3. Вася",
        },
        "second open test 2-3 swap",
    ),
    (
        "5\n10\n7\n",
        {
            "1. Вася\n2. Толя\n3. Петя\n",
            "1. Вася\n    2. Толя\n    3. Петя\n",
            "1. Вася\n    2. Толя\n    3. Петя",
        },
        "third open-like test",
    ),
    (
        "7\n10\n5\n",
        {
            "1. Вася\n2. Петя\n3. Толя\n",
            "1. Вася\n    2. Петя\n    3. Толя\n",
            "1. Вася\n    2. Петя\n    3. Толя",
        },
        "third open-like test 2-3 swap",
    ),
    (
        "10.3\n10.1\n10.2\n",  # Скорости: Петя Вася Толя
        {
            "1. Петя\n2. Толя\n3. Вася\n",
            "1. Петя\n    2. Толя\n    3. Вася\n",
            "1. Петя\n    2. Толя\n    3. Вася",
        },
        "float p t v",
    ),
    (
        "10.3\n10.2\n10.1\n",
        {
            "1. Петя\n2. Вася\n3. Толя\n",
            "1. Петя\n    2. Вася\n    3. Толя\n",
            "1. Петя\n    2. Вася\n    3. Толя",
        },
        "float p v t",
    ),
    (
        "10.2\n10.3\n10.1\n",
        {
            "1. Вася\n2. Петя\n3. Толя\n",
            "1. Вася\n    2. Петя\n    3. Толя\n",
            "1. Вася\n    2. Петя\n    3. Толя",
        },
        "float v p t",
    ),
    (
        "10.1\n10.3\n10.2\n",
        {
            "1. Вася\n2. Толя\n3. Петя\n",
            "1. Вася\n    2. Толя\n    3. Петя\n",
            "1. Вася\n    2. Толя\n    3. Петя",
        },
        "float v t p",
    ),
    (
        "10.1\n10.2\n10.3\n",
        {
            "1. Толя\n2. Вася\n3. Петя\n",
            "1. Толя\n    2. Вася\n    3. Петя\n",
            "1. Толя\n    2. Вася\n    3. Петя",
        },
        "float t v p",
    ),
    (
        "10.2\n10.1\n10.3\n",
        {
            "1. Толя\n2. Петя\n3. Вася\n",
            "1. Толя\n    2. Петя\n    3. Вася\n",
            "1. Толя\n    2. Петя\n    3. Вася",
        },
        "float t p v",
    ),
    (
        "0.00000000003\n0.00000000001\n0.00000000002\n",  # Скорости: Петя Вася Толя
        {
            "1. Петя\n2. Толя\n3. Вася\n",
            "1. Петя\n    2. Толя\n    3. Вася\n",
            "1. Петя\n    2. Толя\n    3. Вася",
        },
        "small float p t v",
    ),
    (
        "0.00000000003\n0.00000000002\n0.00000000001\n",
        {
            "1. Петя\n2. Вася\n3. Толя\n",
            "1. Петя\n    2. Вася\n    3. Толя\n",
            "1. Петя\n    2. Вася\n    3. Толя",
        },
        "small float p v t",
    ),
    (
        "0.00000000002\n0.00000000003\n0.00000000001\n",
        {
            "1. Вася\n2. Петя\n3. Толя\n",
            "1. Вася\n    2. Петя\n    3. Толя\n",
            "1. Вася\n    2. Петя\n    3. Толя",
        },
        "small float v p t",
    ),
    (
        "0.00000000001\n0.00000000003\n0.00000000002\n",
        {
            "1. Вася\n2. Толя\n3. Петя\n",
            "1. Вася\n    2. Толя\n    3. Петя\n",
            "1. Вася\n    2. Толя\n    3. Петя",
        },
        "small float v t p",
    ),
    (
        "0.00000000001\n0.00000000002\n0.00000000003\n",
        {
            "1. Толя\n2. Вася\n3. Петя\n",
            "1. Толя\n    2. Вася\n    3. Петя\n",
            "1. Толя\n    2. Вася\n    3. Петя",
        },
        "small float t v p",
    ),
    (
        "0.00000000002\n0.00000000001\n0.00000000003\n",
        {
            "1. Толя\n2. Петя\n3. Вася\n",
            "1. Толя\n    2. Петя\n    3. Вася\n",
            "1. Толя\n    2. Петя\n    3. Вася",
        },
        "small float t p v",
    ),
    (
        "1000000000003\n1000000000001\n1000000000002\n",  # Скорости: Петя Вася Толя
        {
            "1. Петя\n2. Толя\n3. Вася\n",
            "1. Петя\n    2. Толя\n    3. Вася\n",
            "1. Петя\n    2. Толя\n    3. Вася",
        },
        "big float p t v",
    ),
    (
        "1000000000003\n1000000000002\n1000000000001\n",
        {
            "1. Петя\n2. Вася\n3. Толя\n",
            "1. Петя\n    2. Вася\n    3. Толя\n",
            "1. Петя\n    2. Вася\n    3. Толя",
        },
        "big float p v t",
    ),
    (
        "1000000000002\n1000000000003\n1000000000001\n",
        {
            "1. Вася\n2. Петя\n3. Толя\n",
            "1. Вася\n    2. Петя\n    3. Толя\n",
            "1. Вася\n    2. Петя\n    3. Толя",
        },
        "big float v p t",
    ),
    (
        "1000000000001\n1000000000003\n1000000000002\n",
        {
            "1. Вася\n2. Толя\n3. Петя\n",
            "1. Вася\n    2. Толя\n    3. Петя\n",
            "1. Вася\n    2. Толя\n    3. Петя",
        },
        "big float v t p",
    ),
    (
        "1000000000001\n1000000000002\n1000000000003\n",
        {
            "1. Толя\n2. Вася\n3. Петя\n",
            "1. Толя\n    2. Вася\n    3. Петя\n",
            "1. Толя\n    2. Вася\n    3. Петя",
        },
        "big float t v p",
    ),
    (
        "1000000000002\n1000000000001\n1000000000003\n",
        {
            "1. Толя\n2. Петя\n3. Вася\n",
            "1. Толя\n    2. Петя\n    3. Вася\n",
            "1. Толя\n    2. Петя\n    3. Вася",
        },
        "big float t p v",
    ),
]


e_test_data = [
    ("3\n5\n", "Вася\n", "first open test"),
    ("10\n2\n", "Петя\n", "second open test"),
    ("9\n3\n", "Ровно\n", "equal"),
    ("0\n0\n", "Вася\n", "zero input"),
    ("5\n9\n", "Вася\n", "min diff vasya"),
    ("8\n1\n", "Петя\n", "min diff petya"),
    ("1000000003\n1000000005\n", "Вася\n", "huge first open test"),
    ("10000000010\n1000000002\n", "Петя\n", "huge second open test"),
    ("1000000009\n1000000003\n", "Ровно\n", "huge equal"),
    ("0\n9\n", "Вася\n", "zero to vasya"),
    ("8\n0\n", "Петя\n", "zero to petya petya"),
]


f_test_data = [
    ("2022\n", "NO\n", "first open test"),
    ("2020\n", "YES\n", "second open test"),
    ("1900\n", "NO\n", "century without leap"),
    ("2000\n", "YES\n", "century leap year"),
    ("2100\n", "NO\n", "future non-leap century"),
    ("2400\n", "YES\n", "future leap century"),
    ("1800\n", "NO\n", "old century non-leap"),
    ("1600\n", "YES\n", "old leap century"),
    ("2024\n", "YES\n", "current leap year"),
    ("2019\n", "NO\n", "recent non-leap year"),
    ("0004\n", "YES\n", "second leap year"),
    ("1\n", "NO\n", "the beginning"),
]


g_test_data = [
    ("1234\n", "NO\n", "first open test"),
    ("2332\n", "YES\n", "second open test"),
    ("0001\n", "NO\n", "starts with zeros neg"),
    ("1000\n", "NO\n", "ends with zeros neg"),
    ("0990\n", "YES\n", "starts with zeros pos"),
    ("7007\n", "YES\n", "middle zeros pos"),
    ("3399\n", "NO\n", "different halves test"),
    ("7177\n", "NO\n", "almost palindrome test"),
    ("4141\n", "NO\n", "alternating digits test"),
    ("0000\n", "YES\n", "all zeros pos"),
    ("0300\n", "NO\n", "ends with zeros neg"),
    ("1221\n", "YES\n", "common palindrome test"),
    ("4004\n", "YES\n", "mirror palindrome test"),
    ("1881\n", "YES\n", "eights and ones pos"),
    ("7117\n", "YES\n", "reversed digits pos"),
]


h_test_data = [
    ("березка елочка зайка волк березка\n", "YES\n", "first open test"),
    (
        "сосна сосна сосна елочка грибочки медведь\n",
        "NO\n",
        "second open test",
    ),
    (
        "березка елочка волк березка "
        "сосна сосна сосна елочка грибочки медведь "
        "березка елочка волк березка "
        "сосна сосна сосна елочка грибочки медведь "
        "березка елочка волк березка "
        "сосна сосна сосна елочка грибочки медведь "
        "зайка сосна сосна сосна елочка грибочки медведь \n",
        "YES\n",
        "long line",
    ),
    ("березка елочка волк березка зайка\n", "YES\n", "last word"),
    ("заика березка елочка волк березка\n", "NO\n", "misspelled"),
]


i_test_data = [
    ("Вова\nАня\nБоря\n", "Аня\n", "first open test"),
    ("Толя\nКоля\nВася\n", "Вася\n", "second open test"),
    ("АHна\nАнна\nАнна\n", "АHна\n", "identical names"),
    ("Гриша\nМиша\nДима\n", "Гриша\n", "names with different first letters"),
    ("Яша\nЮра\nЯна\n", "Юра\n", "names with similar letters"),
    ("Алекс\nАлла\nАльберт\n", "Алекс\n", "same first letters"),
    ("Зина\nКатя\nЖеня\n", "Женя\n", "middle alphabet"),
    ("Саша\nАня\nОля\n", "Аня\n", "mixed order"),
    ("Лена\nАня\nВаля\n", "Аня\n", "alphabetical"),
    ("Олег\nИгорь\nАртём\n", "Артём\n", "reverse order"),
]


j_test_data = [
    ("123\n", "53\n", "first open test"),
    ("741\n", "115\n", "second open test"),
    ("111\n", "22\n", "all ones test"),
    ("999\n", "1818\n", "max digits test"),
    ("321\n", "53\n", "decreasing digits test"),
    ("256\n", "117\n", "middle digit test"),
    ("804\n", "84\n", "zero in middle test"),
    ("500\n", "50\n", "leading zeros in sums test"),
    ("111\n", "22\n", "all digits the same test"),
    ("970\n", "167\n", "last digit zero test"),
    ("000\n", "00\n", "all zeros test"),
    ("001\n", "10\n", "leading zeros test"),
]


k_test_data = [
    ("123\n", "YES\n", "first open test"),
    ("748\n", "NO\n", "second open test"),
    ("321\n", "YES\n", "digits in descending order"),
    ("921\n", "NO\n", "digits in descending order not beautiful"),
    ("111\n", "YES\n", "same digits"),
    ("555\n", "YES\n", "same digits middle condition still holds"),
    ("532\n", "NO\n", "highest digit first, not beautiful"),
    ("100\n", "NO\n", "edge case with small values and not beautiful"),
]


l_test_data = [
    ("3\n3\n3\n", "YES\n", "first open test"),
    ("1\n2\n3\n", "NO\n", "second open test"),
    ("5\n5\n5\n", "YES\n", "equilateral triangle"),
    ("2\n2\n3\n", "YES\n", "isosceles triangle"),
    ("2\n3\n4\n", "YES\n", "scalene triangle"),
    ("1\n1\n2\n", "NO\n", "not a triangle, sum equals third side"),
    ("10\n1\n1\n", "NO\n", "not a triangle, one side much larger"),
    ("0\n0\n0\n", "NO\n", "zero sides, invalid triangle"),
    ("5\n10\n15\n", "NO\n", "degenerate case, sum equals third side"),
    ("1000000\n1000000\n1000000\n", "YES\n", "large equilateral triangle"),
]


m_test_data = [
    ("12\n13\n14\n", "1\n", "first open test"),
    ("23\n13\n63\n", "3\n", "second open test"),
    ("21\n22\n23\n", "2\n", "all first digits same"),
    ("41\n43\n49\n", "4\n", "all first digits same, different middle digits"),
    ("10\n20\n30\n", "0\n", "increasing first digits"),
    ("59\n49\n39\n", "9\n", "decreasing first digits"),
    ("77\n72\n77\n", "7\n", "two equal one bigger"),
    ("88\n78\n88\n", "8\n", "two equal one smaller"),
]


n_test_data = [
    ("103\n", "10 31\n", "first open test"),
    ("787\n", "77 87\n", "second open test"),
    ("567\n", "56 76\n", "digits in descending order"),
    ("123\n", "12 32\n", "digits in ascending order"),
    ("900\n", "90 90\n", "digit_three is 0, and digit_two is 0"),
    ("505\n", "50 55\n", "digit_three > 0 and digit_two is 0"),
    ("300\n", "30 30\n", "digit_three > 0, digit_two is 0, digit_one > 0"),
    ("100\n", "10 10\n", "digit_three is 1 and others are 0"),
    ("330\n", "30 33\n", "digit_two == digit_three"),
    ("456\n", "45 65\n", "non-zero digits with ascending order"),
]


o_test_data = [
    ("31\n11\n", "321\n", "first open test"),
    ("49\n17\n", "911\n", "second open test"),
    ("12\n34\n", "451\n", "simple ascending digits"),
    ("98\n76\n", "956\n", "descending digits with no swaps needed"),
    ("99\n99\n", "989\n", "maximum digits"),
    ("10\n10\n", "110\n", "minimal non-zero digits"),
    ("43\n56\n", "693\n", "mix of digits with different maximums"),
    ("91\n19\n", "901\n", "mirrored digits"),
    ("80\n70\n", "870\n", "leading zeros in tens place"),
    ("12\n89\n", "901\n", "large difference between digits"),
    ("56\n78\n", "835\n", "high middle digits"),
    ("10\n20\n", "210\n", "zero in the units place"),
    ("23\n12\n", "341\n", "reverse sorted digits"),
    ("45\n67\n", "714\n", "close values with swapped digits"),
    ("99\n10\n", "900\n", "large and small"),
    ("74\n36\n", "703\n", "no change needed, different tens and units"),
]


p_test_data = [
    (
        "10\n5\n7\n",
        {
            "          Петя          \n"
            "      Толя  \n"
            "                      Вася\n"
            "       II      I      III   \n",
            "          Петя          \n"
            "      Толя  \n"
            "                      Вася\n"
            "       II      I      III   \n"
            "    \n",
            "          Петя          \n"
            "  Толя  \n"
            "                  Вася\n"
            "   II      I      III   \n",
            "          Петя          \n"
            "  Толя  \n"
            "                  Вася  \n"
            "   II      I      III   \n",
            "          Петя          \n"
            "      Толя  \n"
            "                      Вася  \n"
            "       II      I      III   \n",
            "          Петя          \n"
            "      Толя  \n"
            "                      Вася  \n"
            "       II      I      III   ",
        },
        "first open test",
    ),
    (
        "0.0000000003\n0.0000000002\n0.0000000001\n",  # Петя, Вася, Толя
        {
            "          Петя          \n"
            "      Вася  \n"
            "                      Толя\n"
            "       II      I      III   \n",
            "          Петя          \n"
            "      Вася  \n"
            "                      Толя\n"
            "       II      I      III   \n"
            "    \n",
            "          Петя          \n"
            "  Вася  \n"
            "                  Толя\n"
            "   II      I      III   \n",
            "          Петя          \n"
            "  Вася  \n"
            "                  Толя  \n"
            "   II      I      III   \n",
            "          Петя          \n"
            "      Вася  \n"
            "                      Толя  \n"
            "       II      I      III   \n",
            "          Петя          \n"
            "      Вася  \n"
            "                      Толя  \n"
            "       II      I      III   ",
        },
        "small floats",
    ),
    (
        "5\n7\n10\n",
        {
            "          Толя          \n"
            "  Вася  \n"
            "                  Петя\n"
            "   II      I      III   \n",
            "          Толя          \n"
            "      Вася  \n"
            "                      Петя\n"
            "       II      I      III   \n"
            "    \n",
            "          Толя          \n"
            "      Вася  \n"
            "                      Петя\n"
            "       II      I      III   \n",
            "          Толя          \n"
            "  Вася  \n"
            "                  Петя  \n"
            "   II      I      III   \n",
            "          Толя          \n"
            "      Вася  \n"
            "                      Петя  \n"
            "       II      I      III   \n",
            "          Толя          \n"
            "      Вася  \n"
            "                      Петя  \n"
            "       II      I      III   ",
        },
        "second open test",
    ),
    (
        "1000000002\n1000000001\n1000000003\n",  # Петя, Вася, Толя
        {
            "          Толя          \n"
            "  Петя  \n"
            "                  Вася\n"
            "   II      I      III   \n",
            "          Толя          \n"
            "      Петя  \n"
            "                      Вася\n"
            "       II      I      III   \n"
            "    \n",
            "          Толя          \n"
            "      Петя  \n"
            "                      Вася\n"
            "       II      I      III   \n",
            "          Толя          \n"
            "  Петя  \n"
            "                  Вася  \n"
            "   II      I      III   \n",
            "          Толя          \n"
            "      Петя  \n"
            "                      Вася  \n"
            "       II      I      III   \n",
            "          Толя          \n"
            "      Петя  \n"
            "                      Вася  \n"
            "       II      I      III   ",
        },
        "big",
    ),
    (
        "5\n10.3\n10.1\n",  # Петя, Вася, Толя
        {
            "          Вася          \n"
            "  Толя  \n"
            "                  Петя\n"
            "   II      I      III   \n",
            "          Вася          \n"
            "      Толя  \n"
            "                      Петя\n"
            "       II      I      III   \n"
            "    \n",
            "          Вася          \n"
            "      Толя  \n"
            "                      Петя\n"
            "       II      I      III   \n",
            "          Вася          \n"
            "  Толя  \n"
            "                  Петя  \n"
            "   II      I      III   \n",
            "          Вася          \n"
            "      Толя  \n"
            "                      Петя  \n"
            "       II      I      III   \n",
            "          Вася          \n"
            "      Толя  \n"
            "                      Петя  \n"
            "       II      I      III   ",
        },
        "float avrg speeds",
    ),
    (
        "10.2\n10.3\n10.1\n",  # Петя, Вася, Толя
        {
            "          Вася          \n"
            "  Петя  \n"
            "                  Толя\n"
            "   II      I      III   \n",
            "          Вася          \n"
            "      Петя  \n"
            "                      Толя\n"
            "       II      I      III   \n"
            "    \n",
            "          Вася          \n"
            "      Петя  \n"
            "                      Толя\n"
            "       II      I      III   \n",
            "          Вася          \n"
            "  Петя  \n"
            "                  Толя  \n"
            "   II      I      III   \n",
            "          Вася          \n"
            "      Петя  \n"
            "                      Толя  \n"
            "       II      I      III   \n",
            "          Вася          \n"
            "      Петя  \n"
            "                      Толя  \n"
            "       II      I      III   ",
        },
        "float avrg speeds swap 2-3",
    ),
]


q_test_data = [
    ("1\n-2\n1\n", {"1.00\n", "1.0\n"}, "first open test"),
    ("3.5\n-2.4\n-7.3\n", {"-1.14 1.83\n"}, "second open test"),
    ("0\n0\n0\n", {"Infinite solutions\n"}, "all zeros"),
    ("0\n0\n-7.3\n", {"No solution\n"}, "a == b == 0, c != 0"),
    ("-500000\n10\n-1\n", {"No solution\n"}, "big negative a"),
    ("0\n1\n1\n", {"-1.0\n", "-1.00\n"}, "a ==, b and c not 0"),
    ("5\n10\n-1\n", {"-2.1 0.1\n", "-2.10 0.10\n"}, "root2 < root1"),
    ("-5\n10\n-1\n", {"0.11 1.89\n"}, "root1 < root2"),
]


r_test_data = [
    ("3\n5\n4\n", "100%\n", "first open test"),
    ("6\n3\n4\n", "велика\n", "second open test"),
    ("6\n1\n6\n", "крайне мала\n", "third open-like test"),
    ("6.1\n6.1\n6.1\n", "крайне мала\n", "float equilateral triangle"),
    ("6.1\n6.1\n6.1\n", "крайне мала\n", "float equilateral triangle"),
    (
        "5.000000001\n5.000000001\n4.000000001\n",
        "крайне мала\n",
        "float bigger than 90 degrees",
    ),
    (
        "5\n3.000000001\n4.00000000\n",
        "крайне мала\n",
        "float smaller than 90 degrees",
    ),
    (
        "0.000000045\n0.000000075\n0.0000006\n",
        "100%\n",
        "perpendicular triangle float",
    ),
    (
        "4500000000\n7500000000\n6000000000\n",
        "100%\n",
        "perpendicular triangle big int",
    ),
    (
        "4500000000.1\n7500000000.1\n6000000000.1\n",
        "крайне мала\n",
        "almost perpendicular triangle big float",
    ),
]


s_test_data = [
    (
        "3.5\n-3.2\n",
        "Опасность! Покиньте зону как можно скорее!\n",
        "first open test",
    ),
    (
        "-5.2\n3.4\n",
        "Зона безопасна. Продолжайте работу.\n",
        "second open test",
    ),
    (
        "9.1\n4.3\n",
        "Вы вышли в море и рискуете быть съеденным акулой!\n",
        "water test I",
    ),
    (
        "6\n-8.0001\n",
        "Вы вышли в море и рискуете быть съеденным акулой!\n",
        "water test II",
    ),
    (
        "-4\n-9.201\n",
        "Вы вышли в море и рискуете быть съеденным акулой!\n",
        "water test III",
    ),
    (
        "-6\n8.00001\n",
        "Вы вышли в море и рискуете быть съеденным акулой!\n",
        "water test IV",
    ),
    (
        "0\n5\n",
        "Опасность! Покиньте зону как можно скорее!\n",
        "danger test I",
    ),
    (
        "5\n0\n",
        "Опасность! Покиньте зону как можно скорее!\n",
        "danger test II",
    ),
    (
        "-1\n-9\n",
        "Опасность! Покиньте зону как можно скорее!\n",
        "danger test III",
    ),
    (
        "-7\n0\n",
        "Опасность! Покиньте зону как можно скорее!\n",
        "danger test IV one",
    ),
    (
        "-5\n3\n",
        "Опасность! Покиньте зону как можно скорее!\n",
        "danger test IV two",
    ),
    (
        "3.8\n3.79\n",
        "Зона безопасна. Продолжайте работу.\n",
        "safe test I",
    ),
    (
        "-6.4\n-2\n",
        "Зона безопасна. Продолжайте работу.\n",
        "safe test III",
    ),
    (
        "-5\n3.5\n",
        "Зона безопасна. Продолжайте работу.\n",
        "safe test IV",
    ),
]


t_test_data = [
    (
        "березка елочка зайка волк березка\n"
        "сосна сосна сосна елочка грибочки медведь\n"
        "сосна сосна сосна белочка сосна белочка\n",
        "березка елочка зайка волк березка 33\n",
        "first open test",
    ),
    (
        "зайка березка\nберезка зайка\nберезка елочка березка\n",
        "березка зайка 13\n",
        "second open test",
    ),
    (
        "грузовик березка\nопушка березка полянка\nчерт елочка березка зайка\n",
        "черт елочка березка зайка 25\n",
        "last line",
    ),
    (
        "пес зайка\nзайка пёс\nзайка пес\n",
        "зайка пес 9\n",
        "sorting check",
    ),
    (
        "пес\nзайка\n зайка\n",
        " зайка 6\n",
        "second third line comp",
    ),
    (
        "пес\n зайка\nзайка\n",
        " зайка 6\n",
        "second third line comp s>t",
    ),
    (
        "зайка\nпес\n зайка\n",
        " зайка 6\n",
        "first third line comp f>t",
    ),
]
