## [Транслитерация](../../../solutions/3.2/32_j.py)

Для международных документов русский текст преобразуется с использованием латинского алфавита.\
ГОСТ Р 52535.1-2006 задаёт правила транслитерации идентификационных карт.\
Ниже приведена таблица замен:

- А — A
- Б — B
- В — V
- Г — G
- Д — D
- Е — E
- Ё — E
- Ж — ZH
- З — Z
- И — I
- Й — I
- К — K
- Л — L
- М — M
- Н — N
- О — O
- П — P
- Р — R
- С — S
- Т — T
- У — U
- Ф — F
- Х — KH
- Ц — TC
- Ч — CH
- Ш — SH
- Щ — SHCH
- Ы — Y
- Э — E
- Ю — IU
- Я — IA

Давайте транслитерируем русский текст.

Букву «ё» транслитерируйте как «e», «й» как «и», а «ъ» и «ь» (и их заглавные версии «Ъ» и «Ь») должны исчезнуть из текста. Строчные буквы заменяются на строчные, заглавные заменяются на заглавные. Если заглавная буква превращается при транслитерации в несколько букв, то заглавной должна остаться только первая из них (например, «Ц» → «Tc»). Все некириллические символы должны остаться на месте.

### Формат ввода

В единственной строке задан русский текст. Текст может состоять из любых символов. Вам необходимо транслитерировать только русские буквы, а остальные оставить на месте. Гарантируется, что нет слов, состоящих только из букв «ъ» и «ь».

### Формат вывода:

Выведите одну строку — транслитерированный текст.

### Пример 1

__Ввод__
```plaintext
Привет, мир!
```

__Вывод__
```plaintext
Privet, mir!
```

### Пример 2

__Ввод__
```plaintext
Я помню чудное мгновенье: Передо мной явилась ты, Как мимолетное виденье, Как гений чистой красоты.
```

__Вывод__
```plaintext
Ia pomniu chudnoe mgnovene: Peredo mnoi iavilas ty, Kak mimoletnoe videne, Kak genii chistoi krasoty.
```