import requests
import json
import random

# define OpenAI API url
url = "https://api.openai.com/v1/engines/davinci-codex/completions"

# define OpenAI API key
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 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"
}

culprit_info = None

def getAlibi(name):
    locations = ["방1", "방2", "거실", "화장실"]
    location = random.choice(locations)
    data = {
        "prompt": f"{name}이(가) 범행 당시 {location}에 있었는지와 무엇을 하고 있었는지 설명해줘",
        "max_tokens": 60
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    alibi = response.json()['choices'][0]['text'].strip()
    print(f"{name}의 알리바이: {alibi}")

def getDetail(story):
    summary = input("사건 요약을 입력해주세요: ")
    data = {
        "prompt": f"사건 요약: {summary}",
        "max_tokens": 200
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    Detail = response.json()['choices'][0]['text'].strip()
    print(Detail)
    for i in range(6):
        name = input(f"용의자 {i+1}의 이름을 입력해주세요: ")
        getAlibi(name)

def getSetting():
    global culprit_info
    suspect = input("용의자의 이름을 입력해주세요: ")
    weapon = input("범행 도구를 입력해주세요: ")
    subject = random.choice(["병원", "별장", "회사"])
    data = {
        "prompt": f"주제: {subject}, 용의자: {suspect}, 범행 도구: {weapon}",
        "max_tokens": 200
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    Setting = response.json()['choices'][0]['text'].strip()
    culprit_info = Setting
    getDetail(Setting)

getSetting()