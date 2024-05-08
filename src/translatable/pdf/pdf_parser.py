from io import BytesIO

import pdfplumber
from typing import Optional

from translatable.pdf import Book, Page, Content, ContentType, TableContent


class PDFParser:
    def __init__(self):
        pass

    def parse_pdf(self, pdf_bs: bytes, pages: Optional[int] = None) -> Book:
        book = Book()

        with pdfplumber.open(BytesIO(pdf_bs)) as pdf:
            if pages is not None and pages > len(pdf.pages):
                raise ValueError(len(pdf.pages), pages)

            if pages is None:
                pages_to_parse = pdf.pages
            else:
                pages_to_parse = pdf.pages[:pages]

            for pdf_page in pages_to_parse:
                page = Page()

                # Store the original text content
                raw_text = pdf_page.extract_text()
                tables = pdf_page.extract_tables()

                # Remove each cell's content from the original text
                for table_data in tables:
                    for row in table_data:
                        for cell in row:
                            raw_text = raw_text.replace(cell, "", 1)

                # Handling text
                if raw_text:
                    # Remove empty lines and leading/trailing whitespaces
                    raw_text_lines = raw_text.splitlines()
                    cleaned_raw_text_lines = [line.strip() for line in raw_text_lines if line.strip()]
                    cleaned_raw_text = "\n".join(cleaned_raw_text_lines)

                    text_content = Content(content_type=ContentType.TEXT, original=cleaned_raw_text)
                    page.add_content(text_content)

                # Handling tables
                if tables:
                    for table in tables:
                        tc = TableContent(table)
                        page.add_content(tc)

                book.add_page(page)

        return book
