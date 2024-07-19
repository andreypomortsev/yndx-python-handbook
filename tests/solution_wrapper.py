import os


def wrapper(file_name: str) -> None:
    """
    Считывает решение из файла и оборачивает его в main функцию
    для получения информации о покрытии тестов во время тестирования.

    Args:
        file_name (str): имя файла с решением.

    Returns:
        None
    """
    with open(file_name, encoding="UTF-8") as file_in:
        script = file_in.read()

    letter = file_name.split(".py")[-2][-1]
    indented_script = script.replace("\n", "\n    ").rstrip(" ")
    wrapped_script = f"def main():\n    {indented_script}"

    current_dir = os.path.basename(os.path.dirname(__file__))
    file_name = f"wrapped_{letter}.py"
    path_to_save = os.path.join(current_dir, file_name)

    with open(path_to_save, "w", encoding="UTF-8") as file_out:
        file_out.write(wrapped_script)
