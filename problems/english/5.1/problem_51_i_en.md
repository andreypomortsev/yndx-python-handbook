## [Queue](../../../solutions/5.1/51_i.py)

In programming, there is a need for more than just the collections we have studied. One such collection is a queue. It follows the "First In, First Out" principle for data storage.

Implement the `Queue` class, which has no initialization parameters but supports the following methods:

- `push(item)` — adds an element to the end of the queue;
- `pop()` — removes the first element from the queue;
- `is_empty()` — checks if the queue is empty.

### Note

Your solution should contain only classes and functions.\
The solution should not contain calls to initialize the required classes.

### Example 1

__Input__
```python
queue = Queue()
for item in range(10):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop(), end=" ")
```

__Output__
```plaintext
0 1 2 3 4 5 6 7 8 9 
```

### Example 2

__Input__
```python
queue = Queue()
for item in ("Hello,", "world!"):
    queue.push(item)
while not queue.is_empty():
    print(queue.pop())
```

__Output__
```plaintext
Hello,
world!
```