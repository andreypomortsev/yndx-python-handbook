## [Transliteration 2.0](../../../solutions/3.5/35_f.py)

For international documents, Russian text is converted using the Latin alphabet.\
GOST R 52535.1-2006 sets the rules for the transliteration of identification cards.\
Below is the substitution table:

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

Let's transliterate the Russian text.

The letter "ё" should be transliterated as "e", "й" as "i", and "ъ" and "ь" (and their uppercase versions "Ъ" and "Ь") should disappear from the text. Lowercase letters are replaced with lowercase, uppercase letters with uppercase. If an uppercase letter is transformed into several letters during transliteration, only the first of them should remain uppercase (for example, "Ц" → "Tc"). All non-Cyrillic characters should remain unchanged.

### Input Format

In the same folder as your program, there is a file _cyrillic.txt_. It contains, among other things, a number of Cyrillic characters.

### Output Format:

Write the transliteration result to the file _transliteration.txt_.

### Example 1

__Input__
```plaintext
Привет, мир!
```

__Output__
```plaintext
Privet, mir!
```

### Example 2

__Input__
```plaintext
Я помню чудное мгновенье: Передо мной явилась ты, Как мимолетное виденье, Как гений чистой красоты.
```

__Output__
```plaintext
Ia pomniu chudnoe mgnovene: Peredo mnoi iavilas ty, Kak mimoletnoe videne, Kak genii chistoi krasoty.
```