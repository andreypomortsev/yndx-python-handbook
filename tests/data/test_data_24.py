a_test_data = [
    ("3\n", "1 2 3\n2 4 6\n3 6 9\n", "first open test"),
    (
        "5\n",
        "1 2 3 4 5\n"
        "2 4 6 8 10\n"
        "3 6 9 12 15\n"
        "4 8 12 16 20\n"
        "5 10 15 20 25\n",
        "second open test",
    ),
]


b_test_data = [
    (
        "3\n",
        "1 * 1 = 1\n"
        "2 * 1 = 2\n"
        "3 * 1 = 3\n"
        "1 * 2 = 2\n"
        "2 * 2 = 4\n"
        "3 * 2 = 6\n"
        "1 * 3 = 3\n"
        "2 * 3 = 6\n"
        "3 * 3 = 9\n",
        "first open test",
    ),
    (
        "5\n",
        "1 * 1 = 1\n"
        "2 * 1 = 2\n"
        "3 * 1 = 3\n"
        "4 * 1 = 4\n"
        "5 * 1 = 5\n"
        "1 * 2 = 2\n"
        "2 * 2 = 4\n"
        "3 * 2 = 6\n"
        "4 * 2 = 8\n"
        "5 * 2 = 10\n"
        "1 * 3 = 3\n"
        "2 * 3 = 6\n"
        "3 * 3 = 9\n"
        "4 * 3 = 12\n"
        "5 * 3 = 15\n"
        "1 * 4 = 4\n"
        "2 * 4 = 8\n"
        "3 * 4 = 12\n"
        "4 * 4 = 16\n"
        "5 * 4 = 20\n"
        "1 * 5 = 5\n"
        "2 * 5 = 10\n"
        "3 * 5 = 15\n"
        "4 * 5 = 20\n"
        "5 * 5 = 25\n",
        "second open test",
    ),
    ("1\n", "1 * 1 = 1\n", "min size"),
    (
        "10\n",
        "1 * 1 = 1\n"
        "2 * 1 = 2\n"
        "3 * 1 = 3\n"
        "4 * 1 = 4\n"
        "5 * 1 = 5\n"
        "6 * 1 = 6\n"
        "7 * 1 = 7\n"
        "8 * 1 = 8\n"
        "9 * 1 = 9\n"
        "10 * 1 = 10\n"
        "1 * 2 = 2\n"
        "2 * 2 = 4\n"
        "3 * 2 = 6\n"
        "4 * 2 = 8\n"
        "5 * 2 = 10\n"
        "6 * 2 = 12\n"
        "7 * 2 = 14\n"
        "8 * 2 = 16\n"
        "9 * 2 = 18\n"
        "10 * 2 = 20\n"
        "1 * 3 = 3\n"
        "2 * 3 = 6\n"
        "3 * 3 = 9\n"
        "4 * 3 = 12\n"
        "5 * 3 = 15\n"
        "6 * 3 = 18\n"
        "7 * 3 = 21\n"
        "8 * 3 = 24\n"
        "9 * 3 = 27\n"
        "10 * 3 = 30\n"
        "1 * 4 = 4\n"
        "2 * 4 = 8\n"
        "3 * 4 = 12\n"
        "4 * 4 = 16\n"
        "5 * 4 = 20\n"
        "6 * 4 = 24\n"
        "7 * 4 = 28\n"
        "8 * 4 = 32\n"
        "9 * 4 = 36\n"
        "10 * 4 = 40\n"
        "1 * 5 = 5\n"
        "2 * 5 = 10\n"
        "3 * 5 = 15\n"
        "4 * 5 = 20\n"
        "5 * 5 = 25\n"
        "6 * 5 = 30\n"
        "7 * 5 = 35\n"
        "8 * 5 = 40\n"
        "9 * 5 = 45\n"
        "10 * 5 = 50\n"
        "1 * 6 = 6\n"
        "2 * 6 = 12\n"
        "3 * 6 = 18\n"
        "4 * 6 = 24\n"
        "5 * 6 = 30\n"
        "6 * 6 = 36\n"
        "7 * 6 = 42\n"
        "8 * 6 = 48\n"
        "9 * 6 = 54\n"
        "10 * 6 = 60\n"
        "1 * 7 = 7\n"
        "2 * 7 = 14\n"
        "3 * 7 = 21\n"
        "4 * 7 = 28\n"
        "5 * 7 = 35\n"
        "6 * 7 = 42\n"
        "7 * 7 = 49\n"
        "8 * 7 = 56\n"
        "9 * 7 = 63\n"
        "10 * 7 = 70\n"
        "1 * 8 = 8\n"
        "2 * 8 = 16\n"
        "3 * 8 = 24\n"
        "4 * 8 = 32\n"
        "5 * 8 = 40\n"
        "6 * 8 = 48\n"
        "7 * 8 = 56\n"
        "8 * 8 = 64\n"
        "9 * 8 = 72\n"
        "10 * 8 = 80\n"
        "1 * 9 = 9\n"
        "2 * 9 = 18\n"
        "3 * 9 = 27\n"
        "4 * 9 = 36\n"
        "5 * 9 = 45\n"
        "6 * 9 = 54\n"
        "7 * 9 = 63\n"
        "8 * 9 = 72\n"
        "9 * 9 = 81\n"
        "10 * 9 = 90\n"
        "1 * 10 = 10\n"
        "2 * 10 = 20\n"
        "3 * 10 = 30\n"
        "4 * 10 = 40\n"
        "5 * 10 = 50\n"
        "6 * 10 = 60\n"
        "7 * 10 = 70\n"
        "8 * 10 = 80\n"
        "9 * 10 = 90\n"
        "10 * 10 = 100\n",
        "big ten",
    ),
]


