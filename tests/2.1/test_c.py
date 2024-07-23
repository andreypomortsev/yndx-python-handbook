from io import StringIO


def test_first_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("2 + 2 = 4")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "2 + 2 = 4\n2 + 2 = 4\n2 + 2 = 4"

    assert printed_output == expected_output


def test_second_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("2 * 2 = 4")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "2 * 2 = 4\n2 * 2 = 4\n2 * 2 = 4"

    assert printed_output == expected_output


def test_whitespace_input(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO(" ")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue()
    expected_output = " \n \n \n"

    assert printed_output == expected_output


def test_print_empty_input(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("\n")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip("\n")
    expected_output = ""

    assert printed_output == expected_output
