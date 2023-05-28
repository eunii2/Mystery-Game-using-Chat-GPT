import openai
import random

openai.api_key = "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"

def getRespone(message):
    answer = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    respone = answer.choices[0].message["content"].strip()
    return respone

culprit_info = None

def getAlibi(name):
    message = []
    locations = ["방1", "방2", "거실", "화장실"]
    location = random.choice(locations)
    message.append({"role": "system", "content": f"{name}이(가) 범행 당시 {location}에 있었는지와 무엇을 하고 있었는지 설명해줘"})
    alibi = getRespone(message)
    print(f"{name}의 알리바이: {alibi}")

def getDetail(story):
    # Get the story summary from the user
    summary = input("사건 요약을 입력해주세요: ")

    message = []
    message.append({"role": "system", "content": "사건에 대해서 범인을 공개하지 않고 자세한 이야기를 구성해줘"})
    message.append({"role": "user", "content": f"사건 요약: {summary}"})
    Detail = getRespone(message)
    print(Detail)

    # Get the alibi of each suspect
    for i in range(6):  # assuming there are 6 suspects
        name = input(f"용의자 {i+1}의 이름을 입력해주세요: ")
        getAlibi(name)

def getSetting():
    global culprit_info

    # Get the suspect and weapon from the user
    suspect = input("용의자의 이름을 입력해주세요: ")
    weapon = input("범행 도구를 입력해주세요: ")

    # Choose a random subject from the list
    subject = random.choice(["병원", "별장", "회사"])

    message = []
    message.append({"role": "system", "content": f"주제와 용의자를 통해 범인을 특정해서 [범인: 범행도구: 사망원인: ]형태로 답변해줘"})
    message.append({"role": "user", "content": f"주제: {subject}, 용의자: {suspect}, 범행 도구: {weapon}"})
    Setting = getRespone(message)
    #[범인: 범행도구: 사건줄거리: ] 형태로 값이 주어진다.
    culprit_info = Setting
    getDetail(Setting)

getSetting()