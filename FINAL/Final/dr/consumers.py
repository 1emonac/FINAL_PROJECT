from typing import List

import os
import openai
from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import AbstractUser
from openai.types.chat import ChatCompletion

from dr.models import SleepClinicRoom, GptMessage

OPENAI_CLIENT = openai.OpenAI(api_key=os.environ.get("OPENAI_API_KEY"), )

FIXED_ROOM_PK = 1  # 고정된 방의 Primary Key

class SleepClinicRoomConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpt_messages: List[GptMessage] = []

    def connect(self):
        room = self.get_room()
        if room is None:
            self.close()
        else:
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
        try:
            room = SleepClinicRoom.objects.get(pk=FIXED_ROOM_PK)
        except SleepClinicRoom.DoesNotExist:
            room = None
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
            temperature=1,
        )
        response_role = response.choices[0].message.role
        response_content = response.choices[0].message.content

        if command_query is None:
            gpt_message = GptMessage(role=response_role, content=response_content)
            self.gpt_messages.append(gpt_message)
        return response_content
