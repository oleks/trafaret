import re


class Lang:
    def __init__(self) -> None:
        pass

    def is_string(self, text: str) -> bool:
        return False

    @staticmethod
    def load(lang: str) -> 'Lang':
        if lang == 'csharp':
            return CSharp()
        elif lang == 'python3':
            return Python3()
        else:
            raise ValueError("{} is not a known language".format(lang))


class CSharp(Lang):
    def __init__(self) -> None:
        self.todo_comment = "// TODO"
        self.comment = re.compile(
            r'/\*.*?\*/|//.*?\n')
        self.string = re.compile(
            r'"([^\\]|\\[\\"])*?"')


class Python3(Lang):
    def __init__(self) -> None:
        self.todo_comment = "# TODO"
        self.comment = re.compile(
            r'#.*?\n')
        self.string = re.compile(
            r'"([^\\]|\\[\\"])*?"|\'([^\\]|\\[\\\'])*?\'')
