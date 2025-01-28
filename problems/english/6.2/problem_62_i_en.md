## [Endless Battleship](../../../solutions/6.2/62_i.py)

Imagine a battleship field with no boundaries. For simplicity, the coordinates of shots will be denoted as integer coordinates on the plane.

An infinite field generates a large amount of data that needs to be analyzed. One of the players asks you to write a program that trims the data to a limited rectangle.

### Input Format

The first line contains two numbers — the coordinates of the top-left corner. The second line contains the bottom-right corner.

The dataset with the coordinates of all the opponent's shots is located in the `data.csv` file.

### Output Format

The part of the dataset limited by the specified rectangle.

### Note

You can download the dataset from the example [here](../../../tests/data/test_data_62_i.csv).

### Example

__Input__
```plaintext
0 10
10 0
```

__Output__
```plaintext
         x   y
6262     9   0
59060   10   4
69882   10   5
72739    0   0
120951   3   1
137931   9  10
183595   7   0
194157   0   9
219910   0   3
220920  10   0
242318   8   4
283651   1   8
292990   4   3
294474   6   3
352959  10  10
393223   3   5
423449   1   2
```