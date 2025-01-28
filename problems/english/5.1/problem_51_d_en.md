## [Work is not Going Anywhere](../../../solutions/5.1/51_d.py)

Consider an object "Programmer," which is defined by a name, position, and the number of hours worked. Each position has its own hourly wage. In our improvised company, there are 3 positions:

- _Junior_ — with a wage of 10 tugriks per hour;
- _Middle_ — with a wage of 15 tugriks per hour;
- _Senior_ — with a wage of 20 tugriks per hour by default and an additional 1 tugrik for each promotion.

Write a class `Programmer` that initializes with a name and a position (a new employee starts with zero hours worked). The class implements the following methods:

- `work(time)` — records the number of hours worked (`time`);
- `rise()` — promotes the programmer;
- `info()` — returns a string for accounting in the format: _<name> <number of hours worked>ч. <accumulated salary>тгр._

### Note

Your solution should contain only classes and functions.\
There should be no calls to the required class initialization.

### Example

__Input__
```python
programmer = Programmer('Vasilyev Ivan', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
```

__Output__
```plaintext
Vasilyev Ivan 750ч. 7500тгр.
Vasilyev Ivan 1250ч. 15000тгр.
Vasilyev Ivan 1500ч. 20000тгр.
Vasilyev Ivan 1750ч. 25250тгр.
```