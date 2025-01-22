## [Transliteration](../../../solutions/3.2/32_j.py)

For international documents, Russian text is converted using the Latin alphabet.\
GOST R 52535.1-2006 defines the rules for transliteration of identification cards.\
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

Let's transliterate Russian text.

The letter "ё" should be transliterated as "e", "й" as "i", and "ъ" and "ь" (and their uppercase versions "Ъ" and "Ь") should disappear from the text. Lowercase letters are replaced with lowercase, uppercase with uppercase. If an uppercase letter is transliterated into multiple letters, only the first one should remain uppercase (e.g., "Ц" → "Tc"). All non-Cyrillic characters must remain unchanged.

### Input Format

A single line of Russian text is provided. The text may contain any characters. You need to transliterate only Russian letters, leaving others unchanged. It is guaranteed that there are no words consisting only of the letters "ъ" and "ь".

### Output Format:

Print a single line — the transliterated text.

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