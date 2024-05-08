import os
from io import BytesIO

from reportlab.lib import pagesizes, colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Table, TableStyle, PageBreak
)

from .content import ContentType
from .page import Page


class Book:
    def __init__(self):
        self.pages = []

    def add_page(self, page: Page):
        self.pages.append(page)

    def to_pdf(self) -> bytes:
        # Register Chinese font
        print(os.getcwd())
        font_path = "./static/simsun.ttc"  # 请将此路径替换为您的字体文件路径
        pdfmetrics.registerFont(TTFont("SimSun", font_path))

        # Create a new ParagraphStyle with the SimSun font
        simsun_style = ParagraphStyle('SimSun', fontName='SimSun', fontSize=12, leading=14)

        buffer = BytesIO()
        # Create a PDF document
        doc = SimpleDocTemplate(buffer, pagesize=pagesizes.letter)
        styles = getSampleStyleSheet()
        stories = []

        # Iterate over the pages and contents
        for page in self.pages:
            for content in page.contents:
                if content.status:
                    if content.content_type == ContentType.TEXT:
                        # Add translated text to the PDF
                        text = content.translation
                        paras = text.split("\n")
                        for para in paras:
                            p = Paragraph(para, simsun_style)
                            stories.append(p)

                    elif content.content_type == ContentType.TABLE:
                        # Add table to the PDF
                        table = content.translation
                        table_style = TableStyle([
                            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                            ('FONTNAME', (0, 0), (-1, 0), 'SimSun'),  # 更改表头字体为 "SimSun"
                            ('FONTSIZE', (0, 0), (-1, 0), 14),
                            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                            ('FONTNAME', (0, 1), (-1, -1), 'SimSun'),  # 更改表格中的字体为 "SimSun"
                            ('GRID', (0, 0), (-1, -1), 1, colors.black)
                        ])
                        pdf_table = Table(table.values.tolist())
                        pdf_table.setStyle(table_style)
                        stories.append(pdf_table)
            # Add a page break after each page except the last one
            if page != self.pages[-1]:
                stories.append(PageBreak())

        # Save the translated book as a new PDF file
        doc.build(stories)

        return buffer.getvalue()
