a_test_data = [
    (
        "Аня\nхорошо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, Аня!\n"
        "Как дела?\n"
        "Я за вас рада!",
        "first open test",
    ),
    (
        "Боря\nплохо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, Боря!\n"
        "Как дела?\n"
        "Всё наладится!",
        "second open test",
    ),
    (
        "\nхорошо\n",
        "Как Вас зовут?\n" "Здравствуйте, !\n" "Как дела?\n" "Я за вас рада!",
        "empty name good",
    ),
    (
        "\nплохо\n",
        "Как Вас зовут?\n" "Здравствуйте, !\n" "Как дела?\n" "Всё наладится!",
        "empty name bad",
    ),
    (
        " \nхорошо\n",
        "Как Вас зовут?\n" "Здравствуйте,  !\n" "Как дела?\n" "Я за вас рада!",
        "whitespace good",
    ),
    (
        " \nплохо\n",
        "Как Вас зовут?\n" "Здравствуйте,  !\n" "Как дела?\n" "Всё наладится!",
        "whitespace bad",
    ),
    (
        "CaMeL\nхорошо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, CaMeL!\n"
        "Как дела?\n"
        "Я за вас рада!",
        "CaMeLcAsE good",
    ),
    (
        "CaMeL\nплохо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, CaMeL!\n"
        "Как дела?\n"
        "Всё наладится!",
        "CaMeLcAsE bad",
    ),
    (
        "Баба Яга\nхорошо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, Баба Яга!\n"
        "Как дела?\n"
        "Я за вас рада!",
        "double name good",
    ),
    (
        "Баба Яга\nплохо\n",
        "Как Вас зовут?\n"
        "Здравствуйте, Баба Яга!\n"
        "Как дела?\n"
        "Всё наладится!",
        "double name bad",
    ),
]


b_test_data = [
    ("10\n5\n", "Петя", "first open test"),
    ("5\n7\n", "Вася", "second open test"),
    ("0\n5\n", "Вася", "zero speed one"),
    ("10\n0\n", "Петя", "zero speed two"),
    ("4.99\n4\n", "Петя", "float speed one"),
    ("10\n10.01\n", "Вася", "float speed two"),
    ("10.02\n10.01\n", "Петя", "float first greater"),
    ("10.01\n10.02\n", "Вася", "float second greater"),
    ("10.000000002\n10.000000001\n", "Петя", "float first bit greater"),
    ("10.000000001\n10.000000002\n", "Вася", "float second bit greater"),
]


c_test_data = [
    ("10\n5\n7\n", "Петя", "first open test"),
    ("5\n7\n10\n", "Толя", "second open test"),
    ("5\n10\n7\n", "Вася", "vasya wins"),
    ("10.3\n10.2\n10.1\n", "Петя", "float petya wins"),
    ("10.1\n10.2\n10.3\n", "Толя", "float tolya wins"),
    ("10.1\n10.3\n10.2\n", "Вася", "float vasya wins"),
    (
        "0.0000000000000003\n0.0000000000000002\n0.0000000000000001\n",
        "Петя",
        "small float petya wins",
    ),
    (
        "0.0000000000000001\n0.0000000000000002\n0.0000000000000003\n",
        "Толя",
        "small float tolya wins",
    ),
    (
        "0.0000000000000001\n0.0000000000000003\n0.0000000000000002\n",
        "Вася",
        "small float vasya wins",
    ),
    (
        "0.0000000000000003\n0\n0\n",
        "Петя",
        "small float and zeros petya wins",
    ),
    (
        "0\n0\n0.0000000000000003\n",
        "Толя",
        "small float and zeros tolya wins",
    ),
    (
        "0\n0.0000000000000003\n0\n",
        "Вася",
        "small float and zeros vasya wins",
    ),
    (
        "10000000000000003\n10000000000000002\n10000000000000001\n",
        "Петя",
        "huge int petya wins",
    ),
    (
        "10000000000000001\n10000000000000002\n10000000000000003\n",
        "Толя",
        "huge int tolya wins",
    ),
    (
        "10000000000000001\n10000000000000003\n10000000000000002\n",
        "Вася",
        "huge int vasya wins",
    ),
]