c_test_data = [
    (
        "14\n",
        "1\n2 3\n4 5 6\n7 8 9 10\n11 12 13 14 ",
        "first open test",
    ),
    ("6\n", "1\n2 3\n4 5 6\n", "second open test"),
    (
        "92\n",
        "1\n"
        "2 3\n"
        "4 5 6\n"
        "7 8 9 10\n"
        "11 12 13 14 15\n"
        "16 17 18 19 20 21\n"
        "22 23 24 25 26 27 28\n"
        "29 30 31 32 33 34 35 36\n"
        "37 38 39 40 41 42 43 44 45\n"
        "46 47 48 49 50 51 52 53 54 55\n"
        "56 57 58 59 60 61 62 63 64 65 66\n"
        "67 68 69 70 71 72 73 74 75 76 77 78\n"
        "79 80 81 82 83 84 85 86 87 88 89 90 91\n"
        "92 ",
        "big tree with a trunk",
    ),
    (
        "78\n",
        "1\n"
        "2 3\n"
        "4 5 6\n"
        "7 8 9 10\n"
        "11 12 13 14 15\n"
        "16 17 18 19 20 21\n"
        "22 23 24 25 26 27 28\n"
        "29 30 31 32 33 34 35 36\n"
        "37 38 39 40 41 42 43 44 45\n"
        "46 47 48 49 50 51 52 53 54 55\n"
        "56 57 58 59 60 61 62 63 64 65 66\n"
        "67 68 69 70 71 72 73 74 75 76 77 78\n",
        "big tree without a trunk",
    ),
    ("3\n", "1\n2 3\n", "small tree without a trunk"),
    ("4\n", "1\n2 3\n4 ", "small tree with a trunk"),
]


d_test_data = [
    ("5\n1\n2\n3\n4\n5\n", "15\n", "first open test"),
    ("3\n123\n654\n789\n", "45\n", "second open test"),
    ("1\n100897089807687967800780678023\n", "149\n", "looong int one line"),
    (
        "1\n100000000000000000000000000001\n",
        "2\n",
        "looong int one line small sum",
    ),
    (
        "9\n0\n100000000000\n0\n2\n0\n0\n1\n10\n442\n",
        "15\n",
        "nine lines with zeros",
    ),
]


e_test_data = [
    (
        "3\n"
        "березка\n"
        "елочка\n"
        "зайка\n"
        "волк\n"
        "березка\n"
        "ВСЁ\n"
        "сосна\n"
        "сосна\n"
        "сосна\n"
        "елочка\n"
        "грибочки\n"
        "медведь\n"
        "ВСЁ\n"
        "сосна\n"
        "сосна\n"
        "сосна\n"
        "белочка\n"
        "сосна\n"
        "белочка\n"
        "ВСЁ\n",
        "1\n",
        "first open test",
    ),
    (
        "4\n"
        "зайка\n"
        "березка\n"
        "ВСЁ\n"
        "зайка\n"
        "зайка\n"
        "ВСЁ\n"
        "березка\n"
        "елочка\n"
        "березка\n"
        "ВСЁ\n"
        "елочка\n"
        "елочка\n"
        "елочка\n"
        "ВСЁ\n",
        "2\n",
        "second open test",
    ),
    (
        "9\n"
        "ВСЁ\n"
        "ВСЁ\n"
        "ВСЁ\n"
        "ВСЁ\n"
        "ВСЁ\n"
        "зайка\n"
        "березка\n"
        "ВСЁ\n"
        "зайка\n"
        "зайка\n"
        "ВСЁ\n"
        "березка\n"
        "елочка\n"
        "березка\n"
        "ВСЁ\n"
        "елочка\n"
        "елочка\n"
        "елочка\n"
        "ВСЁ\n",
        "2\n",
        "empty zones",
    ),
]


