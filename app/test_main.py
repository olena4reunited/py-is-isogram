import pytest

from app.main import is_isogram


def should_return_true_when_playgrounds():
    assert is_isogram("playgrounds") == True


def should_return_true_when_empty_string():
    assert is_isogram("") == True


def should_return_true_when_isogram():
    assert is_isogram("uncopyrightable") == True


def should_return_false_when_letters_repeat():
    assert is_isogram("look") == False


def should_return_false_ignoring_the_case():
    assert is_isogram("Adam") == False


def test_should_raise_attribute_error() -> None:
    with pytest.raises(AttributeError):
        is_isogram(123)
