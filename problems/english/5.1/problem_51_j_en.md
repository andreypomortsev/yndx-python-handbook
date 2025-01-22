## [Stack](../../../solutions/5.1/51_j.py)

Another useful collection is a stack, which implements the "Last In, First Out" principle. It is often represented as a stack of cards or a gun magazine, where incoming elements cover those already in the collection.

Implement the `Stack` class, which has no initialization parameters but supports the following methods:

- `push(item)` — adds an element to the end of the stack;
- `pop()` — removes the first element from the stack;
- `is_empty()` — checks if the stack is empty.

### Note

Your solution should contain only classes and functions.\
The solution should not contain calls to initialize the required classes.

### Example 1

__Input__
```python
stack = Stack()
for item in range(10):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop(), end=" ")
```

__Output__
```plaintext
9 8 7 6 5 4 3 2 1 0 
```

### Example 2

__Input__
```python
stack = Stack()
for item in ("Hello,", "world!"):
    stack.push(item)
while not stack.is_empty():
    print(stack.pop())
```

__Output__
```plaintext
world!
Hello,
```