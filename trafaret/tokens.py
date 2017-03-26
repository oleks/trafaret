from typing import Any


class OffsetToken:
    def __init__(self, offset: int, text: str) -> None:
        self.offset = offset
        self.text = text

    def __repr__(self) -> str:
        return "({}: {})".format(self.offset, self.text)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, OffsetToken) and \
            self.offset == other.offset and \
            self.text == other.text
