from io import StringIO


def test_first_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("Ann")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "Как Вас зовут?\nПривет, Ann"

    assert printed_output == expected_output


def test_second_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("Bob")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "Как Вас зовут?\nПривет, Bob"

    assert printed_output == expected_output


def test_print_input_bob_lower(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("bob")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "Как Вас зовут?\nПривет, bob"

    assert printed_output == expected_output


def test_print_empty_input(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip("\n")
    expected_output = "Как Вас зовут?\nПривет, "

    assert printed_output == expected_output


def test_print_whitespace_input(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("   ")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip("\n")
    expected_output = "Как Вас зовут?\nПривет,    "

    assert printed_output == expected_output


def test_code_statement(setup_environment):
    _, PATH_TO_TEST_FILE = setup_environment
    with open(PATH_TO_TEST_FILE, encoding="UTF-8") as file:
        lines = file.readlines()
        line = "".join(lines)
        expected_output = {
            'print("Как Вас зовут?")\nprint(f"Привет, {input()}")',
            "print('Как Вас зовут?')\nprint(f'Привет, {input()}')",
            'print("Как Вас зовут?")\nprint(f"Привет, {input()}")\n',
            "print('Как Вас зовут?')\nprint(f'Привет, {input()}')\n",
        }
        assert line in expected_output
