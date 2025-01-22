## [Data update](../../../solutions/3.5/35_m.py)

Often, data needs to be updated.

Create a program that updates a _JSON_ file.

### Input format

The user enters the file name.\
Then, lines of the form key == value are entered.

### Output format:

The updated _JSON_ should be written to the file specified by the user.

### Example

__Input__
```plaintext
# User input:
data.json
one == один
two == два
three == три

# Contents of the data.json file
{
    "one": 1,
    "three": 2
}
```

__Output__
```plaintext
# Contents of the data.json file
{
    "one": "один",
    "three": "три",
    "two": "два"
}
```