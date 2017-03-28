import re


class Lang:
    def __init__(self) -> None:
        pass

    def is_string(self, text: str) -> bool:
        return False


class CSharp(Lang):
    def __init__(self) -> None:
        self.comment = re.compile(
            r'/\*.*?\*/|//.*?\n')
        self.string = re.compile(
            r'"([^\\]|\\[\\"])*?"')


class Python3(Lang):
    def __init__(self) -> None:
        self.comment = re.compile(
            r'#.*?\n')
        self.string = re.compile(
            r'"([^\\]|\\[\\"])*?"|\'([^\\]|\\[\\\'])*?\'')

