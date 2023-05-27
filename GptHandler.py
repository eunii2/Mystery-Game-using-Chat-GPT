import openai

openai.api_key = "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"

def getRespone(message):
    answer = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    respone = answer.choices[0].message["content"].strip()
    return respone