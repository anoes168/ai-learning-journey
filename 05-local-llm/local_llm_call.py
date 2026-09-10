import json
from openai import OpenAI


def main():
    client = OpenAI(
        base_url = "http://127.0.0.1:8080/v1",
        api_key = "local",
    )

    model_id = client.models.list().data[0].id

    response = client.chat.completions.create(
        model = model_id,
        messages = [
            {
                "role":"system",
                "content": (
                    "你是分类器。"
                    "只输出JSON.label只能是0或1."
                    "0便是non-irony，1表示irony"
                ),
            },
            {
                "role":"user",
                "content":(
                    "判断下面文本是否具有讽刺性："
                    "I love my family."
                    "返回字段：label、confidence、evidence。"
                ),

            },
        ],
        temperature = 0,
        max_tokens = 128,
        response_format = {"type":"json_object"},
        extra_body = {
            "chat_template_kwargs":{
                "enable_thinking" : False
            }
        },
    )

    message = response.choices[0].message
    content = message.content

    result = json.loads(content)

    print(result)
    print(result["label"])


if __name__ == "__main__":
    main()
