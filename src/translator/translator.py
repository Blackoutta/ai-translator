import os

from exception.meta import EnumNotSupportedException
from model.openai_model import *
from translatable.pdf.pdf import PDFTranslatable
from translatable.plain_text import PlainTextTranslatable
from translatable.meta import Translatable
from translator.examples import *
from translator.meta import *
from translator.meta import TransRequest


def _parse_style_desc(request: TransRequest) -> list[str]:
    if request.style == Style.CUSTOM:
        return [style_desc_dict["global"].format(request.src, request.target), request.custom_style.desc]

    style_desc = [style_desc_dict["global"].format(request.src, request.target), style_desc_dict[request.style.value]]
    return style_desc


def _parse_examples(request: TransRequest) -> list[str]:
    if request.style == Style.CUSTOM:
        return request.custom_style.examples

    examples = ["Let me give you some translation example(s).",
                "Suppose We are translating this English sentence to Chinese: " + example_text,
                "by using the '{}' style, your translation may look like this: {}".format(request.style.value,
                                                                                          example_dict[
                                                                                              request.style.value])
                ]
    return examples


def _parse_translatable(request: TransRequest, model: Model) -> Translatable:
    if request.trans_type == TransType.TEXT:
        return PlainTextTranslatable(model, request.text_content)
    if request.trans_type == TransType.DOC:
        if request.file_type == 'text/plain':
            return PlainTextTranslatable(model, request.doc_content.decode('utf-8'))
        if request.file_type == 'application/pdf':
            return PDFTranslatable(model, request.doc_content)
    raise EnumNotSupportedException("trans_type: {}, content_type: {}".format(request.trans_type, request.file_type))


def _parse_temperature(request: TransRequest) -> float:
    return style_temp_dict[request.style.value]


class TranslatorV1(Translator):
    def __init__(self):
        super().__init__()

    def translate(self, request: TransRequest) -> Tuple[Optional[TransResponse], Optional[str]]:
        style_desc = _parse_style_desc(request)
        examples = _parse_examples(request)
        temperature = _parse_temperature(request)

        model = OpenAIModel(
            src=request.src,
            target=request.target,
            style_desc=style_desc,
            examples=examples,
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL"),
            model=request.model,
            temperature=temperature
        )

        translatable = _parse_translatable(request, model)

        err = translatable.translate()
        if err is not None:
            return None, err

        resp = TransResponse(translatable.get_text(), translatable.get_bytes())
        return resp, None
