## [Guessing Game](../../../solutions/2.3/23_s.py)

Let's simulate the "Guessing Game" between two people. The task is to write a program that guesses a number between 1 and 1000 inclusive, which is chosen by the user (or the testing system). The program needs to guess the number in no more than 10 attempts.

For each attempt, the user will respond with one of the following phrases:

- Bigger (Больше rus);
- Smaller (Меньше rus);
- Guessed (Угадал! rus)!

This task is checked interactively, meaning the system won't provide feedback until the program guesses the number.

### Input Format

The following phrases:

- Больше;
- Меньше;
- Угадал!

### Output Format:

A number between 1 and 1000, guessed by the program.

### Example

Let's say the number 123 was chosen. The dialog between your program and the user/system should look like this:

```
500
Меньше
250
Меньше
125
Меньше
63
Больше
94
Больше
109
Больше
117
Больше
121
Больше
123
Угадал!
```

### Example

__Input__
```plaintext
The number is: 
123
```

__Output__
```plaintext
Угадал!
```

### Approach to the Solution

This task is a simple example of implementing a binary search algorithm.  
Theory on this topic:  
[Тренировки по алгоритмам 5.0 Лекция 4: Бинарный поиск](https://www.youtube.com/live/-B6xvDeGyPg?si=0WLOHFxji0Kg_hkw&t=301)  
[Harvard CS50 2019 - Lecture 0 - Computational Thinking](https://youtu.be/jjqgP9dpD1k?si=UmAM8u0Ca5T5cPvy)