f_test_data = [
    ("2\n12\n42\n", "6\n", "first open test"),
    ("3\n102\n39\n768\n", "3\n", "second open test"),
    ("2\n12\n42\n0\n", "6\n", "ends with zero"),
    ("3\n102\n0\n39\n768\n", "3\n", "zero in the middle"),
    ("2\n0\n39\n", "39\n", "two elements one zero"),
    ("2\n13\n0\n", "13\n", "two elements another zero"),
    ("2\n12\n8\n", "4\n", "simple case with two numbers"),
    ("3\n15\n15\n15\n", "15\n", "all numbers are the same"),
    ("2\n13\n7\n", "1\n", "coprime numbers"),
    ("4\n24\n36\n60\n12\n", "12\n", "multiple numbers with a common divisor"),
    ("1\n42\n", "42\n", "one number"),
    ("3\n1000000000\n500000000\n250000000\n", "250000000\n", "large numbers"),
    ("2\n0\n25\n", "25\n", "zero and a positive number"),
    ("3\n0\n15\n10\n", "5\n", "zero and multiple numbers"),
    ("3\n-12\n-8\n-4\n", "4\n", "negative numbers"),
    ("3\n-8\n4\n-2\n", "2\n", "combination of positive and negative numbers"),
]


g_test_data = [
    (
        "3\n",
        "До старта 3 секунд(ы)\n"
        "До старта 2 секунд(ы)\n"
        "До старта 1 секунд(ы)\n"
        "Старт 1!!!\n"
        "До старта 4 секунд(ы)\n"
        "До старта 3 секунд(ы)\n"
        "До старта 2 секунд(ы)\n"
        "До старта 1 секунд(ы)\n"
        "Старт 2!!!\n"
        "До старта 5 секунд(ы)\n"
        "До старта 4 секунд(ы)\n"
        "До старта 3 секунд(ы)\n"
        "До старта 2 секунд(ы)\n"
        "До старта 1 секунд(ы)\n"
        "Старт 3!!!\n",
        "first open test",
    ),
    (
        "4\n",
        "До старта 3 секунд(ы)\n"
        "До старта 2 секунд(ы)\n"
        "До старта 1 секунд(ы)\n"
        "Старт 1!!!\n"
        "До старта 4 секунд(ы)\n"
        "До старта 3 секунд(ы)\n"
        "До старта 2 секунд(ы)\n"
        "До старта 1 секунд(ы)\n"
        "Старт 2!!!\n"
        "До старта 5 секунд(ы)\n"
        "До старта 4 секунд(ы)\n"
        "До старта 3 секунд(ы)\n"
        "До старта 2 секунд(ы)\n"
        "До старта 1 секунд(ы)\n"
        "Старт 3!!!\n"
        "До старта 6 секунд(ы)\n"
        "До старта 5 секунд(ы)\n"
        "До старта 4 секунд(ы)\n"
        "До старта 3 секунд(ы)\n"
        "До старта 2 секунд(ы)\n"
        "До старта 1 секунд(ы)\n"
        "Старт 4!!!\n",
        "second open test",
    ),
    (
        "1\n",
        "До старта 3 секунд(ы)\n"
        "До старта 2 секунд(ы)\n"
        "До старта 1 секунд(ы)\n"
        "Старт 1!!!\n",
        "one start",
    ),
]


h_test_data = [
    ("2\nАня\n123\nБоря\n234\n", "Боря\n", "first open test"),
    ("3\nАня\n1234\nБоря\n234\nВаня\n2323\n", "Ваня\n", "second open test"),
    ("3\nАня\n2323\nБоря\n234\nВаня\n2323\n", "Ваня\n", "tiebreak"),
    ("3\nВаня\n2323\nБоря\n234\nАня\n2323\n", "Аня\n", "tiebreak swap"),
    ("1\nВаня\n13\n", "Ваня\n", "lonely child"),
]


