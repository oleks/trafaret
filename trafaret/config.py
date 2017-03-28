import yaml

from html import escape
from trafaret.template import todo, Templates, load_templates
from trafaret.lang import Lang
from typing import Any, Dict, IO

YamlConfig = Dict[str, Any]


class Config:
    def __init__(self, config: YamlConfig) -> None:
        self.config = config
        self.lang = Lang.load(self.config['language'].strip())

    @staticmethod
    def load(f: IO[str]) -> 'Config':
        return Config(yaml.safe_load(f))

    def text(self) -> str:
        return self.config['text'].strip()

    def raw_handout(self) -> str:
        return self.config['handout'].strip()

    def todo_handout(self) -> str:
        return todo(self.lang.todo_comment, self.raw_handout())

    def html_handout(self) -> str:
        html_format = "<div id='code'><pre id='editor'>{}</pre></div>"
        html = escape(self.todo_handout())
        return html_format.format(html)

    def templates(self) -> Templates:
        return load_templates(self.config['templates'])
