## [Result accumulation](../../../solutions/4.3/43_e.py)

In some cases, it's useful to accumulate the result and then retrieve it as a single list.

Implement the `result_accumulator` decorator, which modernizes a function with an unspecified number of positional parameters as follows:

- Adds a named parameter `method` with the default value `accumulate`;
- When the function is called with the `method` parameter equal to `accumulate`, the result is saved in a queue (for each function, its own), and the function returns nothing;
- When the function is called with the `method` parameter equal to `drop`, all accumulated results are returned, and the queue is reset.

### Note

Your solution should only contain functions.\
The solution should not contain calls to the required functions.

### Example 1

__Input__
```python
@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
```

__Output__
```plaintext
None
None
[8, 16, 2]
None
[-6, 45]
```

### Example 2

__Input__
```python
@result_accumulator
def get_letters(text: str) -> str:
    return ''.join(sorted(set(filter(str.isalpha, text.lower()))))


print(get_letters('Hello, world!'))
print(get_letters('Декораторы это круто =)'))
print(get_letters('Ехали медведи на велосипеде', method='drop'))
```

__Output__
```plaintext
None
None
['dehlorw', 'адекортуыэ', 'авдеилмнопсх']
```