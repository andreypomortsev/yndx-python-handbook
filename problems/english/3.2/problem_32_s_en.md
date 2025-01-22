## [Private Property](../../../solutions/3.2/32_s.py)

The kids bring toys to the kindergarten and play together. Today, they decided to find out which toys belong to only one of the children. Write a program that, based on a list of children and their toys, determines the "private property."

### Input format

The first line specifies the number of children in the group ($N$).  
Each of the next $N$ lines contains a child's name and their toys in the format:  
_Name: toy1, toy2, ...._

### Output format:

A list of toys that belong to only one of the children, sorted in alphabetical order.

### Example

__Input__
```plaintext
3
Аня: кукла, машинка, кукла, домик
Боря: машинка, зайчик
Вова: кубики, машинка
```

__Output__
```plaintext
домик
зайчик
кубики
кукла
```