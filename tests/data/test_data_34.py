a_test_data = [
    (
        "картина корзина картонка\n",
        "1. картина\n2. корзина\n3. картонка\n",
        "first open test",
    ),
    (
        "Аня Боря Вова\n",
        "1. Аня\n2. Боря\n3. Вова\n",
        "second open test",
    ),
    ("один\n", "1. один\n", "one line"),
    ("один-one\n", "1. один-one\n", "one line two words"),
    (
        "   Аня      Боря     Вова      \n",
        "1. Аня\n2. Боря\n3. Вова\n",
        "trailing whitespaces",
    ),
    (
        "1 2 3 4 5 6 7 8 9 10\n",
        "1. 1\n2. 2\n3. 3\n4. 4\n5. 5\n6. 6\n7. 7\n8. 8\n9. 9\n10. 10\n",
        "ten digits",
    ),
    (
        "10 9 8 7 6 5 4 3 2 1\n",
        "1. 10\n2. 9\n3. 8\n4. 7\n5. 6\n6. 5\n7. 4\n8. 3\n9. 2\n10. 1\n",
        "ten digits reversed",
    ),
]

b_test_data = [
    (
        "Аня, Вова\nБоря, Дима, Гена\n",
        "Аня - Боря\nВова - Дима\n",
        "first open test",
    ),
    ("Аня, Вова\nБоря, Гена\n", "Аня - Боря\nВова - Гена\n", "even number"),
    (
        "Аня, Вова, Боря, Гога\nБоря, Дима, Гена, Вазген\n",
        "Аня - Боря\nВова - Дима\nБоря - Гена\nГога - Вазген\n",
        "even number two",
    ),
    ("Аня\nБоря, Гена\n", "Аня - Боря\n", "one - two"),
    ("Аня, Вова\nГена\n", "Аня - Гена\n", "two - one"),
]

c_test_data = [
    (
        "3.2 6.4 0.8\n",
        {
            "3.20\n4.00\n4.80\n5.60\n6.40\n",
            "3.2\n4.0\n4.8\n5.6\n6.4\n",
        },
        "first open test",
    ),
    (
        "3.14 10 1.57\n",
        "3.14\n4.71\n6.28\n7.85\n9.42\n",
        "second open test",
    ),
    (
        "3.14 4.21 1.07\n",
        "3.14\n4.21\n",
        "boundaries test",
    ),
    (
        "-3.14 -3.21 -0.07\n",
        "-3.14\n-3.21\n",
        "negative boundaries test",
    ),
    (
        "-3.14 4.21 1.07\n",
        {
            "-3.14\n-2.07\n-1.00\n0.07\n1.14\n2.21\n3.28\n",
            "-3.14\n-2.07\n-1.0\n0.07\n1.14\n2.21\n3.28\n",
        },
        "negative to positive",
    ),
    (
        "3.14 -4.21 -1.07\n",
        {
            "3.14\n2.07\n1.00\n-0.07\n-1.14\n-2.21\n-3.28\n",
            "3.14\n2.07\n1.0\n-0.07\n-1.14\n-2.21\n-3.28\n",
        },
        "positive to negative test",
    ),
    (
        "0 2.2 0.43\n",
        "0.00\n0.43\n0.86\n1.29\n1.72\n2.15\n",
        "zero to positive",
    ),
    (
        "0 -2.2 -0.43\n",
        "0.00\n-0.43\n-0.86\n-1.29\n-1.72\n-2.15\n",
        "zero to negative",
    ),
    ("2.3 0 -0.63\n", "2.30\n1.67\n1.04\n0.41\n", "positive to zero"),
    ("-2.3 0 0.63\n", "-2.30\n-1.67\n-1.04\n-0.41\n", "negative to zero"),
]

d_test_data = [
    (
        "мама мыла раму\n",
        "мама\nмама мыла\nмама мыла раму\n",
        "first open test",
    ),
    (
        "картина корзина картонка\n",
        "картина\n" "картина корзина\n" "картина корзина картонка\n",
        "second open test",
    ),
    ("one-line\n", "one-line\n", "one line"),
]

e_test_data = [
    (
        "картина, корзина, картонка\nмыло, манка\nмолоко, хлеб, сыр\n",
        "1. картина\n"
        "2. картонка\n"
        "3. корзина\n"
        "4. манка\n"
        "5. молоко\n"
        "6. мыло\n"
        "7. сыр\n"
        "8. хлеб\n",
        "first open test",
    ),
    (
        "картина, корзина, картонка\n\nмолоко, хлеб, сыр\n",
        "1. картина\n"
        "2. картонка\n"
        "3. корзина\n"
        "4. молоко\n"
        "5. сыр\n"
        "6. хлеб\n",
        "one empty string",
    ),
]