i_test_data = [
    ("2\n123\n234\n", {"34\n", "34"}, "first open test"),
    ("3\n1234\n7234\n2323\n", {"473\n", "473"}, "second open test"),
    ("1\n987654321", {"9\n", "9"}, "lonely child decreasing"),
    ("1\n123456789", {"9\n", "9"}, "lonely child increasing"),
    ("1\n1\n", {"1\n", "1"}, "lonely child with one"),
    (
        "5\n1234\n7234\n2323\n1234\n7234\n",
        {"47347\n", "47347"},
        "more children",
    ),
    (
        "6\n100\n1234\n7234\n2323\n1234\n7234\n",
        {"147347\n", "147347"},
        "more children and one hundred",
    ),
    (
        "9\n11\n22\n33\n44\n55\n66\n77\n88\n99\n",
        {"123456789\n", "123456789"},
        "9 lines increasing",
    ),
    (
        "9\n99\n88\n77\n66\n55\n44\n33\n22\n11\n",
        {"987654321\n", "987654321"},
        "9 lines decreasing",
    ),
]


j_test_data = [
    ("3\n", "А Б В\n1 1 1\n", "first open test"),
    (
        "5\n",
        "А Б В\n1 1 3\n1 2 2\n1 3 1\n2 1 2\n2 2 1\n3 1 1\n",
        "second open test",
    ),
    (
        "10\n",
        "А Б В\n"
        "1 1 8\n"
        "1 2 7\n"
        "1 3 6\n"
        "1 4 5\n"
        "1 5 4\n"
        "1 6 3\n"
        "1 7 2\n"
        "1 8 1\n"
        "2 1 7\n"
        "2 2 6\n"
        "2 3 5\n"
        "2 4 4\n"
        "2 5 3\n"
        "2 6 2\n"
        "2 7 1\n"
        "3 1 6\n"
        "3 2 5\n"
        "3 3 4\n"
        "3 4 3\n"
        "3 5 2\n"
        "3 6 1\n"
        "4 1 5\n"
        "4 2 4\n"
        "4 3 3\n"
        "4 4 2\n"
        "4 5 1\n"
        "5 1 4\n"
        "5 2 3\n"
        "5 3 2\n"
        "5 4 1\n"
        "6 1 3\n"
        "6 2 2\n"
        "6 3 1\n"
        "7 1 2\n"
        "7 2 1\n"
        "8 1 1\n",
        "many options 10",
    ),
]


k_test_data = [
    ("5\n1\n2\n3\n4\n5\n", "3\n", "first open test"),
    ("6\n11\n13\n15\n63\n71\n51\n", "3\n", "second open test"),
    ("1\n1\n", "0\n", "one line no prime"),
    ("1\n2\n", "1\n", "one line small prime"),
    ("1\n7901421841\n", "1\n", "one line large prime"),
    ("2\n1\n4\n", "0\n", "two lines no primes"),
    ("2\n2\n3\n", "2\n", "two lines two primes"),
    ("2\n1\n7\n", "1\n", "two lines one prime"),
    ("0\n", "0\n", "no lines - no primes"),
]


l_test_data = [
    ("2\n3\n", "1 2 3\n4 5 6\n", "first open test"),
    (
        "4\n6\n",
        " 1  2  3  4  5  6\n"
        " 7  8  9 10 11 12\n"
        "13 14 15 16 17 18\n"
        "19 20 21 22 23 24\n",
        "second open test",
    ),
    ("1\n10\n", " 1  2  3  4  5  6  7  8  9 10\n", "one long line"),
    (
        "10\n1\n",
        " 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n10\n",
        "one long column",
    ),
    (
        "10\n2\n",
        " 1  2\n"
        " 3  4\n"
        " 5  6\n"
        " 7  8\n"
        " 9 10\n"
        "11 12\n"
        "13 14\n"
        "15 16\n"
        "17 18\n"
        "19 20\n",
        "two long columns",
    ),
    (
        "2\n10\n",
        " 1  2  3  4  5  6  7  8  9 10\n11 12 13 14 15 16 17 18 19 20\n",
        "two long lines",
    ),
    ("1\n1\n", "1\n", "small rectangle"),
    (
        "11\n13\n",
        "  1   2   3   4   5   6   7   8   9  10  11  12  13\n"
        " 14  15  16  17  18  19  20  21  22  23  24  25  26\n"
        " 27  28  29  30  31  32  33  34  35  36  37  38  39\n"
        " 40  41  42  43  44  45  46  47  48  49  50  51  52\n"
        " 53  54  55  56  57  58  59  60  61  62  63  64  65\n"
        " 66  67  68  69  70  71  72  73  74  75  76  77  78\n"
        " 79  80  81  82  83  84  85  86  87  88  89  90  91\n"
        " 92  93  94  95  96  97  98  99 100 101 102 103 104\n"
        "105 106 107 108 109 110 111 112 113 114 115 116 117\n"
        "118 119 120 121 122 123 124 125 126 127 128 129 130\n"
        "131 132 133 134 135 136 137 138 139 140 141 142 143\n",
        "big rectangle",
    ),
]


