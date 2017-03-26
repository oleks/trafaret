import pytest
import re

from trafaret import reutil
from trafaret.tokens import OffsetToken
from typing import Iterable, List, Match, Pattern, Tuple, TypeVar  # noqa: F401
from itertools import repeat
from functools import reduce


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


A = TypeVar('A')


# http://stackoverflow.com/a/5656097/5801152
def intersperse(iterable: Iterable[A], delimiter: A) -> Iterable[A]:
    it = iter(iterable)
    yield next(it)
    for x in it:
        yield delimiter
        yield x


def flatten2(iterable: Iterable[Iterable[A]]) -> Iterable[A]:
    return [i for subis in iterable for i in subis]


def offset_tokens(
        tokens: Iterable[str], offset: int = 0
        ) -> Iterable[OffsetToken]:
    init = (0, [])  # type: Tuple[int, List[OffsetToken]]
    return reduce(
        lambda x, y: (x[0] + len(y) + offset, x[1] + [OffsetToken(x[0], y)]),
        tokens, init)[1]


def test_whitespace_split(words: Pattern) -> None:
    tokens = ['a', 'b', 'c', 'd']

    delimeter = ' '
    expected = offset_tokens(tokens, len(delimeter))

    tokens = list(flatten2(zip(tokens, repeat(delimeter))))
    text = ''.join(tokens)

    actual = reutil.split_tokens(
        text, words,
        match_transform, text_transform)

    assert actual == expected


def test_operator_split(words: Pattern) -> None:
    tokens = ['a', 'b', 'c', 'd']
    tokens = list(flatten2(zip(tokens, repeat('+'))))
    text = ''.join(tokens)

    expected = offset_tokens(tokens)
    actual = reutil.split_tokens(
        text, words,
        match_transform, text_transform)

    assert actual == expected
