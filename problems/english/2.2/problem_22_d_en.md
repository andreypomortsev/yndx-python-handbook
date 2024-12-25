## [List of Winners](../../../solutions/2.2/22_d.py)

The length of the race is *43872 meters*, and the spectators want to know the name of the winner.

We know the average speeds of three favorites — Петя, Вася, and Толя. Help summarize the results of the race.

### Input format

The first line contains Петя's average speed.
The second line contains Вася's average speed.
The third line contains Толя's average speed.

### Output format:

The names of the winners in the order of their finishing positions.

### Example 1

**Input**
```plaintext
10
5
7
```

**Output**
```plaintext
1. Петя
2. Толя
3. Вася
```

### Example 2

**Input**
```plaintext
5
7
10
```

**Output**
```plaintext
1. Толя
2. Вася
3. Петя
```

## Solution

The simplest way is to [sort](https://ru.wikipedia.org/wiki/%D0%90%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC_%D1%81%D0%BE%D1%80%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B8) the speed values and names at the same time, swapping the values. Let's define the names as:

- $N_1$ - Петя; 
- $N_2$ - Вася; 
- $N_3$ - Толя.

and their corresponding speeds as $S_1$, $S_2$, $S_3$.

#### For sorting three elements, we will need 3 comparisons:

If $S_1 < S_2$: we swap the speed values and simultaneously swap the name variables.

$S_1$, $S_2$ = $S_2$, $S_1$ — now $S_1 > S_2$;

$N_1$, $N_2$ = $N_2$, $N_1$ — now $N_1$ is not Петя, but Вася.

Following the same principle, we compare $S_1 < S_3$ and $S_2 < S_3$. 

After all comparisons, the largest speed will be in the variable $S_1$, the name of the winner will be in $N_1$, the second place name will be in $N_2$, and the last place name will be in $N_3$.