f_test_data = [
    (
        "треф\n",
        "2 пик\n"
        "2 бубен\n"
        "2 червей\n"
        "3 пик\n"
        "3 бубен\n"
        "3 червей\n"
        "4 пик\n"
        "4 бубен\n"
        "4 червей\n"
        "5 пик\n"
        "5 бубен\n"
        "5 червей\n"
        "6 пик\n"
        "6 бубен\n"
        "6 червей\n"
        "7 пик\n"
        "7 бубен\n"
        "7 червей\n"
        "8 пик\n"
        "8 бубен\n"
        "8 червей\n"
        "9 пик\n"
        "9 бубен\n"
        "9 червей\n"
        "10 пик\n"
        "10 бубен\n"
        "10 червей\n"
        "валет пик\n"
        "валет бубен\n"
        "валет червей\n"
        "дама пик\n"
        "дама бубен\n"
        "дама червей\n"
        "король пик\n"
        "король бубен\n"
        "король червей\n"
        "туз пик\n"
        "туз бубен\n"
        "туз червей\n",
        "first open test",
    ),
    (
        "пик\n",
        "2 треф\n"
        "2 бубен\n"
        "2 червей\n"
        "3 треф\n"
        "3 бубен\n"
        "3 червей\n"
        "4 треф\n"
        "4 бубен\n"
        "4 червей\n"
        "5 треф\n"
        "5 бубен\n"
        "5 червей\n"
        "6 треф\n"
        "6 бубен\n"
        "6 червей\n"
        "7 треф\n"
        "7 бубен\n"
        "7 червей\n"
        "8 треф\n"
        "8 бубен\n"
        "8 червей\n"
        "9 треф\n"
        "9 бубен\n"
        "9 червей\n"
        "10 треф\n"
        "10 бубен\n"
        "10 червей\n"
        "валет треф\n"
        "валет бубен\n"
        "валет червей\n"
        "дама треф\n"
        "дама бубен\n"
        "дама червей\n"
        "король треф\n"
        "король бубен\n"
        "король червей\n"
        "туз треф\n"
        "туз бубен\n"
        "туз червей\n",
        "spades",
    ),
    (
        "бубен\n",
        "2 пик\n"
        "2 треф\n"
        "2 червей\n"
        "3 пик\n"
        "3 треф\n"
        "3 червей\n"
        "4 пик\n"
        "4 треф\n"
        "4 червей\n"
        "5 пик\n"
        "5 треф\n"
        "5 червей\n"
        "6 пик\n"
        "6 треф\n"
        "6 червей\n"
        "7 пик\n"
        "7 треф\n"
        "7 червей\n"
        "8 пик\n"
        "8 треф\n"
        "8 червей\n"
        "9 пик\n"
        "9 треф\n"
        "9 червей\n"
        "10 пик\n"
        "10 треф\n"
        "10 червей\n"
        "валет пик\n"
        "валет треф\n"
        "валет червей\n"
        "дама пик\n"
        "дама треф\n"
        "дама червей\n"
        "король пик\n"
        "король треф\n"
        "король червей\n"
        "туз пик\n"
        "туз треф\n"
        "туз червей\n",
        "diamonds",
    ),
    (
        "червей\n",
        "2 пик\n"
        "2 треф\n"
        "2 бубен\n"
        "3 пик\n"
        "3 треф\n"
        "3 бубен\n"
        "4 пик\n"
        "4 треф\n"
        "4 бубен\n"
        "5 пик\n"
        "5 треф\n"
        "5 бубен\n"
        "6 пик\n"
        "6 треф\n"
        "6 бубен\n"
        "7 пик\n"
        "7 треф\n"
        "7 бубен\n"
        "8 пик\n"
        "8 треф\n"
        "8 бубен\n"
        "9 пик\n"
        "9 треф\n"
        "9 бубен\n"
        "10 пик\n"
        "10 треф\n"
        "10 бубен\n"
        "валет пик\n"
        "валет треф\n"
        "валет бубен\n"
        "дама пик\n"
        "дама треф\n"
        "дама бубен\n"
        "король пик\n"
        "король треф\n"
        "король бубен\n"
        "туз пик\n"
        "туз треф\n"
        "туз бубен\n",
        "hearts",
    ),
]

g_test_data = [
    (
        "3\nАня\nБоря\nВова\n",
        "Аня - Боря\nАня - Вова\nБоря - Вова\n",
        "first open test",
    ),
    ("2\nАня\nБоря\n", "Аня - Боря\n", "two players"),
    (
        "4\nАня\nБоря\nДжон\nЕфростинья\n",
        "Аня - Боря\n"
        "Аня - Джон\n"
        "Аня - Ефростинья\n"
        "Боря - Джон\n"
        "Боря - Ефростинья\n"
        "Джон - Ефростинья\n",
        "four players",
    ),
]

h_test_data = [
    (
        "5\nМанная\nГречневая\nПшённая\nОвсяная\nРисовая\n3\n",
        "Манная\nГречневая\nПшённая\n",
        "first open test",
    ),
    (
        "5\n"
        "Манная\n"
        "Гречневая\n"
        "Пшённая\n"
        "Овсяная\n"
        "Рисовая\n"
        "12\n",
        "Манная\n"
        "Гречневая\n"
        "Пшённая\n"
        "Овсяная\n"
        "Рисовая\n"
        "Манная\n"
        "Гречневая\n"
        "Пшённая\n"
        "Овсяная\n"
        "Рисовая\n"
        "Манная\n"
        "Гречневая\n",
        "second open test",
    ),
    (
        "5\nМанная\nГречневая\nПшённая\nОвсяная\nРисовая\n5\n",
        "Манная\nГречневая\nПшённая\nОвсяная\nРисовая\n",
        "poridge == repeats",
    ),
]

