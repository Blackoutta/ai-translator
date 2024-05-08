style_desc_dict = {
    "global": "You are a professional {} to {} translator. You'll keep the layout and symbols of the given text as it is.",
    "formal": "You will translate the content in a very formal, elegant and explict tone. Be short too.",
    "normal": "You will translate the content without any specific tone.",
    "relaxed": "You will translate the content in a relaxed, poetic, lively and easy-to-understand tone, it's ok to to be inaccurate.",
}

style_temp_dict = {
    "formal": 0.2,
    "normal": 1,
    "relaxed": 1.2

}

example_text = "To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, Or to take arms against a sea of troublesAnd by opposing end them?"

example_dict = {
    "formal": "存乎一心，亡乎一念，乃是疑问：是忍受命运的风浪和荆棘，抑或挺身对抗波涛汹涌的难题，以抗衡而终结之？",
    "normal": "生存还是毁灭，这是个问题：是忍受命运的狠心打击，还是用武器反抗滔滔难题，从而终结之？",
    "relaxed": "是活下去呢，还是放弃呢，这是个问题：是忍受生活的不幸，还是拿起武器对抗麻烦重重的浪潮，从而结束它们呢？"
}
