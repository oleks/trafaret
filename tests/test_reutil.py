import pytest
import re

from trafaret import reutil
from typing import Pattern


@pytest.fixture(scope='session')
def words() -> Pattern:
    return re.compile(r'(\W)')


class Token:
    def __init__(self, offset: int, text: str) -> None:
        self.offset = offset
        self.text = text

    def __repr__(self) -> str:
        return "({}: {})".format(self.offset, self.text)


def test_reutil(words: Pattern) -> None:
    expected = [
            Token(0, 'a'),
            Token(2, 'b'),
            Token(4, 'c'),
            Token(6, 'd')
        ]
    text = " ".join(map(lambda t: t.text, expected))  # type: str
    actual = reutil.split_tokens(
        text, words,
        lambda m: [m for m in [m] if reutil.not_whitespace(m)],
        lambda i, t: [Token(i, t)])

    assert actual == expected
