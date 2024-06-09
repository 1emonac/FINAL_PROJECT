from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SleepClinicRoom


def chat_room(request):
    # 단일 고정된 채팅방을 가져오거나 생성합니다.
    room, created = SleepClinicRoom.objects.get_or_create(
        pk=1,
        defaults={
            'user': request.user,  # 현재 접속한 사용자를 기본값으로 설정
            'situation': '기본 상황',
            'situation_kr': '기본 상황 (한국어)',
            'my_role': '환자',
            'gpt_role': '수면클리닉 의사'
        }
    )
    return render(request, 'dr/dr_chat.html', {'room': room})

def list(request):    
    return render(request, "dr/dr_list.html")
