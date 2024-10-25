from app.hello import main, get_greeting


def test_get_greeting():
    """Test that get_greeting returns the expected message"""
    assert get_greeting() == "Hello from rest-api-django!"


def test_main_output(capsys):
    """Test that main() prints the expected greeting message"""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from rest-api-django!\n"


def test_main_no_return_value():
    """Test that main() returns None"""
    assert main() is None