m_test_data = [
    ("2\n3\n", "1 3 5\n2 4 6\n", "first open test"),
    (
        "4\n6\n",
        " 1  5  9 13 17 21\n"
        " 2  6 10 14 18 22\n"
        " 3  7 11 15 19 23\n"
        " 4  8 12 16 20 24\n",
        "second open test",
    ),
    ("1\n1\n", "1\n", "small rectangle"),
    ("1\n10\n", " 1  2  3  4  5  6  7  8  9 10\n", "one long line"),
    (
        "10\n1\n",
        " 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n10\n",
        "one long column",
    ),
    (
        "10\n10\n",
        "  1  11  21  31  41  51  61  71  81  91\n"
        "  2  12  22  32  42  52  62  72  82  92\n"
        "  3  13  23  33  43  53  63  73  83  93\n"
        "  4  14  24  34  44  54  64  74  84  94\n"
        "  5  15  25  35  45  55  65  75  85  95\n"
        "  6  16  26  36  46  56  66  76  86  96\n"
        "  7  17  27  37  47  57  67  77  87  97\n"
        "  8  18  28  38  48  58  68  78  88  98\n"
        "  9  19  29  39  49  59  69  79  89  99\n"
        " 10  20  30  40  50  60  70  80  90 100\n",
        "big rectangle",
    ),
]


n_test_data = [
    ("2\n3\n", "1 2 3\n6 5 4\n", "first open test"),
    (
        "4\n6\n",
        " 1  2  3  4  5  6\n"
        "12 11 10  9  8  7\n"
        "13 14 15 16 17 18\n"
        "24 23 22 21 20 19\n",
        "second open test",
    ),
    ("1\n1\n", "1\n", "small snake"),
    ("1\n10\n", " 1  2  3  4  5  6  7  8  9 10\n", "one long line"),
    (
        "10\n1\n",
        " 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n10\n",
        "one long column",
    ),
    (
        "10\n3\n",
        " 1  2  3\n"
        " 6  5  4\n"
        " 7  8  9\n"
        "12 11 10\n"
        "13 14 15\n"
        "18 17 16\n"
        "19 20 21\n"
        "24 23 22\n"
        "25 26 27\n"
        "30 29 28\n",
        "ten on three",
    ),
    (
        "10\n10\n",
        "  1   2   3   4   5   6   7   8   9  10\n"
        " 20  19  18  17  16  15  14  13  12  11\n"
        " 21  22  23  24  25  26  27  28  29  30\n"
        " 40  39  38  37  36  35  34  33  32  31\n"
        " 41  42  43  44  45  46  47  48  49  50\n"
        " 60  59  58  57  56  55  54  53  52  51\n"
        " 61  62  63  64  65  66  67  68  69  70\n"
        " 80  79  78  77  76  75  74  73  72  71\n"
        " 81  82  83  84  85  86  87  88  89  90\n"
        "100  99  98  97  96  95  94  93  92  91\n",
        "10 x 10",
    ),
]


