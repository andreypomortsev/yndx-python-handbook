## [Class Point 3.0](../../../solutions/5.2/52_a.py)

Let's extend the functionality of the class you wrote in the task "[Class Point 2.0](../5.1/problem_51_b_en.md)."

Create a class `PatchedPoint` — a subclass of the `Point` class you previously wrote.

You need to implement the following types of initialization for the new class:

- No parameters — the coordinates of the point are set to 0;
- One parameter — a tuple with the coordinates of the point;
- Two parameters — the coordinates of the point.

### Note

Your solution should contain only classes and functions.\
The solution should not contain calls to initialize the required classes.

### Example 1

__Input__
```python
point = PatchedPoint()
print(point.x, point.y)
point.move(2, -3)
print(point.x, point.y)
```

__Output__
```plaintext
0 0
2 -3
```

### Example 2

__Input__
```python
first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))
```

__Output__
```plaintext
16.76
16.76
```