import re

from trafaret.config import Config
from trafaret.template import Templates
from typing import Iterable, Match

_INDENTED_SUBCODE = re.compile(
    r'^([ \t]*)(.*?)____([A-Za-z][A-Za-z0-9]*).*$',
    re.MULTILINE)


def indented_replace(m: Match, code: str) -> str:
    lines = code.split('\n')
    indent = m.group(1).strip('\n')

    retlines = []
    if len(lines) > 0:
        retlines.append(lines[0])
        indent = " " * len(indent)
        for line in lines[1:]:
            retlines.append(indent + line)
    return '\n'.join(retlines)


def replace_yield(m: Match, code: str, ts: Templates) -> Iterable[str]:
    for t in ts[m.group(3)]:
        start = m.end(2)
        end = m.end(3)
        for tail in replace(code[end:], ts):
            tcode = '\n\n'.join(t.code)
            for head in replace(tcode, ts):
                head = indented_replace(m, head)
                yield code[:start] + head + tail


def replace(code: str, ts: Templates) -> Iterable[str]:
    m = _INDENTED_SUBCODE.search(code)
    if not m:
        return [code]
    else:
        return replace_yield(m, code, ts)


def iter_solutions(config: Config) -> Iterable[str]:
    handout = config.raw_handout()
    ts = config.templates()
    return replace(handout, ts)
