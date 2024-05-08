# AI翻译助手

## 特色

- 多语言支持: 各种语言之间互相翻译
- 多风格选择：可以翻译为各种不同的风格
- 即时翻译：在页面上输入文本后即刻翻译
- 文档翻译：上传文档后对文档整体进行翻译，目前支持：.txt, .pdf

## 功能预览

### 支持即时翻译和文档翻译
![switch](switch.gif)

### 即时翻译

![pv1](pv_1.gif)

### 文档翻译

![img.png](pv_2.png)

#### 翻译前
![img.png](doc_before.png)

#### 翻译后
![img.png](doc_after.png)

## 快速开始

下载源码:

```
git clone https://github.com/Blackoutta/ai-translator.git
```

进入源码根目录:

```
cd ai-translator
```

安装依赖

```
pip install -r requirements.txt
```

设置API KEY和BASE URL
```
export OPENAI_API_KEY=your_api_key
export OPENAI_BASE_URL=your_base_url
```

用python运行应用:

```
python ./src/app.py
```

使用浏览器访问以下url

```
http://127.0.0.1:5000/
```