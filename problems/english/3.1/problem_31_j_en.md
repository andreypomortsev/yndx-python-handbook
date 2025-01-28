## [Basic Frequency Analysis](../../../solutions/3.1/31_j.py)

Frequency analysis is the process of counting how often characters appear in a text. It is a crucial tool for breaking many classic ciphers — from the Caesar cipher to the Enigma machine cipher. Let's perform a simple frequency analysis to determine the most frequent character in a given text.

### Input format

Strings are provided, stopping when the string "ФИНИШ" is entered.

### Output format

Output one character in lowercase — the most frequent character.

### Notes

- Spaces are not counted in the analysis.  
- If there are multiple most frequent characters, return the one that comes first alphabetically.

### Example 1

__Input__
```plaintext
Баобаб
Белка
Бобы
ФИНИШ
```

__Output__
```plaintext
б
```

### Example 2

__Input__
```plaintext
Финики Фокачча Зайка
Филин Фосфор Светофор
Фехтовальщик Форма
ФИНИШ
```

__Output__
```plaintext
ф
```

## Approach to the solution

To solve this problem, we will use a frequency analysis algorithm by counting the occurrences of each character using a list. Here’s a step-by-step description of the approach:

__1. Data collection__: 
   - Read the lines until the string "ФИНИШ" is entered.
   - Remove spaces as they are not part of the analysis, and convert all characters to lowercase.

__2. Initialize the counter__:
   - Create a list `char_count` of length 1104, filled with zeros. This will account for all possible characters represented by ASCII codes, though in practice, only a subset will be needed.

__3. Count character frequency__:
   - For each character in the lines, find its ASCII code using the `ord` function.
   - Increase the corresponding value in the `char_count` list.

__4. Find the most frequent character__:
   - Traverse the `char_count` list and find the index with the highest value. This index corresponds to the ASCII code of the most frequent character.
   - If multiple characters have the same frequency, the one that comes first alphabetically will be selected (this is automatically handled by traversing the list from the beginning).

__5. Output the result__:
   - Convert the ASCII code index back to the character using the `chr` function and print it.