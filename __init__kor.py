__version__ = "0.0.1"

# Import modules
import chatgpt
import re
import json


# chatbot 기반 응용 프로그램을 위한 Non-Player Character (NPC) 클래스를 정의합니다.
class NPC:
    # 필요한 정보와 선택적으로 제어자와 프록시를 포함하여 NPC를 초기화합니다.
    def __init__(self, character, prompt, controllers=[], proxy=''):
        self.prompt = prompt
        self.controllers = controllers
        self.character = character
        self.messages = [
            {"role": "system", "content": self.prompt},
        ]
        self.proxy = proxy

        # NPC가 메인 스레드에 콜백을 요청하는 라벨의 리스트입니다.
        # 일부 이유로 인해 NPC가 직접 호출하는 경우 제대로 작동하지 않습니다.
        self.callbacks = []


# 저장 가능하도록 이 객체를 피클링 가능하게 만들기 위해 필요합니다.
def __getstate__(self):
    state = self.__dict__.copy()
    # 이 상태 사전에서 피클링할 수 없는 속성을 제거합니다.
    state['chatgpt'] = None
    state['re'] = None
    state['json'] = None
    return state


def __setstate__(self, state):
    # 상태 사전에서 인스턴스 상태를 복원합니다.
    self.__dict__.update(state)
    import chatgpt
    import re
    import json
    self.chatgpt = chatgpt
    self.re = re
    self.json = json


# NPC가 말하는 함수
def npc_says(self, message, display_message=True):
    self.messages.append(
        {"role": "assistant", "content": message}
    )
    if display_message: self.display_line_by_line(message)


# 사용자 입력을 처리하고 메시지 기록에 추가합니다.
def user_says(self, user_input):
    # 사용자 입력을 메시지 기록에 추가합니다.
    self.messages.append(
        {"role": "user", "content": user_input}
    )

    # 이상한 문자 제거
    user_input = re.sub(r'[^\w\s\'!\(\)\?\.\,\:\;\-]', '', user_input)

    # 메시지 기록이 10000자 제한을 초과하지 않도록 합니다.
    while len(str(self.messages)) > 10000:
        self.messages.pop(1)

    # ChatGPT API를 사용하여 응답 생성을 시도합니다.
    try:
        self.messages = chatgpt.completion(self.messages, proxy=self.proxy)

        # 생성된 메시지에서 NPC의 응답 추출
        response = self.messages[-1]["content"]
    except Exception as e:
        # API 호출이 실패한 경우 오류 메시지 표시
        response = "(오류가 발생했습니다. 다시 시도해주세요)"

    # 지정된 시간 간격으로 NPC의 응답을 한 줄씩 표시합니다.
    self.display_line_by_line(response)

    # 마지막으로 컨트롤러 호출
    for controller in self.controllers:
        result = controller.control(self.messages, self.proxy)
        if result is not None:
            self.callbacks.append(result)


# 주어진 텍스트를 문장 단위로 분할하고 한 줄씩 표시합니다.
def display_line_by_line(self, text):
    # 텍스트가 충분히 짧으면 한 번에 표시합니다.
    if len(text) < 150:
        self.character(text)
        return

    split_into_sentences = []

    # 정규 표현식을 사용하여 텍스트를 문장으로 분할합니다.
    split_into_sentences = re.split(r'\.\s|\n\n', text)

    # 문장을 반복하며 지정된 시간 간격으로 표시합니다.
    for sentence in split_into_sentences:
        # 문장에서 앞뒤 공백 제거
        sentence = sentence.strip()

        self.character(sentence)


# 이 클래스는 대화를 분석하고 특정 키워드가 언급되었는지 확인하여
# 조건이 충족되면 콜백 함수를 트리거하는 데 설계되었습니다.
class Controller:
    def __init__(self, control_phrase, callback, activated=True, permanent=False):
        # control_phrase를 포함하여 컨트롤 프롬프트를 구성하세요.
        self.prompt = (
                """I want you to act as a sentence analyser that responds to questions based on a conversation between a user and an assistant.
            if ("""
                + control_phrase
                + """) then respond this exact word '<TRUE>'
        else respond this exact word '<FALSE>'"""
        )

        # 콜백 함수를 저장합니다.
        self.callback = callback

        # 기본적으로 콜백은 활성화되어 있지만 비활성화할 수 있습니다.
        self.activated = activated

        # 기본적으로 콜백은 트리거된 후에 비활성화됩니다. 그러나 일부 컨트롤러는 영구적일 수 있습니다.
        self.permanent = permanent

    def control(self, messages, proxy):

        # 콜백이 비활성화된 경우 건너뜁니다.
        if not self.activated: return None

        # 대화를 최대 5000자로 유지합니다.
        few_last_messages = messages.copy()

    # 기본적으로 첫 번째 메시지를 제거합니다. (프롬프트입니다.)
    few_last_messages.pop(0)

    # 메시지 기록이 5000자 제한을 초과하지 않도록 합니다.
    while len(str(few_last_messages)) > 5000:
        few_last_messages.pop(0)

        # 대화 기록을 포함하여 컨트롤 메시지를 구성합니다.
    control_messages = [
        {"role": "system", "content": self.prompt},
        {
            "role": "user",
            "content": (
                    "사용자와 어시스턴트 간의 대화입니다 \n\n <"
                    + json.dumps(few_last_messages)
                    + "> \n\n"
                    + self.prompt
            ),
        },
    ]

    try:
        # ChatGPT API 호출로 응답을 가져옵니다.
        response = chatgpt.completion(control_messages, proxy=proxy)[-1]["content"]
    except:
        # API 호출이 실패한 경우 오류 메시지를 표시합니다.
        response = "<FALSE> ERROR"

    # 때로는 "주장"하고 "True"와 "False"가 포함된 응답을 줍니다.
    # 따라서 응답에 True가 있고 False가 없으며 콜백이 None이 아닌 경우에만 계속 진행합니다.
    if "<TRUE>" in response and not "<FALSE>" in response and self.callback is not None:

        # 비영구적이지 않으면 콜백은 한 번만 호출되어야 합니다.
        if not self.permanent: self.activated = False

        return self.callback

    return None