d_test_data = [
    (
        "10\n5\n7\n",  # Скорости: Петя Вася Толя
        "1. Петя\n2. Толя\n3. Вася",
        "first open test",
    ),
    (
        "10\n7\n5\n",
        "1. Петя\n2. Вася\n3. Толя",
        "first open test 2-3 swap",
    ),
    (
        "5\n7\n10\n",
        "1. Толя\n2. Вася\n3. Петя",
        "second open test",
    ),
    (
        "7\n5\n10\n",
        "1. Толя\n2. Петя\n3. Вася",
        "second open test 2-3 swap",
    ),
    (
        "5\n10\n7\n",
        "1. Вася\n2. Толя\n3. Петя",
        "third open-like test",
    ),
    (
        "7\n10\n5\n",
        "1. Вася\n2. Петя\n3. Толя",
        "third open-like test 2-3 swap",
    ),
    (
        "10.3\n10.1\n10.2\n",  # Скорости: Петя Вася Толя
        "1. Петя\n2. Толя\n3. Вася",
        "float p t v",
    ),
    (
        "10.3\n10.2\n10.1\n",
        "1. Петя\n2. Вася\n3. Толя",
        "float p v t",
    ),
    (
        "10.2\n10.3\n10.1\n",
        "1. Вася\n2. Петя\n3. Толя",
        "float v p t",
    ),
    (
        "10.1\n10.3\n10.2\n",
        "1. Вася\n2. Толя\n3. Петя",
        "float v t p",
    ),
    (
        "10.1\n10.2\n10.3\n",
        "1. Толя\n2. Вася\n3. Петя",
        "float t v p",
    ),
    (
        "10.2\n10.1\n10.3\n",
        "1. Толя\n2. Петя\n3. Вася",
        "float t p v",
    ),
    (
        "0.00000000003\n0.00000000001\n0.00000000002\n",  # Скорости: Петя Вася Толя
        "1. Петя\n2. Толя\n3. Вася",
        "small float p t v",
    ),
    (
        "0.00000000003\n0.00000000002\n0.00000000001\n",
        "1. Петя\n2. Вася\n3. Толя",
        "small float p v t",
    ),
    (
        "0.00000000002\n0.00000000003\n0.00000000001\n",
        "1. Вася\n2. Петя\n3. Толя",
        "small float v p t",
    ),
    (
        "0.00000000001\n0.00000000003\n0.00000000002\n",
        "1. Вася\n2. Толя\n3. Петя",
        "small float v t p",
    ),
    (
        "0.00000000001\n0.00000000002\n0.00000000003\n",
        "1. Толя\n2. Вася\n3. Петя",
        "small float t v p",
    ),
    (
        "0.00000000002\n0.00000000001\n0.00000000003\n",
        "1. Толя\n2. Петя\n3. Вася",
        "small float t p v",
    ),
    (
        "1000000000003\n1000000000001\n1000000000002\n",  # Скорости: Петя Вася Толя
        "1. Петя\n2. Толя\n3. Вася",
        "big float p t v",
    ),
    (
        "1000000000003\n1000000000002\n1000000000001\n",
        "1. Петя\n2. Вася\n3. Толя",
        "big float p v t",
    ),
    (
        "1000000000002\n1000000000003\n1000000000001\n",
        "1. Вася\n2. Петя\n3. Толя",
        "big float v p t",
    ),
    (
        "1000000000001\n1000000000003\n1000000000002\n",
        "1. Вася\n2. Толя\n3. Петя",
        "big float v t p",
    ),
    (
        "1000000000001\n1000000000002\n1000000000003\n",
        "1. Толя\n2. Вася\n3. Петя",
        "big float t v p",
    ),
    (
        "1000000000002\n1000000000001\n1000000000003\n",
        "1. Толя\n2. Петя\n3. Вася",
        "big float t p v",
    ),
]


e_test_data = [
    ("3\n5\n", "Вася", "first open test"),
    ("10\n2\n", "Петя", "second open test"),
    ("9\n3\n", "Ровно", "equal"),
    ("0\n0\n", "Вася", "zero input"),
    ("5\n9\n", "Вася", "min diff vasya"),
    ("8\n1\n", "Петя", "min diff petya"),
    ("1000000003\n1000000005\n", "Вася", "huge first open test"),
    ("10000000010\n1000000002\n", "Петя", "huge second open test"),
    ("1000000009\n1000000003\n", "Ровно", "huge equal"),
    ("0\n9\n", "Вася", "zero to vasya"),
    ("8\n0\n", "Петя", "zero to petya petya"),
]


