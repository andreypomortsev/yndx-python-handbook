## [Don't Press the Red Button!](../../../solutions/5.1/51_c.py)

If you write a warning "Don't press the red button!", you will immediately want to press it.

Write a class `RedButton` that describes the red button.

The class should implement the following methods:

- `click()` — simulates pressing the button and prints the message "Тревога!" ("Alert!");
- `count()` — returns the number of times the button has been pressed.

### Note

Your solution should only contain classes and functions.\
The solution should not contain initialization calls of the required classes.

### Example

__Input__
```python
first_button = RedButton()
second_button = RedButton()
for time in range(5):
    if time % 2 == 0:
        second_button.click()
    else:
        first_button.click()
print(first_button.count(), second_button.count())
```

__Output__
```plaintext
Тревога!
Тревога!
Тревога!
Тревога!
Тревога!
2 3
```