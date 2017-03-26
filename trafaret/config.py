import yaml

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
