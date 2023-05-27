from GptHandler import getRespone

def getSetting(subject):
    message = []
    message.append({"role": "system", "content": "주제와 용의자를 통해 범인을 특정해서 [범인: 범행도구: 사망원인: ]형태로 답변해줘"})
    message.append({"role": "user", "content": f"{subject}"})
    Setting = getRespone(message)
    #[범인: 범행도구: 사건줄거리: ] 형태로 값이 주어진다.
    print(Setting)
    getDetail(Setting)

def getDetail(story):
    message = []
    message.append({"role": "system", "content": "사건에 대해서 범인을 공개하지 않고 자세한 이야기를 구성해줘"})
    message.append({"role": "user", "content": f"{story}"})
    Detail = getRespone(message)
    print(Detail)

def getName(n = 6):
    message = []
    message.append({"role": "system", "content": "[1. 이름 (나이) 성별] 형태로 출력해줘 예를 들어 [1. 김민석 (23세) 남자]"})
    message.append({"role": "user", "content": f"성과 이름을 포함한 한국어 이름과 나이와 성별을 {n}개 출력해줘"})
    names = getRespone(message)
    # [1. 김민수 (27세) 남자] 형태로 n개 출력된다
    print(names)

    return names
getSetting(f"병원")