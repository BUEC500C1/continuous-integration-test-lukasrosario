from converter import format_question


def test_format():
    assert format_question(" hello") == "hello"
