from typing import TypedDict, Literal
from django.conf import settings
from django.db import models
from django.urls import reverse

class GptMessage(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str

class SurveyRoom(models.Model):
    class Meta:
        ordering = ["-pk"]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    situation = models.CharField(max_length=100, verbose_name="상황", default="기본 상황")
    situation_kr = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="상황 (한국어)",
        help_text="GPT 프롬프트에 직접적으로 활용됩니다. 비워두시면, situation 필드를 번역하여 자동 반영됩니다.",
    )
    my_role = models.CharField(max_length=100, verbose_name="내 역할", default="설문조사 참여자")
    gpt_role = models.CharField(max_length=100, verbose_name="GPT 역할", default="설문조사 안내원")

    def get_absolute_url(self):
        return reverse("survey3", args=[self.pk])

    def get_initial_messages(self):
        gpt_name = "E-nest"
        situation_kr = self.situation_kr or self.situation
        user_name = self.user.username if self.user else "사용자"

        system_message = (
            f"당신은 설문조사 안내원입니다. "
            f"당신의 이름은 {gpt_name}입니다. "
            f"한국어로 참여자와 대화하십시오. "
        )

        user_message = (
            f"상황은 '{situation_kr}'입니다. "
            f"나는 {user_name}입니다. 당신은 설문조사 질문을 안내해 주는 역할을 맡고 있습니다. "
            f"이제 대화를 시작합시다!"
        )

        return [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ]
    
class Message(models.Model):
    user = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}: {self.content}"


class Pred(models.Model):
    user = models.CharField(max_length=255)
    predict = models.TextField("결과", max_length=1) # 0은 잘 잤다고 평가 1은 잘 못잤다고 평가
    predict_proba = models.TextField("잘 잤을 확률", max_length=2) # 0은 잘 잤다고 평가 1은 잘 못잤다고 평가
    survey1 = models.TextField("숙면여부", max_length=1) # 0은 잘 잤다고 평가 1은 잘 못잤다고 평가
    survey2 = models.TextField("스트레스의 강도", max_length=1) # 1 ~ 5 사이의 값
    survey3 = models.TextField("긴장의 강도", max_length=1 ) # 1 ~ 7 사이의 값
    date = models.DateField("일자", auto_now_add=True) 
    