l_test_data = [
    (
        "3\nкартина, корзина, картонка\nмыло, манка\nмолоко, хлеб, сыр\n",
        "1. картина\n"
        "2. картонка\n"
        "3. корзина\n"
        "4. манка\n"
        "5. молоко\n"
        "6. мыло\n"
        "7. сыр\n"
        "8. хлеб\n",
        "first open test",
    ),
    (
        "2\nпеченье, сушки\nчай, кофе\n",
        "1. кофе\n2. печенье\n3. сушки\n4. чай\n",
        "second open test",
    ),
    (
        "3\nкартина, корзина, картонка\n\nмолоко, хлеб, сыр\n",
        "1. картина\n"
        "2. картонка\n"
        "3. корзина\n"
        "4. молоко\n"
        "5. сыр\n"
        "6. хлеб\n",
        "one empty string",
    ),
]

m_test_data = [
    (
        "3\nАня\nБоря\nВова\n",
        "Аня, Боря, Вова\n"
        "Аня, Вова, Боря\n"
        "Боря, Аня, Вова\n"
        "Боря, Вова, Аня\n"
        "Вова, Аня, Боря\n"
        "Вова, Боря, Аня\n",
        "first open test",
    ),
    (
        "4\nВова\nАня\nДима\nБоря\n",
        "Аня, Боря, Вова, Дима\n"
        "Аня, Боря, Дима, Вова\n"
        "Аня, Вова, Боря, Дима\n"
        "Аня, Вова, Дима, Боря\n"
        "Аня, Дима, Боря, Вова\n"
        "Аня, Дима, Вова, Боря\n"
        "Боря, Аня, Вова, Дима\n"
        "Боря, Аня, Дима, Вова\n"
        "Боря, Вова, Аня, Дима\n"
        "Боря, Вова, Дима, Аня\n"
        "Боря, Дима, Аня, Вова\n"
        "Боря, Дима, Вова, Аня\n"
        "Вова, Аня, Боря, Дима\n"
        "Вова, Аня, Дима, Боря\n"
        "Вова, Боря, Аня, Дима\n"
        "Вова, Боря, Дима, Аня\n"
        "Вова, Дима, Аня, Боря\n"
        "Вова, Дима, Боря, Аня\n"
        "Дима, Аня, Боря, Вова\n"
        "Дима, Аня, Вова, Боря\n"
        "Дима, Боря, Аня, Вова\n"
        "Дима, Боря, Вова, Аня\n"
        "Дима, Вова, Аня, Боря\n"
        "Дима, Вова, Боря, Аня\n",
        "second open test",
    ),
    ("2\nАня\nДима\n", "Аня, Дима\nДима, Аня\n", "two of us"),
    ("1\nВова\n", "Вова\n", "lonely champ"),
]

n_test_data = [
    (
        "3\nАня\nБоря\nВова\n",
        "Аня, Боря, Вова\n"
        "Аня, Вова, Боря\n"
        "Боря, Аня, Вова\n"
        "Боря, Вова, Аня\n"
        "Вова, Аня, Боря\n"
        "Вова, Боря, Аня\n",
        "first open test",
    ),
    (
        "4\nВова\nАня\nДима\nБоря\n",
        "Аня, Боря, Вова\n"
        "Аня, Боря, Дима\n"
        "Аня, Вова, Боря\n"
        "Аня, Вова, Дима\n"
        "Аня, Дима, Боря\n"
        "Аня, Дима, Вова\n"
        "Боря, Аня, Вова\n"
        "Боря, Аня, Дима\n"
        "Боря, Вова, Аня\n"
        "Боря, Вова, Дима\n"
        "Боря, Дима, Аня\n"
        "Боря, Дима, Вова\n"
        "Вова, Аня, Боря\n"
        "Вова, Аня, Дима\n"
        "Вова, Боря, Аня\n"
        "Вова, Боря, Дима\n"
        "Вова, Дима, Аня\n"
        "Вова, Дима, Боря\n"
        "Дима, Аня, Боря\n"
        "Дима, Аня, Вова\n"
        "Дима, Боря, Аня\n"
        "Дима, Боря, Вова\n"
        "Дима, Вова, Аня\n"
        "Дима, Вова, Боря\n",
        "four athletes",
    ),
]

