translator = str.maketrans("", "", " ")
word = input().translate(translator).lower()

n = len(word)
mid = n // 2

mid_odd = mid + n % 2
is_poli = word[:mid] == word[mid_odd:][::-1]

if is_poli:
    print("YES")
else:
    print("NO")
