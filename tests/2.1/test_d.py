from io import StringIO


def test_first_open_test(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("100")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "5"

    assert printed_output == expected_output


def test_tousand(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("1000")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "905"

    assert printed_output == expected_output


def test_without_change(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("95")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().rstrip()
    expected_output = "0"

    assert printed_output == expected_output


def test_million(monkeypatch, setup_environment):
    wrapped_module, _ = setup_environment

    mock_input = StringIO("1000000")
    mock_print = StringIO()
    monkeypatch.setattr("sys.stdin", mock_input)
    monkeypatch.setattr("sys.stdout", mock_print)

    wrapped_module.main()

    printed_output = mock_print.getvalue().strip()
    expected_output = "999905"

    assert printed_output == expected_output
