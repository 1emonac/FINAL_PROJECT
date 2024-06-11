from typing import List

import os
import openai
from channels.generic.websocket import JsonWebsocketConsumer
from django.conf import settings
from openai.types.chat import ChatCompletion

from dr.models import SleepClinicRoom, GptMessage

OPENAI_CLIENT = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

class SleepClinicRoomConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpt_messages: List[GptMessage] = []

    def connect(self):
        room = self.get_room()
        self.accept()
        self.gpt_messages = room.get_initial_messages()
        assistant_message = self.get_query()
        self.send_json(
            {
                "type": "assistant-message",
                "message": assistant_message,
            }
        )

    def receive_json(self, content_dict, **kwargs):
        if content_dict["type"] == "user-message":
            assistant_message = self.get_query(user_query=content_dict["message"])
            self.send_json(
                {
                    "type": "assistant-message",
                    "message": assistant_message,
                }
            )
        else:
            self.send_json(
                {
                    "type": "error",
                    "message": f"Invalid type: {content_dict['type']}",
                }
            )

    def get_room(self):
        room, created = SleepClinicRoom.objects.get_or_create(
            pk=1,
            defaults={
                'user': self.scope["user"],  # 현재 접속한 사용자를 기본값으로 설정
                'situation': '기본 상황',
                'situation_kr': '기본 상황 (한국어)',
                'my_role': '환자',
                'gpt_role': '수면클리닉 의사'
            }
        )
        return room

    def get_query(self, command_query: str = None, user_query: str = None) -> str:
        if command_query is not None and user_query is not None:
            raise ValueError("command_query 인자와 user_query 인자는 동시에 사용할 수 없습니다.")
        elif command_query is not None:
            self.gpt_messages.append(GptMessage(role="user", content=command_query))
        elif user_query is not None:
            self.gpt_messages.append(GptMessage(role="user", content=user_query))

        response: ChatCompletion = OPENAI_CLIENT.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.gpt_messages,
            temperature=0.9
        )
        response_role = response.choices[0].message.role
        response_content = response.choices[0].message.content

        if command_query is None:
            gpt_message = GptMessage(role=response_role, content=response_content)
            self.gpt_messages.append(gpt_message)
        return response_content
