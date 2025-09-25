# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI
URI="https://api.deepseek.com"
API_KEY="sk-4f6149105c2042d2b3d15ee6ce9cf35d"
class DeepSeekBot:
    client=OpenAI(api_key=API_KEY,base_url=URI)
    def __init__(self,model="deepseek-chat"):
        self.model=model
        pass

    def
    # client = OpenAI(api_key=API_KEY, base_url=URI)

    response = client.chat.completions.create(
        model=self.model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=False
    )

    print(response.choices[0].message.content)