f_test_data = [
    ("2022\n", "NO", "first open test"),
    ("2020\n", "YES", "second open test"),
    ("1900\n", "NO", "century without leap"),
    ("2000\n", "YES", "century leap year"),
    ("2100\n", "NO", "future non-leap century"),
    ("2400\n", "YES", "future leap century"),
    ("1800\n", "NO", "old century non-leap"),
    ("1600\n", "YES", "old leap century"),
    ("2024\n", "YES", "current leap year"),
    ("2019\n", "NO", "recent non-leap year"),
    ("0004\n", "YES", "second leap year"),
    ("1\n", "NO", "the beginning"),
]


g_test_data = [
    ("1234\n", "NO", "first open test"),
    ("2332\n", "YES", "second open test"),
    ("0001\n", "NO", "starts with zeros neg"),
    ("1000\n", "NO", "ends with zeros neg"),
    ("0990\n", "YES", "starts with zeros pos"),
    ("7007\n", "YES", "middle zeros pos"),
    ("3399\n", "NO", "different halves test"),
    ("7177\n", "NO", "almost palindrome test"),
    ("4141\n", "NO", "alternating digits test"),
    ("0000\n", "YES", "all zeros pos"),
    ("0300\n", "NO", "ends with zeros neg"),
    ("1221\n", "YES", "common palindrome test"),
    ("4004\n", "YES", "mirror palindrome test"),
    ("1881\n", "YES", "eights and ones pos"),
    ("7117\n", "YES", "reversed digits pos"),
]


h_test_data = [
    ("березка елочка зайка волк березка\n", "YES", "first open test"),
    (
        "сосна сосна сосна елочка грибочки медведь\n",
        "NO",
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
        "YES",
        "long line",
    ),
    ("березка елочка волк березка зайка\n", "YES", "last word"),
    ("заика березка елочка волк березка\n", "NO", "misspelled"),
]


i_test_data = [
    ("Вова\nАня\nБоря\n", "Аня", "first open test"),
    ("Толя\nКоля\nВася\n", "Вася", "second open test"),
    ("АHна\nАнна\nАнна\n", "АHна", "identical names"),
    ("Гриша\nМиша\nДима\n", "Гриша", "names with different first letters"),
    ("Яша\nЮра\nЯна\n", "Юра", "names with similar letters"),
    ("Алекс\nАлла\nАльберт\n", "Алекс", "same first letters"),
    ("Зина\nКатя\nЖеня\n", "Женя", "middle alphabet"),
    ("Саша\nАня\nОля\n", "Аня", "mixed order"),
    ("Лена\nАня\nВаля\n", "Аня", "alphabetical"),
    ("Олег\nИгорь\nАртём\n", "Артём", "reverse order"),
]


j_test_data = [
    ("123\n", "53", "first open test"),
    ("741\n", "115", "second open test"),
    ("111\n", "22", "all ones test"),
    ("999\n", "1818", "max digits test"),
    ("321\n", "53", "decreasing digits test"),
    ("256\n", "117", "middle digit test"),
    ("804\n", "84", "zero in middle test"),
    ("500\n", "50", "leading zeros in sums test"),
    ("111\n", "22", "all digits the same test"),
    ("970\n", "167", "last digit zero test"),
    ("000\n", "00", "all zeros test"),
    ("001\n", "10", "leading zeros test"),
]


k_test_data = [
    ("123\n", "YES", "first open test"),
    ("748\n", "NO", "second open test"),
    ("321\n", "YES", "digits in descending order"),
    ("921\n", "NO", "digits in descending order not beautiful"),
    ("111\n", "YES", "same digits"),
    ("555\n", "YES", "same digits middle condition still holds"),
    ("532\n", "NO", "highest digit first, not beautiful"),
    ("100\n", "NO", "edge case with small values and not beautiful"),
]


l_test_data = [
    ("3\n3\n3\n", "YES", "first open test"),
    ("1\n2\n3\n", "NO", "second open test"),
    ("5\n5\n5\n", "YES", "equilateral triangle"),
    ("2\n2\n3\n", "YES", "isosceles triangle"),
    ("2\n3\n4\n", "YES", "scalene triangle"),
    ("1\n1\n2\n", "NO", "not a triangle, sum equals third side"),
    ("10\n1\n1\n", "NO", "not a triangle, one side much larger"),
    ("0\n0\n0\n", "NO", "zero sides, invalid triangle"),
    ("5\n10\n15\n", "NO", "degenerate case, sum equals third side"),
    ("1000000\n1000000\n1000000\n", "YES", "large equilateral triangle"),
]


