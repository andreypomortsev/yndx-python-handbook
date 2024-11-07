{
    char: text.lower().count(char)  # noqa F821
    for char in text.lower()  # noqa F821
    if char.isalpha()
}
