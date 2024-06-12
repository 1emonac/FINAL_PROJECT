# from typing import TypedDict, Literal
from django.conf import settings
from django.db import models
from django.urls import reverse

class Pred(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    user_username = models.CharField(max_length=150, verbose_name="유저명")
    predict = models.SmallIntegerField("결과") # 0은 잘 잤다고 평가 1은 잘 못잤다고 평가
    predict_proba = models.SmallIntegerField("잘 잤을 확률") # 0이 나올 확률(정확하지 않다고 입력 시 1이 나올 확률을 입력)
    sleep_survey = models.SmallIntegerField("숙면여부") # 0은 잘 잤다고 평가 1은 잘 못잤다고 평가
    stress_survey = models.SmallIntegerField("스트레스의 강도") # 1 ~ 5 사이의 값 높을 수록 강도가 낮음
    positive_survey = models.SmallIntegerField("긍정의 강도") # 1 ~ 7 사이의 값 높을 수록 긍정
    date = models.DateField("일자", ) 

    class Meta:
        ordering = ['date']  # 날짜가 작은 순서로 정렬
    
    def save(self, *args, **kwargs):
        self.user_username = self.user.username  # user의 username을 동기화
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_username} - {self.date}"

class PlusPred(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE,)
    user_username = models.CharField(max_length=150, verbose_name="유저명")
    date = models.DateField("일자") 
    dream_survey = models.SmallIntegerField("꿈의 강도")
    caffeine_survey = models.SmallIntegerField("카페인 강도")
    alcohol_survey = models.SmallIntegerField("알코올의 강도")
    talk_survey = models.SmallIntegerField("대화의 강도")
    personalcare_survey = models.SmallIntegerField("개인정비의 강도")
    work_survey = models.SmallIntegerField("당일 업무 유무")
    home_survey = models.SmallIntegerField("집에서 많은 시간을 보내는지의 여부")
    
    def save(self, *args, **kwargs):
        self.user_username = self.user.username  # user의 username을 동기화
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user_username} - {self.date}"