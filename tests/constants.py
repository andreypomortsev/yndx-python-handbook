MEMORY_LIMIT = 64  # RAM в MB
TIME_LIMIT = 1  # Временной лимит в сек

TEST_FILE_NAMES = {
    "3.5": {
        "f": ("cyrillic.txt", "transliteration.txt"),
        "o": "scoring.json",
        "q": "secret.txt",
        "s": ("public.txt", "private.txt"),
        "t": "numbers.num",
    },
}

TEST_FUNCTION_NAMES = {
    "4.1": {
        "a": "print_hello",
        "b": "gcd",
        "c": "number_length",
        "d": "month",
        "e": "split_numbers",
        "f": "modern_print",
        "g": "can_eat",
        "h": "is_palindrome",
        "i": "is_prime",
        "j": "merge",
    }
}
