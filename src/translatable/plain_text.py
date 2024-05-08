from model.meta import Model
from translatable.meta import Translatable


class PlainTextTranslatable(Translatable):
    def __init__(self, model: Model, text: str):
        super().__init__(model)
        self.original = text
        self.translated = None

    def translate(self):
        self.translated = self.model.translate(self.original)

    def get_bytes(self) -> bytes:
        return self.translated.encode('utf-8')

    def get_text(self) -> str:
        return self.translated
