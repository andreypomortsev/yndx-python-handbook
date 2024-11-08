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
    },
    "4.2": {
        "a": "make_list",
        "b": "make_matrix",
        "c": "gcd",
        "d": "month",
        "e": "to_string",
        "f": "order",
        "j": "secret_replace",
    },
    "4.3": {
        "a": "recursive_sum",
        "b": "recursive_digit_sum",
        "c": "make_equation",
        "j": "make_linear",
    },
}

TEST_DATA_PATHS = {"6.2": {"i": "tests/data/test_data_62_i.csv"}}
TEST_URLS = {"6.3": {"a": "http://127.0.0.1:5000"}}

# ANSI escape codes for colored text
BLUE = "\033[94m"  # Blue text
RED = "\033[91m"  # Red text
RESET = "\033[0m"  # Reset to default text color

TIMEOUT_WARNING = (
    f"\n\n{BLUE}Missing {RESET}'timeout'{BLUE} parameter in requests.\n"
    f"This may cause requests to hang {RED}indefinitely.{BLUE}\n"
    f"Please specify a timeout value.{RESET}\n\n"
)

RECURSION_ERROR = "Функция должна быть реализована при помощи рекурсии."
WRONG_URL_ERROR = "The request was made to the wrong URL or port."
JSON_ERROR = "The parameter was not a valid/right JSON."
