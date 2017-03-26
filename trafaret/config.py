import yaml

from html import escape
from trafaret.template import todo
from typing import Dict, IO

YamlType = Dict[str, str]


class Config:
    def __init__(self, config: YamlType) -> None:
        self.config = config

    @staticmethod
    def load(f: IO[str]) -> 'Config':
        return Config(yaml.safe_load(f))

    def text(self) -> str:
        return self.config['text'].strip()

    def raw_handout(self) -> str:
        return self.config['handout'].strip()

    def handout(self) -> str:
        html_format = "<div id='code'><pre id='editor'>{}</pre></div>"
        html = escape(todo(self.raw_handout()))
        return html_format.format(html)
