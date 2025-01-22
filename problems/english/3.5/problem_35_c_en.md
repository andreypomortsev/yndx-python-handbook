## [No comments 2.0](../../../solutions/3.5/35_c.py)

As you remember, when you comment your code, the interpreter removes the comments before execution.\
Write a program that performs this function for the interpreter.

### Input Format

Lines of the program are entered.

### Output Format:

Each line should be cleared of comments.\
If the comment is the entire line, it should not be printed.

### Example 1

__Input__
```plaintext
# My first super-duper program
print("What is your name?") #  What is your name?
name = input() #  Save the name
print(f"Hello, {name}!") #  Greet# End of my super-duper program
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
for i in range(10): # Counting to 10
    print(i) # printing the number
```

__Output__
```plaintext
for i in range(10):
    print(i)
```

### [Approach](../3.1/problem_31_i_en.md#solution-approach)