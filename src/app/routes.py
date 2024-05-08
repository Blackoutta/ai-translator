from flask import Flask, request, render_template, send_file
from io import BytesIO

from translator.meta import TransRequest, TransType, Style
from translator.translator import TranslatorV1

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('trans_doc.html')


@app.route('/translate_doc', methods=['POST'])
def translate_doc():
    # 处理请求
    form = request.form
    print(form)
    style = Style(form.get("style"))

    f = request.files['file']
    file_type = f.content_type
    file_data = f.read()
    file_name = f.filename

    req = TransRequest(
        src=form.get("src"),
        target=form.get("target"),
        trans_type=TransType.DOC,
        doc_content=file_data,
        file_type=file_type,
        style=style  # 可选风格: FORMAL, NORMAL, RELAXED
    )

    translator = TranslatorV1()
    resp = translator.translate(req)
    file_object = BytesIO(resp.bs)
    return send_file(file_object, as_attachment=True, mimetype=file_type, download_name='translated_' + file_name)


@app.route('/translate_text', methods=['POST'])
def translate_text():
    # 处理请求
    form = request.form
    print(request.content_type)
    print(form)
    original = form.get("text_content")
    style = Style(form.get("style"))

    req = TransRequest(
        src=form.get("src"),
        target=form.get("target"),
        trans_type=TransType.TEXT,
        text_content=original,
        style=style  # 可选风格: FORMAL, NORMAL, RELAXED
    )

    translator = TranslatorV1()
    resp = translator.translate(req)
    translated = resp.text

    return render_template('trans_text.html',
                           translated=translated,
                           original=original,
                           style=style
                           )


if __name__ == '__main__':
    app.run(debug=True)
