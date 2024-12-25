## [Automation of Safety](../../../solutions/2.2/22_s.py)

A group of researchers is about to land on an island with an incredibly regular shape, but satellite reconnaissance revealed a quicksand zone on the island.

To increase the expedition's safety, it was decided to develop a warning system that will alert researchers about danger. To reduce production costs, it was decided to order the software.

![Plot](../../russian/2.2/problem_22_s_visual.png)

Write a program that, based on the coordinates of a researcher, will report the safety of that point.

### Input Format

Two rational numbers — the coordinates of the researcher.

### Output Format:

One of the following messages:

- Опасность! Покиньте зону как можно скорее!
- Зона безопасна. Продолжайте работу.
- Вы вышли в море и рискуете быть съеденным акулой!

### Example 1

**Input**
```plaintext
3.5
-3.2
```

**Output**
```plaintext
Опасность! Покиньте зону как можно скорее!
```

### Example 2

**Input**
```plaintext
-5.2
3.4
```

**Output**
```plaintext
Зона безопасна. Продолжайте работу.
```