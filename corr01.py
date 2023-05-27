import openai

openai.api_key = "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"

def getRespone(message):
    answer = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    respone = answer.choices[0].message["content"].strip()
    return respone

def getSetting(subject):
    # Get the suspect and weapon from the user
    suspect = input("용의자의 이름을 입력해주세요: ")
    weapon = input("범행 도구를 입력해주세요: ")

    message = []
    message.append({"role": "system", "content": f"주제와 용의자를 통해 범인을 특정해서 [범인: 범행도구: 사망원인: ]형태로 답변해줘"})
    message.append({"role": "user", "content": f"주제: {subject}, 용의자: {suspect}, 범행 도구: {weapon}"})
    Setting = getRespone(message)
    #[범인: 범행도구: 사건줄거리: ] 형태로 값이 주어진다.
    print(Setting)
    getDetail(Setting)

def getDetail(story):
    # Get the story summary from the user
    summary = input("사건 요약을 입력해주세요: ")

    message = []
    message.append({"role": "system", "content": "사건에 대해서 범인을 공개하지 않고 자세한 이야기를 구성해줘"})
    message.append({"role": "user", "content": f"사건 요약: {summary}"})
    Detail = getRespone(message)
    print(Detail)

def getName(n = 6):
    names = []
    for i in range(n):
        name = input(f"{i+1}. 이름과 나이, 성별을 입력해주세요(예: 김민석 (23세) 남자): ")
        names.append(name)

    message = []
    message.append({"role": "system", "content": "[1. 이름 (나이) 성별] 형태로 출력해줘 예를 들어 [1. 김민석 (23세) 남자]"})
    message.append({"role": "user", "content": f"{names}"})
    names = getRespone(message)
    # [1. 김민수 (27세) 남자] 형태로 n개 출력된다
    print(names)

    return names