o_test_data = [
    (
        "2\nпеченье, сушки\nчай, кофе\n",
        "кофе печенье сушки\n"
        "кофе печенье чай\n"
        "кофе сушки печенье\n"
        "кофе сушки чай\n"
        "кофе чай печенье\n"
        "кофе чай сушки\n"
        "печенье кофе сушки\n"
        "печенье кофе чай\n"
        "печенье сушки кофе\n"
        "печенье сушки чай\n"
        "печенье чай кофе\n"
        "печенье чай сушки\n"
        "сушки кофе печенье\n"
        "сушки кофе чай\n"
        "сушки печенье кофе\n"
        "сушки печенье чай\n"
        "сушки чай кофе\n"
        "сушки чай печенье\n"
        "чай кофе печенье\n"
        "чай кофе сушки\n"
        "чай печенье кофе\n"
        "чай печенье сушки\n"
        "чай сушки кофе\n"
        "чай сушки печенье\n",
        "first opne test",
    ),
    (
        "4\nпеченье, сушки, яблоки\nчай, кофе\nабрикосы\nхлеб, сахар\n",
        "абрикосы кофе печенье\n"
        "абрикосы кофе сахар\n"
        "абрикосы кофе сушки\n"
        "абрикосы кофе хлеб\n"
        "абрикосы кофе чай\n"
        "абрикосы кофе яблоки\n"
        "абрикосы печенье кофе\n"
        "абрикосы печенье сахар\n"
        "абрикосы печенье сушки\n"
        "абрикосы печенье хлеб\n"
        "абрикосы печенье чай\n"
        "абрикосы печенье яблоки\n"
        "абрикосы сахар кофе\n"
        "абрикосы сахар печенье\n"
        "абрикосы сахар сушки\n"
        "абрикосы сахар хлеб\n"
        "абрикосы сахар чай\n"
        "абрикосы сахар яблоки\n"
        "абрикосы сушки кофе\n"
        "абрикосы сушки печенье\n"
        "абрикосы сушки сахар\n"
        "абрикосы сушки хлеб\n"
        "абрикосы сушки чай\n"
        "абрикосы сушки яблоки\n"
        "абрикосы хлеб кофе\n"
        "абрикосы хлеб печенье\n"
        "абрикосы хлеб сахар\n"
        "абрикосы хлеб сушки\n"
        "абрикосы хлеб чай\n"
        "абрикосы хлеб яблоки\n"
        "абрикосы чай кофе\n"
        "абрикосы чай печенье\n"
        "абрикосы чай сахар\n"
        "абрикосы чай сушки\n"
        "абрикосы чай хлеб\n"
        "абрикосы чай яблоки\n"
        "абрикосы яблоки кофе\n"
        "абрикосы яблоки печенье\n"
        "абрикосы яблоки сахар\n"
        "абрикосы яблоки сушки\n"
        "абрикосы яблоки хлеб\n"
        "абрикосы яблоки чай\n"
        "кофе абрикосы печенье\n"
        "кофе абрикосы сахар\n"
        "кофе абрикосы сушки\n"
        "кофе абрикосы хлеб\n"
        "кофе абрикосы чай\n"
        "кофе абрикосы яблоки\n"
        "кофе печенье абрикосы\n"
        "кофе печенье сахар\n"
        "кофе печенье сушки\n"
        "кофе печенье хлеб\n"
        "кофе печенье чай\n"
        "кофе печенье яблоки\n"
        "кофе сахар абрикосы\n"
        "кофе сахар печенье\n"
        "кофе сахар сушки\n"
        "кофе сахар хлеб\n"
        "кофе сахар чай\n"
        "кофе сахар яблоки\n"
        "кофе сушки абрикосы\n"
        "кофе сушки печенье\n"
        "кофе сушки сахар\n"
        "кофе сушки хлеб\n"
        "кофе сушки чай\n"
        "кофе сушки яблоки\n"
        "кофе хлеб абрикосы\n"
        "кофе хлеб печенье\n"
        "кофе хлеб сахар\n"
        "кофе хлеб сушки\n"
        "кофе хлеб чай\n"
        "кофе хлеб яблоки\n"
        "кофе чай абрикосы\n"
        "кофе чай печенье\n"
        "кофе чай сахар\n"
        "кофе чай сушки\n"
        "кофе чай хлеб\n"
        "кофе чай яблоки\n"
        "кофе яблоки абрикосы\n"
        "кофе яблоки печенье\n"
        "кофе яблоки сахар\n"
        "кофе яблоки сушки\n"
        "кофе яблоки хлеб\n"
        "кофе яблоки чай\n"
        "печенье абрикосы кофе\n"
        "печенье абрикосы сахар\n"
        "печенье абрикосы сушки\n"
        "печенье абрикосы хлеб\n"
        "печенье абрикосы чай\n"
        "печенье абрикосы яблоки\n"
        "печенье кофе абрикосы\n"
        "печенье кофе сахар\n"
        "печенье кофе сушки\n"
        "печенье кофе хлеб\n"
        "печенье кофе чай\n"
        "печенье кофе яблоки\n"
        "печенье сахар абрикосы\n"
        "печенье сахар кофе\n"
        "печенье сахар сушки\n"
        "печенье сахар хлеб\n"
        "печенье сахар чай\n"
        "печенье сахар яблоки\n"
        "печенье сушки абрикосы\n"
        "печенье сушки кофе\n"
        "печенье сушки сахар\n"
        "печенье сушки хлеб\n"
        "печенье сушки чай\n"
        "печенье сушки яблоки\n"
        "печенье хлеб абрикосы\n"
        "печенье хлеб кофе\n"
        "печенье хлеб сахар\n"
        "печенье хлеб сушки\n"
        "печенье хлеб чай\n"
        "печенье хлеб яблоки\n"
        "печенье чай абрикосы\n"
        "печенье чай кофе\n"
        "печенье чай сахар\n"
        "печенье чай сушки\n"
        "печенье чай хлеб\n"
        "печенье чай яблоки\n"
        "печенье яблоки абрикосы\n"
        "печенье яблоки кофе\n"
        "печенье яблоки сахар\n"
        "печенье яблоки сушки\n"
        "печенье яблоки хлеб\n"
        "печенье яблоки чай\n"
        "сахар абрикосы кофе\n"
        "сахар абрикосы печенье\n"
        "сахар абрикосы сушки\n"
        "сахар абрикосы хлеб\n"
        "сахар абрикосы чай\n"
        "сахар абрикосы яблоки\n"
        "сахар кофе абрикосы\n"
        "сахар кофе печенье\n"
        "сахар кофе сушки\n"
        "сахар кофе хлеб\n"
        "сахар кофе чай\n"
        "сахар кофе яблоки\n"
        "сахар печенье абрикосы\n"
        "сахар печенье кофе\n"
        "сахар печенье сушки\n"
        "сахар печенье хлеб\n"
        "сахар печенье чай\n"
        "сахар печенье яблоки\n"
        "сахар сушки абрикосы\n"
        "сахар сушки кофе\n"
        "сахар сушки печенье\n"
        "сахар сушки хлеб\n"
        "сахар сушки чай\n"
        "сахар сушки яблоки\n"
        "сахар хлеб абрикосы\n"
        "сахар хлеб кофе\n"
        "сахар хлеб печенье\n"
        "сахар хлеб сушки\n"
        "сахар хлеб чай\n"
        "сахар хлеб яблоки\n"
        "сахар чай абрикосы\n"
        "сахар чай кофе\n"
        "сахар чай печенье\n"
        "сахар чай сушки\n"
        "сахар чай хлеб\n"
        "сахар чай яблоки\n"
        "сахар яблоки абрикосы\n"
        "сахар яблоки кофе\n"
        "сахар яблоки печенье\n"
        "сахар яблоки сушки\n"
        "сахар яблоки хлеб\n"
        "сахар яблоки чай\n"
        "сушки абрикосы кофе\n"
        "сушки абрикосы печенье\n"
        "сушки абрикосы сахар\n"
        "сушки абрикосы хлеб\n"
        "сушки абрикосы чай\n"
        "сушки абрикосы яблоки\n"
        "сушки кофе абрикосы\n"
        "сушки кофе печенье\n"
        "сушки кофе сахар\n"
        "сушки кофе хлеб\n"
        "сушки кофе чай\n"
        "сушки кофе яблоки\n"
        "сушки печенье абрикосы\n"
        "сушки печенье кофе\n"
        "сушки печенье сахар\n"
        "сушки печенье хлеб\n"
        "сушки печенье чай\n"
        "сушки печенье яблоки\n"
        "сушки сахар абрикосы\n"
        "сушки сахар кофе\n"
        "сушки сахар печенье\n"
        "сушки сахар хлеб\n"
        "сушки сахар чай\n"
        "сушки сахар яблоки\n"
        "сушки хлеб абрикосы\n"
        "сушки хлеб кофе\n"
        "сушки хлеб печенье\n"
        "сушки хлеб сахар\n"
        "сушки хлеб чай\n"
        "сушки хлеб яблоки\n"
        "сушки чай абрикосы\n"
        "сушки чай кофе\n"
        "сушки чай печенье\n"
        "сушки чай сахар\n"
        "сушки чай хлеб\n"
        "сушки чай яблоки\n"
        "сушки яблоки абрикосы\n"
        "сушки яблоки кофе\n"
        "сушки яблоки печенье\n"
        "сушки яблоки сахар\n"
        "сушки яблоки хлеб\n"
        "сушки яблоки чай\n"
        "хлеб абрикосы кофе\n"
        "хлеб абрикосы печенье\n"
        "хлеб абрикосы сахар\n"
        "хлеб абрикосы сушки\n"
        "хлеб абрикосы чай\n"
        "хлеб абрикосы яблоки\n"
        "хлеб кофе абрикосы\n"
        "хлеб кофе печенье\n"
        "хлеб кофе сахар\n"
        "хлеб кофе сушки\n"
        "хлеб кофе чай\n"
        "хлеб кофе яблоки\n"
        "хлеб печенье абрикосы\n"
        "хлеб печенье кофе\n"
        "хлеб печенье сахар\n"
        "хлеб печенье сушки\n"
        "хлеб печенье чай\n"
        "хлеб печенье яблоки\n"
        "хлеб сахар абрикосы\n"
        "хлеб сахар кофе\n"
        "хлеб сахар печенье\n"
        "хлеб сахар сушки\n"
        "хлеб сахар чай\n"
        "хлеб сахар яблоки\n"
        "хлеб сушки абрикосы\n"
        "хлеб сушки кофе\n"
        "хлеб сушки печенье\n"
        "хлеб сушки сахар\n"
        "хлеб сушки чай\n"
        "хлеб сушки яблоки\n"
        "хлеб чай абрикосы\n"
        "хлеб чай кофе\n"
        "хлеб чай печенье\n"
        "хлеб чай сахар\n"
        "хлеб чай сушки\n"
        "хлеб чай яблоки\n"
        "хлеб яблоки абрикосы\n"
        "хлеб яблоки кофе\n"
        "хлеб яблоки печенье\n"
        "хлеб яблоки сахар\n"
        "хлеб яблоки сушки\n"
        "хлеб яблоки чай\n"
        "чай абрикосы кофе\n"
        "чай абрикосы печенье\n"
        "чай абрикосы сахар\n"
        "чай абрикосы сушки\n"
        "чай абрикосы хлеб\n"
        "чай абрикосы яблоки\n"
        "чай кофе абрикосы\n"
        "чай кофе печенье\n"
        "чай кофе сахар\n"
        "чай кофе сушки\n"
        "чай кофе хлеб\n"
        "чай кофе яблоки\n"
        "чай печенье абрикосы\n"
        "чай печенье кофе\n"
        "чай печенье сахар\n"
        "чай печенье сушки\n"
        "чай печенье хлеб\n"
        "чай печенье яблоки\n"
        "чай сахар абрикосы\n"
        "чай сахар кофе\n"
        "чай сахар печенье\n"
        "чай сахар сушки\n"
        "чай сахар хлеб\n"
        "чай сахар яблоки\n"
        "чай сушки абрикосы\n"
        "чай сушки кофе\n"
        "чай сушки печенье\n"
        "чай сушки сахар\n"
        "чай сушки хлеб\n"
        "чай сушки яблоки\n"
        "чай хлеб абрикосы\n"
        "чай хлеб кофе\n"
        "чай хлеб печенье\n"
        "чай хлеб сахар\n"
        "чай хлеб сушки\n"
        "чай хлеб яблоки\n"
        "чай яблоки абрикосы\n"
        "чай яблоки кофе\n"
        "чай яблоки печенье\n"
        "чай яблоки сахар\n"
        "чай яблоки сушки\n"
        "чай яблоки хлеб\n"
        "яблоки абрикосы кофе\n"
        "яблоки абрикосы печенье\n"
        "яблоки абрикосы сахар\n"
        "яблоки абрикосы сушки\n"
        "яблоки абрикосы хлеб\n"
        "яблоки абрикосы чай\n"
        "яблоки кофе абрикосы\n"
        "яблоки кофе печенье\n"
        "яблоки кофе сахар\n"
        "яблоки кофе сушки\n"
        "яблоки кофе хлеб\n"
        "яблоки кофе чай\n"
        "яблоки печенье абрикосы\n"
        "яблоки печенье кофе\n"
        "яблоки печенье сахар\n"
        "яблоки печенье сушки\n"
        "яблоки печенье хлеб\n"
        "яблоки печенье чай\n"
        "яблоки сахар абрикосы\n"
        "яблоки сахар кофе\n"
        "яблоки сахар печенье\n"
        "яблоки сахар сушки\n"
        "яблоки сахар хлеб\n"
        "яблоки сахар чай\n"
        "яблоки сушки абрикосы\n"
        "яблоки сушки кофе\n"
        "яблоки сушки печенье\n"
        "яблоки сушки сахар\n"
        "яблоки сушки хлеб\n"
        "яблоки сушки чай\n"
        "яблоки хлеб абрикосы\n"
        "яблоки хлеб кофе\n"
        "яблоки хлеб печенье\n"
        "яблоки хлеб сахар\n"
        "яблоки хлеб сушки\n"
        "яблоки хлеб чай\n"
        "яблоки чай абрикосы\n"
        "яблоки чай кофе\n"
        "яблоки чай печенье\n"
        "яблоки чай сахар\n"
        "яблоки чай сушки\n"
        "яблоки чай хлеб\n",
        "a lot of options",
    ),
    (
        "1\nпеченье, сушки, яблоки\n",
        "печенье сушки яблоки\n"
        "печенье яблоки сушки\n"
        "сушки печенье яблоки\n"
        "сушки яблоки печенье\n"
        "яблоки печенье сушки\n"
        "яблоки сушки печенье\n",
        "lonesome",
    ),
]