m_test_data = [
    ("12\n13\n14\n", "1", "first open test"),
    ("23\n13\n63\n", "3", "second open test"),
    ("21\n22\n23\n", "2", "all first digits same"),
    ("41\n43\n49\n", "4", "all first digits same, different middle digits"),
    ("10\n20\n30\n", "0", "increasing first digits"),
    ("59\n49\n39\n", "9", "decreasing first digits"),
    ("77\n72\n77\n", "7", "two equal one bigger"),
    ("88\n78\n88\n", "8", "two equal one smaller"),
]


n_test_data = [
    ("103\n", "10 31", "first open test"),
    ("787\n", "77 87", "second open test"),
    ("567\n", "56 76", "digits in descending order"),
    ("123\n", "12 32", "digits in ascending order"),
    ("900\n", "90 90", "digit_three is 0, and digit_two is 0"),
    ("505\n", "50 55", "digit_three > 0 and digit_two is 0"),
    ("300\n", "30 30", "digit_three > 0, digit_two is 0, digit_one > 0"),
    ("100\n", "10 10", "digit_three is 1 and others are 0"),
    ("330\n", "30 33", "digit_two == digit_three"),
    ("456\n", "45 65", "non-zero digits with ascending order"),
]


o_test_data = [
    ("31\n11\n", "321", "first open test"),
    ("49\n17\n", "911", "second open test"),
    ("12\n34\n", "451", "simple ascending digits"),
    ("98\n76\n", "956", "descending digits with no swaps needed"),
    ("99\n99\n", "989", "maximum digits"),
    ("10\n10\n", "110", "minimal non-zero digits"),
    ("43\n56\n", "693", "mix of digits with different maximums"),
    ("91\n19\n", "901", "mirrored digits"),
    ("80\n70\n", "870", "leading zeros in tens place"),
    ("12\n89\n", "901", "large difference between digits"),
    ("56\n78\n", "835", "high middle digits"),
    ("10\n20\n", "210", "zero in the units place"),
    ("23\n12\n", "341", "reverse sorted digits"),
    ("45\n67\n", "714", "close values with swapped digits"),
    ("99\n10\n", "900", "large and small"),
    ("74\n36\n", "703", "no change needed, different tens and units"),
]


p_test_data = [
    (
        "10\n5\n7\n",
        "          Петя          \n"
        "  Толя  \n"
        "                  Вася\n"
        "   II      I      III",
        "first open test",
    ),
    (
        "0.0000000003\n0.0000000002\n0.0000000001\n",  # Петя, Вася, Толя
        "          Петя          \n"
        "  Вася  \n"
        "                  Толя\n"
        "   II      I      III",
        "small floats",
    ),
    (
        "5\n7\n10\n",
        "          Толя          \n"
        "  Вася  \n"
        "                  Петя\n"
        "   II      I      III",
        "second open test",
    ),
    (
        "1000000002\n1000000001\n1000000003\n",  # Петя, Вася, Толя
        "          Толя          \n"
        "  Петя  \n"
        "                  Вася\n"
        "   II      I      III",
        "big",
    ),
    (
        "5\n10.3\n10.1\n",  # Петя, Вася, Толя
        "          Вася          \n"
        "  Толя  \n"
        "                  Петя\n"
        "   II      I      III",
        "float avrg speeds",
    ),
    (
        "10.2\n10.3\n10.1\n",  # Петя, Вася, Толя
        "          Вася          \n"
        "  Петя  \n"
        "                  Толя\n"
        "   II      I      III",
        "float avrg speeds swap 2-3",
    ),
]


q_test_data = [
    ("1\n-2\n1\n", "1.0", "first open test"),
    ("3.5\n-2.4\n-7.3\n", "-1.14 1.83", "second open test"),
    ("0\n0\n0\n", "Infinite solutions", "all zeros"),
    ("0\n0\n-7.3\n", "No solution", "a == b == 0, c != 0"),
    ("-500000\n10\n-1\n", "No solution", "big negative a"),
    ("0\n1\n1\n", "-1.0", "a ==, b and c not 0"),
    ("5\n10\n-1\n", "-2.1 0.1", "root2 < root1"),
    ("-5\n10\n-1\n", "0.11 1.89", "root1 < root2"),
]


