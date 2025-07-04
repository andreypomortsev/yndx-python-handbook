{
    i
    for i in numbers
    if i > 1 and all(i != j and i % j for j in range(2, int(i**0.5) + 1))
}
