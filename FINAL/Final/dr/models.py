from typing import TypedDict, Literal
from django.conf import settings
from django.db import models
from django.urls import reverse


class GptMessage(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


class SleepClinicRoom(models.Model):
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
    my_role = models.CharField(max_length=100, verbose_name="내 역할", default="환자")
    gpt_role = models.CharField(max_length=100, verbose_name="GPT 역할", default="수면클리닉 의사")

    def get_absolute_url(self):
        return reverse("dr_chat", args=[self.pk])

    def get_initial_messages(self):
        gpt_name = "Dr.Eunoia"
        situation_kr = self.situation_kr or self.situation

        system_message = (
            f"당신은 수면 클리닉 의사입니다. "
            f"당신의 이름은 {gpt_name}입니다. "
            f"한국어로 상담자와 대화하십시오. "
        )

        user_message = (
            f"상황은 '{situation_kr}'입니다. "
            f"나는 상담자입니다. 당신은 수면클리닉 의사 역할을 맡고 있습니다. 나는 수면의 문제로 클리닉에 처음 방문했습니다."
            f"상담자님이라고 불러주세요. "
            f"이제 대화를 시작합시다!"
        )

        # user의 이름을 메시지에 포함
        if self.user:
            user_name = self.user.username  # username을 사용
            user_message = user_message.replace("나는 상담자입니다.", f"나는 {user_name}입니다.")
            
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
