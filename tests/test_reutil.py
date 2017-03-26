import pytest
import re

from trafaret import reutil
from trafaret.tokens import OffsetToken
from typing import List, Match, Pattern


@pytest.fixture(scope='session')
def words() -> Pattern:
    return re.compile(r'(\W)')


def text_transform(offset: int, text: str) -> List[OffsetToken]:
    return [OffsetToken(offset, text)]


def match_transform(m: Match) -> List[OffsetToken]:
    if reutil.not_whitespace(m):
        return text_transform(m.start(0), m.group(0))
    else:
        return []


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
        match_transform, text_transform)

    assert actual == expected
