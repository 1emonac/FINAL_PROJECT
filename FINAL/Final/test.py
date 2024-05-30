from langchain import ConversationChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

class ChatBot:
    def __init__(self):
        self.memory = ConversationBufferMemory()
        self.llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key="YOUR_OPENAI_API_KEY")
        self.system_message = "당신은 정신과에서 근무하고 있고 수면 장애를 겪고 있는 사람들을 위한 의사입니다."
        self.conversation = ConversationChain(llm=self.llm, memory=self.memory, system_prompt=self.system_message)

    def get_query(self, command_query: str = None, user_query: str = None) -> str:
        if command_query is not None and user_query is not None:
            raise ValueError("command_query 인자와 user_query 인자는 동시에 사용할 수 없습니다.")
        elif command_query is not None:
            input_text = command_query
        elif user_query is not None:
            input_text = user_query

        response = self.conversation.predict(input_text)
        return response

# 사용 예제
chatbot = ChatBot()
response = chatbot.get_query(user_query="대화를 나눠봅시다.")
print(response)