o_test_data = [
    ("2\n3\n", "1 4 5\n2 3 6\n", "first open test"),
    (
        "4\n6\n",
        " 1  8  9 16 17 24\n"
        " 2  7 10 15 18 23\n"
        " 3  6 11 14 19 22\n"
        " 4  5 12 13 20 21\n",
        "second open test",
    ),
    ("1\n1\n", "1\n", "small snake"),
    ("1\n10\n", " 1  2  3  4  5  6  7  8  9 10\n", "one long line"),
    (
        "10\n1\n",
        " 1\n 2\n 3\n 4\n 5\n 6\n 7\n 8\n 9\n10\n",
        "one long column",
    ),
    (
        "10\n10\n",
        "  1  20  21  40  41  60  61  80  81 100\n"
        "  2  19  22  39  42  59  62  79  82  99\n"
        "  3  18  23  38  43  58  63  78  83  98\n"
        "  4  17  24  37  44  57  64  77  84  97\n"
        "  5  16  25  36  45  56  65  76  85  96\n"
        "  6  15  26  35  46  55  66  75  86  95\n"
        "  7  14  27  34  47  54  67  74  87  94\n"
        "  8  13  28  33  48  53  68  73  88  93\n"
        "  9  12  29  32  49  52  69  72  89  92\n"
        " 10  11  30  31  50  51  70  71  90  91\n",
        "10 x 10",
    ),
    (
        "3\n34\n",
        "  1   6   7  12  13  18  19  24  25  30  31  36  37  42  43  48  49"
        "  54  55  60  61  66  67  72  73  78  79  84  85  90  91  96  97 102\n"
        "  2   5   8  11  14  17  20  23  26  29  32  35  38  41  44  47  50"
        "  53  56  59  62  65  68  71  74  77  80  83  86  89  92  95  98 101\n"
        "  3   4   9  10  15  16  21  22  27  28  33  34  39  40  45  46  51"
        "  52  57  58  63  64  69  70  75  76  81  82  87  88  93  94  99 100\n",
        "long rows",
    ),
    (
        "26\n4\n",
        "  1  52  53 104\n"
        "  2  51  54 103\n"
        "  3  50  55 102\n"
        "  4  49  56 101\n"
        "  5  48  57 100\n"
        "  6  47  58  99\n"
        "  7  46  59  98\n"
        "  8  45  60  97\n"
        "  9  44  61  96\n"
        " 10  43  62  95\n"
        " 11  42  63  94\n"
        " 12  41  64  93\n"
        " 13  40  65  92\n"
        " 14  39  66  91\n"
        " 15  38  67  90\n"
        " 16  37  68  89\n"
        " 17  36  69  88\n"
        " 18  35  70  87\n"
        " 19  34  71  86\n"
        " 20  33  72  85\n"
        " 21  32  73  84\n"
        " 22  31  74  83\n"
        " 23  30  75  82\n"
        " 24  29  76  81\n"
        " 25  28  77  80\n"
        " 26  27  78  79\n",
        "tall columns",
    ),
]


