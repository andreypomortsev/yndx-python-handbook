## [Let's Hype a Little!](../../../solutions/2.3/23_t.py)

Blockchain is a "chain of blocks." It is a method of storing data that is protected from tampering. For example, it is the basis of the cryptocurrency Bitcoin.

A blockchain is indeed a sequence of blocks, and each block contains some useful information. For example, the Bitcoin sequence is a list of transactions over a certain period of time: who, to whom, when, and how much money was transferred. This list is accompanied by a random number and some auxiliary data, including a hash — a number that, according to a specific formula, depends on the rest of the block and the hash of the previous block.

The hash must be smaller than a certain number. The formula used to calculate the hash is arranged in such a way that it is impossible to get a sufficiently small hash except by iterating over different values of the random number. Therefore, if an attacker tries to tamper with the blockchain — for example, insert a block in the middle stating that everyone transferred all their money to them — they will face a problem. They will have to find a new random number not only in the fake block but in all subsequent ones, as the hash of each subsequent block depends on the hash of the previous one.

This requires incredible computational power, so the blockchain is generally protected from such attacks.

Write a program that checks the correctness of the hashes in a model blockchain with a simple hash function. Block $b_n$ with number $n$ contains useful information $m_n$, represented as a natural number, $r_n$ — a random number from 0 to 255, and $h_n$ — the hash (an integer from 0 to 255). The hash of each block is calculated using the formula:

$h_n = 37 × (m_n + r_n + h_{n-1})$ modulo 256,

where for the calculation of the hash of the initial block $h_0$, the hash of the previous block is considered to be zero. Each block is represented by a single number:

$b_n = h_n + r_n × 256 + m_n × 256^2$.

Additionally, it is required that the hash $h_n$ be smaller than 100.

### Input Format

The first line contains a natural number $N$ — the number of blocks. Then, $N$ numbers $b_n$ follow, each on a separate line.

### Output Format

Output the number of the first block with an incorrect hash (either not less than 100 or not matching the computed hash according to the specified formula), or -1 if all hashes in the blockchain are correct. Block numbering starts from zero, so the blocks are numbered from 0 to N-1.

### Example 1

__Input__
```plaintext
5
6122802
14406496
15230209
2541121
1758741
```

__Output__
```plaintext
-1
```

### Example 2

__Input__
```plaintext
5
1865535
13479687
16689153
1839958
5214020
```

__Output__
```plaintext
3
```