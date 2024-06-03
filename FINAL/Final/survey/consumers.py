import json
from django.db import transaction
from channels.generic.websocket import WebsocketConsumer
from .models import Question, Choice, Response

class SurveyConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def connect(self):
        self.accept()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']

        if message_type == 'get_question':
            question_id = text_data_json['question_id']
            try:
                question = self.get_question(question_id)
                choices = self.get_choices(question_id)
                
                # Send question and choices to the user
                self.send(text_data=json.dumps({
                    'question': question.text,
                    'choices': choices,  # 변경됨
                    'type': question.question_type
                }))
            except Question.DoesNotExist:
                self.send(text_data=json.dumps({'error': 'Question not found'}))

        elif message_type == 'submit_response':
            user_id = text_data_json['user_id']
            question_id = text_data_json['question_id']
            choice_ids = text_data_json.get('choice_ids', [])
            text_response = text_data_json.get('text_response', '')

            # Store response
            self.store_response(question_id, user_id, text_response, choice_ids)

    def get_question(self, question_id):
        return Question.objects.get(pk=question_id)

    def get_choices(self, question_id):
        choices = Choice.objects.filter(question_id=question_id)
        return [{'id': choice.id, 'text': choice.choice_text} for choice in choices]

    def store_response(self, question_id, user_id, text_response, choice_ids):
        question = Question.objects.get(pk=question_id)
        response = Response(question=question, user_id=user_id)
        with transaction.atomic():
            response.save()

            if question.question_type == 'text':
                response.text_response = text_response
            elif question.question_type in ['choice', 'multiple']:
                for choice_id in choice_ids:
                    choice = Choice.objects.get(pk=choice_id)
                    response.choice_responses.add(choice)

            response.save()
