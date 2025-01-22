## [Treasure Map](../../../solutions/3.2/32_r.py)

The pirate map marks $N$ points where treasures are buried. Each point is specified by coordinates ($x_i$, $y_i$). The coordinates are in kilometers. Captain Hook's crew wants to create a route to collect as many treasures as possible. However, there is a restriction: for any two adjacent points on the route ($x_i$, $y_i$) and ($x_j$, $y_j$), the $x_i$ and $x_j$ coordinates can only differ in the last digit, and the $y_i$ and $y_j$ coordinates can also only differ in the last digit. For example, after point (15, 10), they can go to point (18, 16), but they cannot go from point (14, 68) to point (19, 71) because 68 and 71 differ in more than the last digit. Also, they cannot go from point (5, 12) to point (13, 14) because the numbers 5 and 13 differ in the tens place. Given the coordinates, determine the maximum number of points Captain Hook can add to his route.

### Input format

The first line contains the number $N$ $(1 \leq N \leq 10^5)$ — the number of points marked on the treasure map. The next $N$ lines contain pairs of coordinates: $x_i$ and $y_i$ — the coordinates of the $i$-th point. The coordinates are integers no less than zero and no greater than $10^9$. It is guaranteed that there are no duplicate points in the list.

### Output format:

Print one number — the maximum number of points Captain Hook can visit on a route constructed according to the described rules.

### Example 1

__Input__
```plaintext
9
10 18
17 15
25 21
0 21
1 16
25 29
24 24
8 26
10 20
```

__Output__
```plaintext
3
```

### Example 2

__Input__
```plaintext
3
12 113
114 15
16 117
```

__Output__
```plaintext
2
```

### Important

In Yandex tests, there are duplicates, so solutions using sets will not pass.

The solution to the problem must be faster than $O(n^2)$, otherwise the program may receive a **Time Limit Exceeded (TLE)** due to large input data, which can reach $10^5$.

In the case of an algorithm with a time complexity of $O(n^2)$, the number of operations will be approximately $10^{10}$. In Python, this number of operations usually takes longer than one second.

If you don't quite understand what this is about, I recommend watching [this excellent lecture](https://www.youtube.com/live/c67zB3FWLOs?si=yGf2LcpWMoWIz0bb&t=703) for a deeper understanding.