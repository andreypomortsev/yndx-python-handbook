translator = str.maketrans("", "", " ")
word = input().translate(translator).lower()

left_index = 0
right_index = len(word) - 1

while left_index < right_index:
    if word[left_index] != word[right_index]:
        print("NO")
        break
    left_index += 1
    right_index -= 1
else:
    print("YES")
