from typing import Tuple, Optional

import openai

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

    def translate(self, content: str) -> Tuple[str, Optional[str]]:
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
            {"role": "user",
             "content": "translate the following content from {} to {}: {}".format(self.src, self.target, content)}
        )
        for msg in messages:
            print(msg)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
            )

            translation = response.choices[0].message.content.strip()
            return translation, None
        except openai.RateLimitError as e:
            print(e)
            return "", "API用量被限制。"
        except openai.APIConnectionError as e:
            print(e)
            return "", "发生API连接问题, 请重试。"
        except openai.APIStatusError as e:
            print(e)
            return "", "API调用返回错误: {}".format(e.message)
        except Exception as e:
            print(e)
            return "", "发生未知错误"
