from io import StringIO


def test_print_output(setup_environment, monkeypatch):
    wrapped_module, _ = setup_environment

    mock_print = StringIO()
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "Привет, Яндекс!"

    assert printed_output == expected_output


def test_code_statement(setup_environment):
    _, path_to_test_file = setup_environment

    with open(path_to_test_file, encoding="UTF-8") as file:
        line = file.readline().strip()
        expected_outputs = {
            'print("Привет, Яндекс!")',
            "print('Привет, Яндекс!')",
            'print("Привет, Яндекс!")\n',
            "print('Привет, Яндекс!')\n",
        }
        assert line in expected_outputs
