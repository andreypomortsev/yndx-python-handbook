## [No Comments](../../../solutions/3.1/31_i.py)

We hope you write comments in your code. If you do, the interpreter removes them before executing the code. Write a program that performs this task as the interpreter would.

### Input format

Lines of code are provided.  
The input ends when an empty line is encountered.

### Output format

For each line, remove any comments.  
If the line consists entirely of a comment, it should not be output.

### Example 1

__Input__
```plaintext
# My first super-duper program
print("What is your name?") #  What is your name?
name = input() #  Save the name
print(f"Hello, {name}!") #  Greeting# End of my super-duper program

```

__Output__
```plaintext
print("What is your name?")
name = input()
print(f"Hello, {name}!")
```

### Example 2

__Input__
```plaintext
# My first loop
for i in range(10): # Count to 10
    print(i) # output the number

```

__Output__
```plaintext
for i in range(10):
    print(i)
```

## Solution Approach

The first thing a beginner learning Python might think of is using `str.find("#")` to locate the index of the `#` symbol and remove everything that follows it. If the line starts with `#`, it can simply be skipped. While this approach is "good enough" for simple tasks, it is not correct. 

For example, if we apply this solution to its own code, it would not work properly. Here's an example:

```Python
# Incorrect approach
lines = []
while (line := input()):
    if line.startswith("#"):
        pass
    else:
        index = line.find("#")
        if index > 0:
            lines.append(line[:index])
        else:
            lines.append(line)
print(*lines, sep="\n")
```

__Input__
```plaintext
# Incorrect approach
lines = []
while (line := input()):
    if line.startswith("#"):
        pass
    else:
        index = line.find("#")
        if index > 0:
            lines.append(line[:index])
        else:
            lines.append(line)
print(*lines, sep="\n")
```

__Output__
```plaintext
lines = []
while (line := input()):
    if line.startswith("
        pass
    else:
        index = line.find("
        if index > 0:
            lines.append(line[:index])
        else:
            lines.append(line)
print(*lines, sep="\n")
```

This approach fails to handle cases where comments are inside strings or where `#` appears inside quotes. As a result, part of the code may be incorrectly truncated.

To solve this correctly, it's recommended to use a **stack**. The idea is as follows:

1. Iterate through each character in each line.
2. If the character is `#`:
   - If it’s the first character of the line, the entire line is a comment.
   - If the stack is empty, this means the `#` is not inside a string or comment, so it's the start of a comment after code.
3. If the character is a quote (`"` or `'`):
   - If the stack is not empty and the top of the stack matches the current quote, this means the quote is closing, and we remove it from the stack.
   - If the stack is empty, the quote opens a new string or expression, so we add it to the stack.