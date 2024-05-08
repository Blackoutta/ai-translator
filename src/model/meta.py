from abc import ABC, abstractmethod
from typing import Tuple, Optional


class Model(ABC):
    def __init__(self, src: str, target: str, style_desc: list[str], examples: list[str]):
        self.src = src
        self.target = target
        self.style_desc = style_desc
        self.examples = examples

    @abstractmethod
    def translate(self, content: str) -> Tuple[str, Optional[str]]:
        pass
