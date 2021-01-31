import pytest
from converter import format_question


strings = [" foo ", "?foo?", "\\foo\\", "/foo/", "&foo&", "/ &/ foo &\\// "]
strings_spaces = ["foo bar", "foo   bar"]
strings_both = [
    " foo bar ",
    " foo   bar ",
    "?/foo bar\\&",
    "/ \\/  foo  bar /&",
]


@pytest.mark.parametrize("string", strings)
def test_strip(string):
    assert format_question(string) == "foo"


@pytest.mark.parametrize("string", strings_spaces)
def test_spaces(string):
    assert format_question(string) == "foo+bar"


@pytest.mark.parametrize("string", strings_both)
def test_both(string):
    assert format_question(string) == "foo+bar"