p_test_data = [
    (
        "3\n3\n",
        {
            " 1 | 2 | 3 \n"
            "-----------\n"
            " 2 | 4 | 6 \n"
            "-----------\n"
            " 3 | 6 | 9 ",
            " 1 | 2 | 3 \n"
            "-----------\n"
            " 2 | 4 | 6 \n"
            "-----------\n"
            " 3 | 6 | 9 \n",
        },
        "first open test",
    ),
    (
        "5\n5\n",
        {
            "  1  |  2  |  3  |  4  |  5  \n"
            "-----------------------------\n"
            "  2  |  4  |  6  |  8  | 10  \n"
            "-----------------------------\n"
            "  3  |  6  |  9  | 12  | 15  \n"
            "-----------------------------\n"
            "  4  |  8  | 12  | 16  | 20  \n"
            "-----------------------------\n"
            "  5  | 10  | 15  | 20  | 25  ",
            "  1  |  2  |  3  |  4  |  5  \n"
            "-----------------------------\n"
            "  2  |  4  |  6  |  8  | 10  \n"
            "-----------------------------\n"
            "  3  |  6  |  9  | 12  | 15  \n"
            "-----------------------------\n"
            "  4  |  8  | 12  | 16  | 20  \n"
            "-----------------------------\n"
            "  5  | 10  | 15  | 20  | 25  \n",
        },
        "second open test",
    ),
    (
        "4\n7\n",
        {
            "   1   |   2   |   3   |   4   \n"
            "-------------------------------\n"
            "   2   |   4   |   6   |   8   \n"
            "-------------------------------\n"
            "   3   |   6   |   9   |  12   \n"
            "-------------------------------\n"
            "   4   |   8   |  12   |  16   ",
            "   1   |   2   |   3   |   4   \n"
            "-------------------------------\n"
            "   2   |   4   |   6   |   8   \n"
            "-------------------------------\n"
            "   3   |   6   |   9   |  12   \n"
            "-------------------------------\n"
            "   4   |   8   |  12   |  16   \n",
        },
        "not a square",
    ),
    (
        "10\n3\n",
        {
            " 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 \n"
            "---------------------------------------\n"
            " 2 | 4 | 6 | 8 |10 |12 |14 |16 |18 |20 \n"
            "---------------------------------------\n"
            " 3 | 6 | 9 |12 |15 |18 |21 |24 |27 |30 \n"
            "---------------------------------------\n"
            " 4 | 8 |12 |16 |20 |24 |28 |32 |36 |40 \n"
            "---------------------------------------\n"
            " 5 |10 |15 |20 |25 |30 |35 |40 |45 |50 \n"
            "---------------------------------------\n"
            " 6 |12 |18 |24 |30 |36 |42 |48 |54 |60 \n"
            "---------------------------------------\n"
            " 7 |14 |21 |28 |35 |42 |49 |56 |63 |70 \n"
            "---------------------------------------\n"
            " 8 |16 |24 |32 |40 |48 |56 |64 |72 |80 \n"
            "---------------------------------------\n"
            " 9 |18 |27 |36 |45 |54 |63 |72 |81 |90 \n"
            "---------------------------------------\n"
            "10 |20 |30 |40 |50 |60 |70 |80 |90 |100",
            " 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 \n"
            "---------------------------------------\n"
            " 2 | 4 | 6 | 8 |10 |12 |14 |16 |18 |20 \n"
            "---------------------------------------\n"
            " 3 | 6 | 9 |12 |15 |18 |21 |24 |27 |30 \n"
            "---------------------------------------\n"
            " 4 | 8 |12 |16 |20 |24 |28 |32 |36 |40 \n"
            "---------------------------------------\n"
            " 5 |10 |15 |20 |25 |30 |35 |40 |45 |50 \n"
            "---------------------------------------\n"
            " 6 |12 |18 |24 |30 |36 |42 |48 |54 |60 \n"
            "---------------------------------------\n"
            " 7 |14 |21 |28 |35 |42 |49 |56 |63 |70 \n"
            "---------------------------------------\n"
            " 8 |16 |24 |32 |40 |48 |56 |64 |72 |80 \n"
            "---------------------------------------\n"
            " 9 |18 |27 |36 |45 |54 |63 |72 |81 |90 \n"
            "---------------------------------------\n"
            "10 |20 |30 |40 |50 |60 |70 |80 |90 |100\n",
        },
        "tight 10",
    ),
    (
        "7\n12\n",
        {
            "     1      |     2      |     3      |     4      |     5      |     6      |     7      \n"
            "------------------------------------------------------------------------------------------\n"
            "     2      |     4      |     6      |     8      |     10     |     12     |     14     \n"
            "------------------------------------------------------------------------------------------\n"
            "     3      |     6      |     9      |     12     |     15     |     18     |     21     \n"
            "------------------------------------------------------------------------------------------\n"
            "     4      |     8      |     12     |     16     |     20     |     24     |     28     \n"
            "------------------------------------------------------------------------------------------\n"
            "     5      |     10     |     15     |     20     |     25     |     30     |     35     \n"
            "------------------------------------------------------------------------------------------\n"
            "     6      |     12     |     18     |     24     |     30     |     36     |     42     \n"
            "------------------------------------------------------------------------------------------\n"
            "     7      |     14     |     21     |     28     |     35     |     42     |     49     ",
            "     1      |     2      |     3      |     4      |     5      |     6      |     7      \n"
            "------------------------------------------------------------------------------------------\n"
            "     2      |     4      |     6      |     8      |     10     |     12     |     14     \n"
            "------------------------------------------------------------------------------------------\n"
            "     3      |     6      |     9      |     12     |     15     |     18     |     21     \n"
            "------------------------------------------------------------------------------------------\n"
            "     4      |     8      |     12     |     16     |     20     |     24     |     28     \n"
            "------------------------------------------------------------------------------------------\n"
            "     5      |     10     |     15     |     20     |     25     |     30     |     35     \n"
            "------------------------------------------------------------------------------------------\n"
            "     6      |     12     |     18     |     24     |     30     |     36     |     42     \n"
            "------------------------------------------------------------------------------------------\n"
            "     7      |     14     |     21     |     28     |     35     |     42     |     49     \n",
        },
        "wide formatting",
    ),
]


q_test_data = [
    ("5\n1\n2\n3\n4\n5\n", "5\n", "first open test"),
    ("3\n123\n454\n321\n", "1\n", "second open test"),
    ("3\n123\n45214\n321\n", "0\n", "no palindromes"),
    ("1\n1212129212121\n", "1\n", "one line one palindrome"),
    ("1\n23\n", "0\n", "one line no palindromes"),
]


