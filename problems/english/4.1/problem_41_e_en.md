## [Virtual clicker](../../../solutions/4.1/41_e.py)

Let's say you are creating an online clicker—a game where each click increases the score.
Let's implement the basis of such a game in Python.

Create two functions:

- `click()` — increases the counter's value by 1;
- `get_count()` — returns the current value of the counter.

### Note

The solution should not contain calls to the required functions.

<details>
<summary>Hint</summary>

First, create a global variable:

```python
count = 0
```

Additionally, you can put two underscores at the beginning of the name:

```python
__count = 0
```

In Python, such a variable is considered private.

Define the functions:

```python
def click():
    ...
```

```python
def get_count():
    ...
```

In the first function, you will need to change the variable's value; to do this, use the `global` directive. It will link the variable in the local scope with the global variable.

```python
global __count
```

In the second function, you only need the variable's value, so there is no need for the `global` directive.

</details>

### Example 1

__Input__
```python
print(get_count())
click()
print(get_count())
```

__Output__
```plaintext
0
1
```

### Example 2

__Input__
```python
click()
click()
click()
print(get_count())
```

__Output__
```plaintext
3
```