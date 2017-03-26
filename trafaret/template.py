import re


_TEMPLATE = re.compile(r'____([a-zA-Z0-9]+)')


def todo(text: str) -> str:
    return _TEMPLATE.sub('// TODO', text)