p_test_data = [
    (
        "пики\n10\n",
        "2 бубен, 2 пик, 2 треф\n"
        "2 бубен, 2 пик, 2 червей\n"
        "2 бубен, 2 пик, 3 бубен\n"
        "2 бубен, 2 пик, 3 пик\n"
        "2 бубен, 2 пик, 3 треф\n"
        "2 бубен, 2 пик, 3 червей\n"
        "2 бубен, 2 пик, 4 бубен\n"
        "2 бубен, 2 пик, 4 пик\n"
        "2 бубен, 2 пик, 4 треф\n"
        "2 бубен, 2 пик, 4 червей\n",
        "first open test",
    ),
    (
        "трефы\nкороль\n",
        "10 бубен, 10 пик, 10 треф\n"
        "10 бубен, 10 пик, 2 треф\n"
        "10 бубен, 10 пик, 3 треф\n"
        "10 бубен, 10 пик, 4 треф\n"
        "10 бубен, 10 пик, 5 треф\n"
        "10 бубен, 10 пик, 6 треф\n"
        "10 бубен, 10 пик, 7 треф\n"
        "10 бубен, 10 пик, 8 треф\n"
        "10 бубен, 10 пик, 9 треф\n"
        "10 бубен, 10 пик, валет треф\n",
        "second open test",
    ),
    (
        "буби\n2\n",
        "10 бубен, 10 пик, 10 треф\n"
        "10 бубен, 10 пик, 10 червей\n"
        "10 бубен, 10 пик, 3 бубен\n"
        "10 бубен, 10 пик, 3 пик\n"
        "10 бубен, 10 пик, 3 треф\n"
        "10 бубен, 10 пик, 3 червей\n"
        "10 бубен, 10 пик, 4 бубен\n"
        "10 бубен, 10 пик, 4 пик\n"
        "10 бубен, 10 пик, 4 треф\n"
        "10 бубен, 10 пик, 4 червей\n",
        "diamonds two",
    ),
    (
        "черви\nтуз\n",
        "10 бубен, 10 пик, 10 червей\n"
        "10 бубен, 10 пик, 2 червей\n"
        "10 бубен, 10 пик, 3 червей\n"
        "10 бубен, 10 пик, 4 червей\n"
        "10 бубен, 10 пик, 5 червей\n"
        "10 бубен, 10 пик, 6 червей\n"
        "10 бубен, 10 пик, 7 червей\n"
        "10 бубен, 10 пик, 8 червей\n"
        "10 бубен, 10 пик, 9 червей\n"
        "10 бубен, 10 пик, валет червей\n",
        "hearts ace",
    ),
    (
        "черви\n10\n",
        "2 бубен, 2 пик, 2 червей\n"
        "2 бубен, 2 пик, 3 червей\n"
        "2 бубен, 2 пик, 4 червей\n"
        "2 бубен, 2 пик, 5 червей\n"
        "2 бубен, 2 пик, 6 червей\n"
        "2 бубен, 2 пик, 7 червей\n"
        "2 бубен, 2 пик, 8 червей\n"
        "2 бубен, 2 пик, 9 червей\n"
        "2 бубен, 2 пик, валет червей\n"
        "2 бубен, 2 пик, дама червей\n",
        "hearts ten",
    ),
]

