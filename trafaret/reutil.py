from typing import Callable, List, Match, Pattern, TypeVar


A = TypeVar('A')


def not_whitespace(m: Match) -> bool:
    return len(m.group(0).strip()) > 0


def split_tokens(
        text: str, pattern: Pattern,
        match_transform: Callable[[Match], List[A]],
        text_transform: Callable[[int, str], List[A]]) -> List[A]:
    """Tokenize text by splitting it up using the pattern. For each part of the
    text, call text_transform. For each match, call match_transform. Hence, you
    decide whether to include the splitting match in your list of tokens, or
    not.
    """
    start = 0
    retval = []
    for m in pattern.finditer(text):
        end = m.start(0)
        if start < end:
            retval.extend(text_transform(start, text[start:end]))
        retval.extend(match_transform(m))
        start = m.end(0)
    if start < len(text):
        retval.extend(text_transform(start, text[start:]))
    return retval
