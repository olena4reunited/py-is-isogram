import pytest

from app.main import is_isogram


@pytest.mark.parametrize(
    "word, expected_result",
    [
        ("playgrounds", True),
        ("", True),
        ("uncopyrightable", True),
        ("ambidextrously", True),
        ("look", False),
        ("Adam", False)
    ]
)
def should_return_correct_answer(word: str, expected_result: bool) -> None:
    assert is_isogram(word) == expected_result
