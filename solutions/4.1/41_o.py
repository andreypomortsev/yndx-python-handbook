def get_dict(text: str) -> dict:
    result = {}

    for token in text.split(";"):
        key, value = token.split("=")
        stripped_value = value.lstrip("-")
        if stripped_value.isdigit():
            value = int(value)
        elif (
            value.count(".") == 1 and stripped_value.replace(".", "").isdigit()
        ):
            value = float(value)

        result[key] = value

    return result
