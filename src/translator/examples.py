style_desc_dict = {
    "global": "You are a professional {} to {} translator. You'll keep the layout and symbols of the given text as it is.",
    "formal": "You will translate the content in a very classic, poetic and elegant way. Be as short as possible.",
    "normal": "You will translate the content without any specific tone.",
    "relaxed": "You will translate the content in a humorous, lively and easy-to-understand way.",
}

style_temp_dict = {
    "formal": 0.8,
    "normal": 0.2,
    "relaxed": 1.2

}

example_text = "The wind whispered secrets through the trees."

example_dict = {
    "formal": "风自树间低语，隐晦信息亦由之传。",
    "normal": "风在树间低语着秘密。",
    "relaxed": "风在树叶间窃窃私语，好像有什么神秘的事情要说哦~"
}
