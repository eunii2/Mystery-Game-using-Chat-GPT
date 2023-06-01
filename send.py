import openai

openai.api_key = "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"


def getRespone(message):
    answer = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
    respone = answer.choices[0].message["content"].strip()
    return respone


# 상호 작용 함수들 넣을 예정
def getSetting():
    message = []
    message.append({"role": "system", "content": "주제와 용의자를 통해 범인을 특정해서 살인사건 이야기를 만들어서 [범인: 범행도구: 사망원인: ]형태로 답변해줘"})
    message.append({"role": "user", "content": f"{subject}"})
    Setting = getRespone(message)
    # [범인: 범행도구: 사건줄거리: ] 형태로 값이 주어진다.
    print(Setting)
    # getDetail(Setting)
    return Setting


def person_1():
    message = []
    message.append({"role": "system", "content": subject + "\n" + getSetting() + "\n 이 이야기의 김민석이 되어서 대화를 해줘"})
    # message.append({"role": "assistant", "content": getSetting('펜션에서 살인 사건이 일어났다. 용의자 1, 2, 3, 4, 5 중 범인이 있다고 한다. 증거로는 피 묻은 칼과 침대 밑에서 수면제가 발견되었다.')})
    aa = input('입력 : ')
    message.append({"role": "user", "content": aa})
    Setting = getRespone(message)
    message.append({"role": "assistant", "content": Setting})
    print(Setting)

    while True:
        aa = input('입력 : ')
        message.append({"role": "user", "content": aa})
        Setting = getRespone(message)
        message.append({"role": "assistant", "content": Setting})

        print(Setting)

    # getDetail(Setting)
    return Setting


subject = '병원에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 자주 다투던 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자와 원한 관계에 있다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 주사기와 침대 옆 선반에 독성 물질이 발견되었다.'
subject_1 = '펜션에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 친한 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자와 원한 관계에 있다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 피 묻은 칼과 침대 옆 선반에 수면제 가루가 발견되었다.'
person_1()