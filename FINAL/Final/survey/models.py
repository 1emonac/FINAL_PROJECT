# from typing import TypedDict, Literal
from django.conf import settings
from django.db import models
from django.urls import reverse

# class GptMessage(TypedDict):
#     role: Literal["system", "user", "assistant"]
#     content: str

# class SurveyRoom(models.Model):
#     class Meta:
#         ordering = ["-pk"]

#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     situation = models.CharField(max_length=100, verbose_name="상황", default="기본 상황")
#     situation_kr = models.CharField(
#         max_length=100,
#         blank=True,
#         verbose_name="상황 (한국어)",
#         help_text="GPT 프롬프트에 직접적으로 활용됩니다. 비워두시면, situation 필드를 번역하여 자동 반영됩니다.",
#     )
#     my_role = models.CharField(max_length=100, verbose_name="내 역할", default="설문조사 참여자")
#     gpt_role = models.CharField(max_length=100, verbose_name="GPT 역할", default="설문조사 안내원")

#     def get_absolute_url(self):
#         return reverse("survey3", args=[self.pk])

#     def get_initial_messages(self):
#         gpt_name = "E-nest"
#         situation_kr = self.situation_kr or self.situation
#         user_name = self.user.username if self.user else "사용자"

#         system_message = (
#             f"당신은 설문조사 안내원입니다. "
#             f"당신의 이름은 {gpt_name}입니다. "
#             f"한국어로 참여자와 대화하십시오. "
#         )

#         user_message = (
#             f"상황은 '{situation_kr}'입니다. "
#             f"나는 {user_name}입니다. 당신은 설문조사 질문을 안내해 주는 역할을 맡고 있습니다. "
#             f"이제 대화를 시작합시다!"
#         )

#         return [
#             {"role": "system", "content": system_message},
#             {"role": "user", "content": user_message},
#         ]
    
# class Message(models.Model):
#     user = models.CharField(max_length=255)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user}: {self.content}"

class Pred(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    predict = models.SmallIntegerField("결과") # 0은 잘 잤다고 평가 1은 잘 못잤다고 평가
    predict_proba = models.SmallIntegerField("잘 잤을 확률") # 0이 나올 확률(정확하지 않다고 입력 시 1이 나올 확률을 입력)
    sleep_survey = models.SmallIntegerField("숙면여부") # 0은 잘 잤다고 평가 1은 잘 못잤다고 평가
    stress_survey = models.SmallIntegerField("스트레스의 강도") # 1 ~ 5 사이의 값 높을 수록 강도가 낮음
    positive_survey = models.SmallIntegerField("긍정의 강도") # 1 ~ 7 사이의 값 높을 수록 긍정
    date = models.DateField("일자", auto_now_add=True) 
    

class PlusPred(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    date = models.DateField("일자", auto_now_add=True) 
    dream_survey = models.SmallIntegerField("꿈의 강도")
    caffeine_survey = models.SmallIntegerField("카페인 강도")
    alcohol_survey = models.SmallIntegerField("알코올의 강도")
    talk_survey = models.SmallIntegerField("대화의 강도")
    personalcare_survey = models.SmallIntegerField("개인정비의 강도")
    work_survey = models.SmallIntegerField("당일 업무 유무")
    home_survey = models.SmallIntegerField("집에서 많은 시간을 보내는지의 여부")
    