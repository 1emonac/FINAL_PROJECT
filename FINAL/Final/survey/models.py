from django.db import models
from django.conf import settings

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=50)  # 예: text, choice, multiple
    choices = models.TextField(blank=True)  # 선택형 질문의 선택지들을 저장

    def __str__(self):
        return self.question_text

class Response(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.response
