from notopenai import NotOpenAI
import json

API_KEY = "fynBW7aqLlOSdV9wR8ZV"
CLIENT = NotOpenAI(api_key=API_KEY)
def get_response(prompt):
    chat_completion = CLIENT.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="gpt-3.5-turbo", # the GPT model to use
    )
    response_str = chat_completion.choices[0].message.content
    return response_str

if __name__ == '__main__':
    print(get_response("What is the meaning of life"))
