# survey/consumers.py

import json
import os
from channels.generic.websocket import WebsocketConsumer
from .models import Response
from django.contrib.auth.models import User
from django.conf import settings

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'survey_chat'
        self.room_group_name = 'chat_%s' % self.room_name
        self.questions = self.load_questions()
        self.current_question_index = 0
        self.responses = {}

        self.accept()
        self.send_question()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json.get('type')

        if message_type == 'user-message':
            message = text_data_json['message']
            current_question = self.questions[self.current_question_index - 1]
            self.responses[current_question['key']] = message

            if self.current_question_index < len(self.questions):
                self.send_question()
            else:
                self.send(text_data=json.dumps({
                    'type': 'assistant-message',
                    'message': '설문조사가 완료되었습니다. 감사합니다!'
                }))
                self.save_responses()
        else:
            self.send(text_data=json.dumps({
                'type': 'error',
                'message': 'Unknown message type.'
            }))

    def send_question(self):
        question = self.questions[self.current_question_index]
        self.current_question_index += 1

        if question['type'] == 'text':
            self.send(text_data=json.dumps({
                'type': 'assistant-message',
                'message': question['question']
            }))
        elif question['type'] == 'choice':
            choices = ', '.join(question['choices'])
            self.send(text_data=json.dumps({
                'type': 'assistant-message',
                'message': f"{question['question']} (Choices: {choices})"
            }))
        elif question['type'] == 'multiple':
            choices = ', '.join(question['choices'])
            self.send(text_data=json.dumps({
                'type': 'assistant-message',
                'message': f"{question['question']} (Multiple choices: {choices})"
            }))

    def load_questions(self):
        file_path = os.path.join(settings.BASE_DIR, 'survey', 'data', 'questions.json')
        with open(file_path, 'r') as f:
            questions = json.load(f)
        return questions

    def save_responses(self):
        user = self.scope['user']
        for key, response in self.responses.items():
            Response.objects.create(user=user if user.is_authenticated else None, response=response)