q_test_data = [
    (
        "пики\n10\n9 пик, король треф, туз червей\n",
        "9 пик, король червей, туз бубен\n",
        "first open test",
    ),
    (
        "трефы\nкороль\n2 червей, туз пик, туз треф\n",
        "2 червей, туз треф, туз червей\n",
        "second open test",
    ),
]

r_test_data = [
    (
        "not a or b and c\n",
        "a b c f\n"
        "0 0 0 1\n"
        "0 0 1 1\n"
        "0 1 0 1\n"
        "0 1 1 1\n"
        "1 0 0 0\n"
        "1 0 1 0\n"
        "1 1 0 0\n"
        "1 1 1 1\n",
        "first open test",
    ),
    (
        "a and not b and c\n",
        "a b c f\n"
        "0 0 0 0\n"
        "0 0 1 0\n"
        "0 1 0 0\n"
        "0 1 1 0\n"
        "1 0 0 0\n"
        "1 0 1 1\n"
        "1 1 0 0\n"
        "1 1 1 0\n",
        "second open test",
    ),
    (
        "not a and not b and c or a\n",
        "a b c f\n"
        "0 0 0 0\n"
        "0 0 1 1\n"
        "0 1 0 0\n"
        "0 1 1 0\n"
        "1 0 0 1\n"
        "1 0 1 1\n"
        "1 1 0 1\n"
        "1 1 1 1\n",
        "double a",
    ),
    (
        "a and b and c or not c\n",
        "a b c f\n"
        "0 0 0 1\n"
        "0 0 1 0\n"
        "0 1 0 1\n"
        "0 1 1 0\n"
        "1 0 0 1\n"
        "1 0 1 0\n"
        "1 1 0 1\n"
        "1 1 1 1\n",
        "c or not c",
    ),
    (
        "a and b and c\n",
        "a b c f\n"
        "0 0 0 0\n"
        "0 0 1 0\n"
        "0 1 0 0\n"
        "0 1 1 0\n"
        "1 0 0 0\n"
        "1 0 1 0\n"
        "1 1 0 0\n"
        "1 1 1 1\n",
        "three ands",
    ),
]