r_test_data = [
    ("3\n5\n4\n", "100%", "first open test"),
    ("6\n3\n4\n", "велика", "second open test"),
    ("6\n1\n6\n", "крайне мала", "third open-like test"),
    ("6.1\n6.1\n6.1\n", "крайне мала", "float equilateral triangle"),
    ("6.1\n6.1\n6.1\n", "крайне мала", "float equilateral triangle"),
    (
        "5.000000001\n5.000000001\n4.000000001\n",
        "крайне мала",
        "float bigger than 90 degrees",
    ),
    (
        "5\n3.000000001\n4.00000000\n",
        "крайне мала",
        "float smaller than 90 degrees",
    ),
    (
        "0.000000045\n0.000000075\n0.00000006\n",
        "100%",
        "perpendicular triangle float",
    ),
    (
        "4500000000\n7500000000\n6000000000\n",
        "100%",
        "perpendicular triangle big int",
    ),
    (
        "4500000000.1\n7500000000.1\n6000000000.1\n",
        "крайне мала",
        "almost perpendicular triangle big float",
    ),
]


s_test_data = [
    (
        "3.5\n-3.2\n",
        "Опасность! Покиньте зону как можно скорее!",
        "first open test",
    ),
    (
        "-5.2\n3.4\n",
        "Зона безопасна. Продолжайте работу.",
        "second open test",
    ),
    (
        "9.1\n4.3\n",
        "Вы вышли в море и рискуете быть съеденным акулой!",
        "water test I",
    ),
    (
        "6\n-8.0001\n",
        "Вы вышли в море и рискуете быть съеденным акулой!",
        "water test II",
    ),
    (
        "-4\n-9.201\n",
        "Вы вышли в море и рискуете быть съеденным акулой!",
        "water test III",
    ),
    (
        "-6\n8.00001\n",
        "Вы вышли в море и рискуете быть съеденным акулой!",
        "water test IV",
    ),
    (
        "0\n5\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test I",
    ),
    (
        "5\n0\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test II",
    ),
    (
        "-1\n-9\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test III",
    ),
    (
        "-7\n0\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test IV one",
    ),
    (
        "-5\n3\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test IV two",
    ),
    (
        "3.8\n3.79\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test I",
    ),
    (
        "-6.4\n-2\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test III",
    ),
    (
        "-5\n3.5\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test IV",
    ),
    (
        "-4.1\n5.02\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test II",
    ),
    (
        "-3.95\n4.95\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test II",
    ),
    (
        "-5.95\n2.01\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test II",
    ),
    (
        "-5.8\n2\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test II",
    ),
    (
        "-1.95\n4.95\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test II",
    ),
    (
        "-1.95\n5.01\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test II",
    ),
    (
        "3.01\n4.01\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test I",
    ),
    (
        "2.99\n3.99\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test I",
    ),
    (
        "5.01\n0\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test I",
    ),
    (
        "4.99\n0\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test I",
    ),
    (
        "3.82\n-3.21\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test IV",
    ),
    (
        "3.79\n-3.2\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test IV",
    ),
    (
        "0.6\n-8.4\n",
        "Зона безопасна. Продолжайте работу.",
        "safe test IV",
    ),
    (
        "0.6\n-8.35\n",
        "Опасность! Покиньте зону как можно скорее!",
        "danger test IV",
    ),
]


t_test_data = [
    (
        "березка елочка зайка волк березка\n"
        "сосна сосна сосна елочка грибочки медведь\n"
        "сосна сосна сосна белочка сосна белочка\n",
        "березка елочка зайка волк березка 33",
        "first open test",
    ),
    (
        "зайка березка\nберезка зайка\nберезка елочка березка\n",
        "березка зайка 13",
        "second open test",
    ),
    (
        "грузовик березка\nопушка березка полянка\nчерт елочка березка зайка\n",
        "черт елочка березка зайка 25",
        "last line",
    ),
    (
        "пес зайка\nзайка пёс\nзайка пес\n",
        "зайка пес 9",
        "sorting check",
    ),
    (
        "пес\nзайка\n зайка\n",
        " зайка 6",
        "second third line comp",
    ),
    (
        "пес\n зайка\nзайка\n",
        " зайка 6",
        "second third line comp s>t",
    ),
    (
        "зайка\nпес\n зайка\n",
        " зайка 6",
        "first third line comp f>t",
    ),
]
