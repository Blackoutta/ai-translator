from model.meta import Model
from openai import OpenAI


class OpenAIModel(Model):
    def __init__(self,
                 src: str,
                 target: str,
                 style_desc: list[str],
                 examples: list[str],
                 api_key: str,
                 base_url: str,
                 model: str,
                 temperature: float = 1.0,
                 ):
        super().__init__(src, target, style_desc, examples)
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.model = model
        self.temperature = temperature

    def translate(self, content: str) -> str:
        messages = []
        for desc in self.style_desc:
            messages.append(
                {"role": "system", "content": desc}
            )

        for example in self.examples:
            messages.append(
                {"role": "system", "content": example}
            )

        messages.append(
            {"role": "user", "content": "translate the following content from {} to {}: {}".format(self.src, self.target, content)}
        )

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
        )
        translation = response.choices[0].message.content.strip()
        return translation