r_test_data = [
    (
        "14\n",
        "     1     \n"
        "    2 3    \n"
        "   4 5 6   \n"
        " 7 8 9 10  \n"
        "11 12 13 14\n",
        "first open test",
    ),
    ("6\n", "  1  \n 2 3 \n4 5 6\n", "second open test"),
    (
        "100\n",
        "                  1                   \n"
        "                 2 3                  \n"
        "                4 5 6                 \n"
        "               7 8 9 10               \n"
        "            11 12 13 14 15            \n"
        "          16 17 18 19 20 21           \n"
        "         22 23 24 25 26 27 28         \n"
        "       29 30 31 32 33 34 35 36        \n"
        "      37 38 39 40 41 42 43 44 45      \n"
        "    46 47 48 49 50 51 52 53 54 55     \n"
        "   56 57 58 59 60 61 62 63 64 65 66   \n"
        " 67 68 69 70 71 72 73 74 75 76 77 78  \n"
        "79 80 81 82 83 84 85 86 87 88 89 90 91\n"
        "     92 93 94 95 96 97 98 99 100      \n",
        "100",
    ),
    (
        "201\n",
        "                                     1                                     \n"
        "                                    2 3                                    \n"
        "                                   4 5 6                                   \n"
        "                                 7 8 9 10                                  \n"
        "                              11 12 13 14 15                               \n"
        "                             16 17 18 19 20 21                             \n"
        "                           22 23 24 25 26 27 28                            \n"
        "                          29 30 31 32 33 34 35 36                          \n"
        "                        37 38 39 40 41 42 43 44 45                         \n"
        "                       46 47 48 49 50 51 52 53 54 55                       \n"
        "                     56 57 58 59 60 61 62 63 64 65 66                      \n"
        "                    67 68 69 70 71 72 73 74 75 76 77 78                    \n"
        "                  79 80 81 82 83 84 85 86 87 88 89 90 91                   \n"
        "              92 93 94 95 96 97 98 99 100 101 102 103 104 105              \n"
        "        106 107 108 109 110 111 112 113 114 115 116 117 118 119 120        \n"
        "      121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136      \n"
        "    137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153    \n"
        "  154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171  \n"
        "172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190\n"
        "                191 192 193 194 195 196 197 198 199 200 201                \n",
        "a big tree",
    ),
    ("3\n", " 1 \n2 3\n", "smallest tree"),
]


s_test_data = [
    ("3\n", "1 1 1\n1 2 1\n1 1 1\n", "first open test"),
    (
        "5\n",
        "1 1 1 1 1\n1 2 2 2 1\n1 2 3 2 1\n1 2 2 2 1\n1 1 1 1 1\n",
        "second open test",
    ),
    (
        "19\n",
        " 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1\n"
        " 1  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  1\n"
        " 1  2  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  2  1\n"
        " 1  2  3  4  4  4  4  4  4  4  4  4  4  4  4  4  3  2  1\n"
        " 1  2  3  4  5  5  5  5  5  5  5  5  5  5  5  4  3  2  1\n"
        " 1  2  3  4  5  6  6  6  6  6  6  6  6  6  5  4  3  2  1\n"
        " 1  2  3  4  5  6  7  7  7  7  7  7  7  6  5  4  3  2  1\n"
        " 1  2  3  4  5  6  7  8  8  8  8  8  7  6  5  4  3  2  1\n"
        " 1  2  3  4  5  6  7  8  9  9  9  8  7  6  5  4  3  2  1\n"
        " 1  2  3  4  5  6  7  8  9 10  9  8  7  6  5  4  3  2  1\n"
        " 1  2  3  4  5  6  7  8  9  9  9  8  7  6  5  4  3  2  1\n"
        " 1  2  3  4  5  6  7  8  8  8  8  8  7  6  5  4  3  2  1\n"
        " 1  2  3  4  5  6  7  7  7  7  7  7  7  6  5  4  3  2  1\n"
        " 1  2  3  4  5  6  6  6  6  6  6  6  6  6  5  4  3  2  1\n"
        " 1  2  3  4  5  5  5  5  5  5  5  5  5  5  5  4  3  2  1\n"
        " 1  2  3  4  4  4  4  4  4  4  4  4  4  4  4  4  3  2  1\n"
        " 1  2  3  3  3  3  3  3  3  3  3  3  3  3  3  3  3  2  1\n"
        " 1  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  2  1\n"
        " 1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1  1\n",
        "19",
    ),
]


t_test_data = [
    ("12\n", "7\n", "first open test"),
    ("52\n", "9\n", "second open test"),
    ("99\n", "10\n", "equal digits"),
    ("7901421841\n", "7\n", "large prime number"),
    ("1011101101011\n", "8\n", "binary-like number"),
    ("1\n", "2\n", "one"),
    ("1000000000\n", "6\n", "one mil"),
    ("2\n", "3\n", "small third"),
    ("3\n", "4\n", "small fourth"),
    ("4\n", "5\n", "small fifth"),
    ("631530\n", "4\n", "big fourth"),
    ("10008624\n", "5\n", "big fifth"),
]
