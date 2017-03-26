import pytest
import re

from trafaret import reutil
from trafaret.tokens import OffsetToken
from typing import Pattern


@pytest.fixture(scope='session')
def words() -> Pattern:
    return re.compile(r'(\W)')


def test_reutil(words: Pattern) -> None:
    expected = [
            OffsetToken(0, 'a'),
            OffsetToken(2, 'b'),
            OffsetToken(4, 'c'),
            OffsetToken(6, 'd')
        ]
    text = " ".join(map(lambda t: t.text, expected))  # type: str
    actual = reutil.split_tokens(
        text, words,
        lambda m: [m for m in [m] if reutil.not_whitespace(m)],
        lambda i, t: [OffsetToken(i, t)])

    assert actual == expected
