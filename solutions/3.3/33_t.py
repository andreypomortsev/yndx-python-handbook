{
    tuple(sorted([first_word, second_word]))
    for i, first_word in enumerate(text.split())
    for second_word in text.split()[i + 1 :]
    if len(set(first_word) & set(second_word)) > 2
}
