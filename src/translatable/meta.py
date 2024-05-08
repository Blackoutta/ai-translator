from abc import ABC, abstractmethod
from model.meta import Model


class Translatable(ABC):
    def __init__(self, model: Model):
        self.model = model

    @abstractmethod
    def translate(self):
        pass

    @abstractmethod
    def get_bytes(self) -> bytes:
        pass

    @abstractmethod
    def get_text(self) -> str:
        pass
