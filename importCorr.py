import requests
import json

api_key = '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'

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

def getResponse(message):
    response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions',
                             headers=headers,
                             json={'model': 'gpt-3.5-turbo', 'messages': message})

    output = response.json()
    return output['choices'][0]['message']['content'].strip()

def getSetting():
    message = [{"role": "system",
                "content": "주제와 용의자를 통해 범인을 특정해서 살인사건 이야기를 만들어서 [범인: 범행도구: 사망원인: ]형태로 답변해줘"},
               {"role": "user", "content": f"{subject}"}]
    Setting = getResponse(message)
    print(Setting)
    return Setting

def person_1():
    Setting = getSetting()
    message = [{"role": "system", "content": subject + "\n" + Setting + "\n 이 이야기의 김민석이 되어서 대화를 해줘"}]

    while True:
        user_input = input('입력 : ')
        message.append({"role": "user", "content": user_input})
        response_text = getResponse(message)
        message.append({"role": "assistant", "content": response_text})

        print(response_text)

subject = '병원에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 자주 다투던 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자와 원한 관계에 있다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 주사기와 침대 옆 선반에 독성 물질이 발견되었다.'

person_1()
