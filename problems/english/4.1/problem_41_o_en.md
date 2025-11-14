## [Dictionary String](../../../solutions/4.1/41_o.py)

Now let’s learn how to turn data strings into dictionaries.\
This is useful if you receive configuration data from a text file or process user input.

Create a function `get_dict(text)` that accepts a string of the form:

key1=value1;key2=value2;...

and returns a dictionary with these pairs.

The type of keys is always a string. Try to convert values to `int` or `float` if possible.

### Note

Your solution must contain only functions.\
The solution must not contain calls to the required functions.

<details>
<summary>Hint</summary>

Split the given string using `split` by `;`, and then by `=`.

The `isdigit` method helps determine if a string is an integer.

A floating-point number will look like two integers separated by a dot.

</details>

### Example 1

__Input__

```python
result = get_dict('a=A;b=2;c=-3.5')
```

__Output__

```python
result = {'a': 'A', 'b': 2, 'c': -3.5}
```

### Example 2

__Input__

```python
result = get_dict('id=3-76;ip=127.0.0.1;phone=+7-(123)-456-78-90')
```

__Output__

```python
result = {'id': '3-76', 'ip': '127.0.0.1', 'phone': '+7-(123)-456-78-90'}
```