s_test_data = [
    (
        "not A or B and C\n",
        "A B C F\n"
        "0 0 0 1\n"
        "0 0 1 1\n"
        "0 1 0 1\n"
        "0 1 1 1\n"
        "1 0 0 0\n"
        "1 0 1 0\n"
        "1 1 0 0\n"
        "1 1 1 1\n",
        "first open test",
    ),
    (
        "A and not B and A\n",
        "A B F\n" "0 0 0\n" "0 1 0\n" "1 0 1\n" "1 1 0\n",
        "second open test",
    ),
    ("A and not A and A\n", "A F\n0 0\n1 0\n", "one variable"),
    ("X and not X and X\n", "X F\n0 0\n1 0\n", "one last variable"),
]

t_test_data = [
    (
        "A -> B ~ C\n",
        "A B C F\n"
        "0 0 0 0\n"
        "0 0 1 1\n"
        "0 1 0 0\n"
        "0 1 1 1\n"
        "1 0 0 1\n"
        "1 0 1 0\n"
        "1 1 0 0\n"
        "1 1 1 1\n",
        "first open test",
    ),
    (
        "A or C ~ not (A -> B) or C\n",
        "A B C F\n"
        "0 0 0 1\n"
        "0 0 1 1\n"
        "0 1 0 1\n"
        "0 1 1 1\n"
        "1 0 0 1\n"
        "1 0 1 1\n"
        "1 1 0 0\n"
        "1 1 1 1\n",
        "second open test",
    ),
    (
        "A or C~ not(A -> B) or C\n",
        "A B C F\n"
        "0 0 0 1\n"
        "0 0 1 1\n"
        "0 1 0 1\n"
        "0 1 1 1\n"
        "1 0 0 1\n"
        "1 0 1 1\n"
        "1 1 0 0\n"
        "1 1 1 1\n",
        "missed whitespaces",
    ),
    (
        "Z or not X ^((not A) ~ (D and W)) -> Z\n",
        "A D W X Z F\n"
        "0 0 0 0 0 0\n"
        "0 0 0 0 1 1\n"
        "0 0 0 1 0 1\n"
        "0 0 0 1 1 1\n"
        "0 0 1 0 0 0\n"
        "0 0 1 0 1 1\n"
        "0 0 1 1 0 1\n"
        "0 0 1 1 1 1\n"
        "0 1 0 0 0 0\n"
        "0 1 0 0 1 1\n"
        "0 1 0 1 0 1\n"
        "0 1 0 1 1 1\n"
        "0 1 1 0 0 1\n"
        "0 1 1 0 1 1\n"
        "0 1 1 1 0 0\n"
        "0 1 1 1 1 1\n"
        "1 0 0 0 0 1\n"
        "1 0 0 0 1 1\n"
        "1 0 0 1 0 0\n"
        "1 0 0 1 1 1\n"
        "1 0 1 0 0 1\n"
        "1 0 1 0 1 1\n"
        "1 0 1 1 0 0\n"
        "1 0 1 1 1 1\n"
        "1 1 0 0 0 1\n"
        "1 1 0 0 1 1\n"
        "1 1 0 1 0 0\n"
        "1 1 0 1 1 1\n"
        "1 1 1 0 0 0\n"
        "1 1 1 0 1 1\n"
        "1 1 1 1 0 1\n"
        "1 1 1 1 1 1\n",
        "mixed var names",
    ),
    ("A and not A and A\n", "A F\n0 0\n1 0\n", "one variable"),
    ("X and not X and X\n", "X F\n0 0\n1 0\n", "one last variable"),
    (
        "A and (G or ((not X) )^((not A ~ (D and W))) -> (Z ^ G))\n",
        "A D G W X Z F\n"
        "0 0 0 0 0 0 0\n"
        "0 0 0 0 0 1 0\n"
        "0 0 0 0 1 0 0\n"
        "0 0 0 0 1 1 0\n"
        "0 0 0 1 0 0 0\n"
        "0 0 0 1 0 1 0\n"
        "0 0 0 1 1 0 0\n"
        "0 0 0 1 1 1 0\n"
        "0 0 1 0 0 0 0\n"
        "0 0 1 0 0 1 0\n"
        "0 0 1 0 1 0 0\n"
        "0 0 1 0 1 1 0\n"
        "0 0 1 1 0 0 0\n"
        "0 0 1 1 0 1 0\n"
        "0 0 1 1 1 0 0\n"
        "0 0 1 1 1 1 0\n"
        "0 1 0 0 0 0 0\n"
        "0 1 0 0 0 1 0\n"
        "0 1 0 0 1 0 0\n"
        "0 1 0 0 1 1 0\n"
        "0 1 0 1 0 0 0\n"
        "0 1 0 1 0 1 0\n"
        "0 1 0 1 1 0 0\n"
        "0 1 0 1 1 1 0\n"
        "0 1 1 0 0 0 0\n"
        "0 1 1 0 0 1 0\n"
        "0 1 1 0 1 0 0\n"
        "0 1 1 0 1 1 0\n"
        "0 1 1 1 0 0 0\n"
        "0 1 1 1 0 1 0\n"
        "0 1 1 1 1 0 0\n"
        "0 1 1 1 1 1 0\n"
        "1 0 0 0 0 0 1\n"
        "1 0 0 0 0 1 1\n"
        "1 0 0 0 1 0 0\n"
        "1 0 0 0 1 1 1\n"
        "1 0 0 1 0 0 1\n"
        "1 0 0 1 0 1 1\n"
        "1 0 0 1 1 0 0\n"
        "1 0 0 1 1 1 1\n"
        "1 0 1 0 0 0 1\n"
        "1 0 1 0 0 1 1\n"
        "1 0 1 0 1 0 1\n"
        "1 0 1 0 1 1 1\n"
        "1 0 1 1 0 0 1\n"
        "1 0 1 1 0 1 1\n"
        "1 0 1 1 1 0 1\n"
        "1 0 1 1 1 1 1\n"
        "1 1 0 0 0 0 1\n"
        "1 1 0 0 0 1 1\n"
        "1 1 0 0 1 0 0\n"
        "1 1 0 0 1 1 1\n"
        "1 1 0 1 0 0 0\n"
        "1 1 0 1 0 1 1\n"
        "1 1 0 1 1 0 1\n"
        "1 1 0 1 1 1 1\n"
        "1 1 1 0 0 0 1\n"
        "1 1 1 0 0 1 1\n"
        "1 1 1 0 1 0 1\n"
        "1 1 1 0 1 1 1\n"
        "1 1 1 1 0 0 1\n"
        "1 1 1 1 0 1 0\n"
        "1 1 1 1 1 0 1\n"
        "1 1 1 1 1 1 0\n",
        "a few brackets",
    ),
]
