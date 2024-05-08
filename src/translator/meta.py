from abc import ABC, abstractmethod
from enum import Enum


class Style(Enum):
    FORMAL = 'formal'
    NORMAL = 'normal'
    RELAXED = 'relaxed'
    CUSTOM = 'custom'


class TransType(Enum):
    TEXT = 'text'
    DOC = 'doc'


class CustomStyle:
    def __init__(self, desc: list[str], examples: list[str]):
        self.desc = desc
        self.examples = examples


class TransRequest:
    def __init__(self,
                 src: str,
                 target: str,
                 trans_type: TransType,
                 text_content: str = None,
                 doc_content: bytes = None,
                 file_type: str = None,
                 style: Style = Style.NORMAL,
                 custom_style: CustomStyle = None,
                 model: str = 'gpt-3.5-turbo'
                 ):
        self.src = src
        self.target = target
        self.trans_type = trans_type
        self.text_content = text_content
        self.doc_content = doc_content
        self.file_type = file_type
        self.style = style
        self.custom_style = custom_style
        self.model = model


class TransResponse:
    def __init__(self, text: str, bs: bytes):
        self.text = text
        self.bs = bs


class Translator(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def translate(self, request: TransRequest) -> TransResponse:
        pass
