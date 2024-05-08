from translator.translator import TranslatorV1
from translator.meta import TransRequest, TransType, Style

translator = TranslatorV1()

req = TransRequest(
    src="Chinese",
    target="English",
    trans_type=TransType.DOC,
    doc_content="床前明月光，疑似地上霜。举头望明月，低头思故乡。".encode(),
    file_type='text/plain',
    style=Style.FORMAL  # 可选风格: FORMAL, NORMAL, RELAXED
)

resp = translator.translate(req)
print(resp.text)
