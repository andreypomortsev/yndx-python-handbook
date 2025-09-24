def get_dict(text: str) -> dict:
    result = {}

    for token in text.split(";"):
        key, value = token.split("=")

        if value.lstrip("-").isdigit():
            value = int(value)
        elif (
            value.count(".") == 1
            and value.lstrip("-").replace(".", "").isdigit()
        ):
            value = float(value)

        result[key] = value

    return result
