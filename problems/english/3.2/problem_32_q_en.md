## [Friends of Friends](../../../solutions/3.2/32_q.py)

The Six Degrees of Separation theory is a sociological theory that any two people on Earth are separated by no more than five levels of common acquaintances (and thus, six levels of connections). The formal mathematical formulation of the theory is: the diameter of the social graph does not exceed 6. We will not dive deeply into the intricacies of friendships and will stick to just two levels for now. Write a program that, given a list of friendship pairs, determines the list of "second-level friends" for each person.

### Input format

Each line contains two names.\
The input ends with an empty line.

### Output format:

Print the list of all people and their "second-level friends" in the format "Person: Friend1, Friend2, ...".\
The list of people and friends should be printed in alphabetical order without repetitions.

### Example 1

__Input__
```plaintext
Иванов Петров
Иванов Сергеев
Васильев Петров
Сергеев Яковлев
Петров Кириллов
Петров Яковлев
```

__Output__
```plaintext
Васильев: Иванов, Кириллов, Яковлев
Иванов: Васильев, Кириллов, Яковлев
Кириллов: Васильев, Иванов, Яковлев
Петров: Сергеев
Сергеев: Петров
Яковлев: Васильев, Иванов, Кириллов
```

### Example 2

__Input__
```plaintext
Николай Фёдор
Николай Женя
Фёдор Женя
Фёдор Илья
Илья Фёдор
```

__Output__
```plaintext
Женя: Илья
Илья: Женя, Николай
Николай: Илья
Фёдор: 
```

## Approach to Solution

### Explanation of Graph Theory

A graph is a structure consisting of nodes (vertices) and edges (connections). In this task:
- Nodes represent people.
- Edges represent "friendship" relations.
- Second-level friends are at a distance of 2 edges from the current node.

__1. Building the Friendship Graph:__
   - Use `defaultdict` from the `collections` module to store the list of friends. 
   - Each input line adds a pair of friends, creating a bidirectional connection between two names.

__2. Graph Traversal to Find Second-Level Friends:__
   - For each person, take their first-level friends.
   - For each of these friends, add their friends to the final list of second-level friends.
   - Exclude the person and their first-level friends from the result.

__3. Sorting and Output:__
   - Print each person and their second-level friends in alphabetical order.

### Example Graph and Steps

#### Let's break down Example 1:

- The graph is represented as:
    ```python
    friends = {
        'Иванов': {'Петров', 'Сергеев'},
        'Петров': {'Иванов', 'Кириллов', 'Яковлев', 'Васильев'},
        'Сергеев': {'Иванов', 'Яковлев'},
        'Яковлев': {'Петров', 'Сергеев'},
        'Кириллов': {'Петров'},
        'Васильев': {'Петров'}
    }
    ```

- For each person, we intersect their friends' friends, taking exclusions into account.
    - __For "Иванов":__
    - Friends: `{'Петров', 'Сергеев'}`.
    - Friends of their friends:
        - "Петров": `{'Иванов', 'Кириллов', 'Яковлев', 'Васильев'}`.
        - "Сергеев": `{'Иванов', 'Яковлев'}`.
    - Result: `{'Кириллов', 'Яковлев', 'Васильев'}`.

- Sort the people and their second-level friends. Output:
    ```plaintext
    Васильев: Иванов, Кириллов, Яковлев
    Иванов: Васильев, Кириллов, Яковлев
    Кириллов: Васильев, Иванов, Яковлев
    Петров: Сергеев
    Сергеев: Петров
    Яковлев: Васильев, Иванов, Кириллов
    ```