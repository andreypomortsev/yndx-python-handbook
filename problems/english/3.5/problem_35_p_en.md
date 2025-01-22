## [Everything can be found 3.0](../../../solutions/3.5/35_p.py)

Let's write a small search system component again.

### Input format

First, a search query is entered.\
Then, file names are entered, among which the search should be performed.

### Output format:

Output all file names that contain the search string, ignoring case and repeated whitespace characters.\
If no information is found in any file, output "404. Not Found".

### Note

The search system should treat strings like "a\&nbsp;\&nbsp;\&nbsp;\&nbsp;b", "a b", and "a\nb" as identical.

### Example 1

__Input__
```plaintext
# User input:
Мама мыла РАМУ
first.txt
second.txt

# Contents of first.txt
В этом файле говорится    о том что МАМА   

мылА
Раму

# Contents of second.txt
А в этом не говорится

```

__Output__
```plaintext
first.txt
```

### Example 2

__Input__
```plaintext
# User input:
Python
only_one_file.txt

# Contents of only_one_file.txt
Тут нет никаких змей

```

__Output__
```plaintext
404. Not Found
```