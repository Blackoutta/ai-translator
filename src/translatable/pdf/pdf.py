from typing import Tuple, Optional

from model.meta import Model
from translatable.meta import Translatable
from translatable.pdf.pdf_parser import PDFParser


class PDFTranslatable(Translatable):
    def __init__(self, model: Model, bs: bytes):
        super().__init__(model)
        self.original = bs
        self.translated = None

    def translate(self) -> Optional[str]:
        # 从原始文件解析出Book抽象
        book = PDFParser().parse_pdf(
            pdf_bs=self.original
        )

        # 对Book中每个Page的每个Content进行翻译
        for page_idx, page in enumerate(book.pages):
            for content_idx, content in enumerate(page.contents):
                translated, err = self.model.translate(content.get_original_as_str())
                if err is not None:
                    return err
                book.pages[page_idx].contents[content_idx].set_translation(translated, True)

        translated_book = book.to_pdf()

        self.translated = translated_book
        return None

    def get_bytes(self) -> bytes:
        return self.translated

    def get_text(self) -> str:
        return ""
