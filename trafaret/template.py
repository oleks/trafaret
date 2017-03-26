import re

from typing import Any, Dict, List


TemplateRegex = r'____([a-zA-Z0-9]+)'

_TEMPLATE = re.compile(TemplateRegex)


def todo(text: str) -> str:
    return _TEMPLATE.sub('// TODO', text)


YamlTemplate = Dict[str, Any]


class Template:
    def __init__(
            self, kind: str,
            code: List[str],
            explanation: str = ""
            ) -> None:
        self.kind = kind
        self.code = [c.rstrip() for c in code]
        self.explanation = explanation.strip()

    @staticmethod
    def load(data: YamlTemplate) -> 'Template':
        return Template(**data)


Templates = Dict[str, List[Template]]


def load_templates(data: List[YamlTemplate]) -> Templates:
    retval = {str(d['kind']): [] for d in data} \
        # type: Dict[str, List[Template]]
    for d in data:
        kind = str(d['kind'])
        t = Template.load(d)
        retval[kind].append(t)
    return retval
