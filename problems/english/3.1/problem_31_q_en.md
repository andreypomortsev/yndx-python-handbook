## [Racecar 5.0](../../../solutions/3.1/31_q.py)

Once again, let's write a program that determines whether the given string is a palindrome or not.

### Input Format

A string is entered.

### Output Format:

If the entered string is a palindrome, output YES; otherwise, output NO.

### Notes

When checking, ignore case and spaces.

### Example 1

__Input__
```plaintext
А роза упала на лапу Азора
```

__Output__
```plaintext
YES
```

### Example 2

__Input__
```plaintext
Мама мыла раму
```

__Output__
```plaintext
NO
```

## Approach to the Solution
Here's how we approached solving the problem:

1. **Remove spaces and convert the string to lowercase**:  
   First, to simplify the check, we need to remove spaces and make all letters lowercase. We use the method [`str.maketrans`](https://docs.python.org/3/library/stdtypes.html#str.maketrans) to create a translation table that removes spaces, and then apply [`str.translate`](https://docs.python.org/3/library/stdtypes.html#str.translate) to remove them from the string, which is a very efficient and fast method for working with characters. After that, we call `lower()` to disregard case sensitivity. The result is a string that's easy to work with.  

   For example, if the input is:  
   ```
   А роза упала на лапу Азора
   ```
   After processing, it becomes:  
   ```
   арозаупаланалапуазора
   ```

2. **Initialize two pointers**:  
   To check if the string is a palindrome, we place one pointer `left_index` at the start of the string, and the second pointer `right_index` at the end. This is needed to compare the characters from both ends.  

3. **Check the string with a loop**:  
   We run a loop that continues until the pointers cross. Inside the loop, we compare the characters:  
   - If the current characters from both ends are not equal, the string is not a palindrome. In that case, we immediately output "NO" and break the loop.  
   - If the characters are equal, we move both pointers toward the center: increase `left_index` and decrease `right_index`.  

4. **Output the result**:  
   If the loop completes without breaking, the string has passed the check and is a palindrome. Then we output "YES".  

   We use an `else` block after the `while` loop to handle this case, as it runs only if the loop completes entirely.  

   For example:  
   - For the string `арозаупаланалапуазора`, the loop will finish successfully, and we will output "YES".  
   - For the string `мамамылараму`, the loop will break on the mismatch and output "NO".

### Why it works efficiently?

The preprocessing of the string (removing spaces and converting to lowercase) is done in $O(n)$ time, where $n$ is the length of the string. Comparing characters from both ends also takes $O(n)$ time, but the loop only goes through half the string, making it run even faster on average.  
You can eliminate preprocessing and handle case sensitivity and spaces during the comparison, which might be more efficient for input data with fewer spaces.

```python
word = input()

left_index = 0
right_index = len(word) - 1

while left_index < right_index:
    left_char = word[left_index].lower()
    right_char = word[right_index].lower()
    
    if left_char == " ":
        left_index += 1
        continue
    
    if right_char == " ":
        right_index -= 1
        continue
    
    if left_char != right_char:
        print("NO")
        break
    
    left_index += 1
    right_index -= 1

else:
    print("YES")
```