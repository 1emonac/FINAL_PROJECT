import openai
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SurveyRoom

# OpenAI API 키 설정
openai.api_key = os.environ.get("OPENAI_API_KEY")

def survey_room(request):
    try:
        # 단일 고정된 채팅방을 가져오거나 생성합니다.
        room, created = SurveyRoom.objects.get_or_create(
            pk=1,
            defaults={
                'user': request.user,  # 현재 접속한 사용자를 기본값으로 설정
                'situation': '기본 상황',
                'situation_kr': '기본 상황 (한국어)',
                'my_role': '설문조사 참여자',
                'gpt_role': '설문조사 안내원'
            }
        )
    except Exception as e:
        return render(request, 'survey/error.html', {'error': str(e)})

    return render(request, 'survey/survey3.html', {'room': room})




# WebSocket 기반 설문조사를 위한 뷰
def chat_view(request):
    return render(request, 'survey/chat.html')

# 결과 페이지를 보여주는 뷰
def result_view(request):
    return render(request, 'survey/result.html')

def example(request):
    return render(request, 'survey/survey3.html')

def example2(request):
    return render(request, 'survey/survey4.html')

def survey5(request):
    return render(request, 'survey/survey5.html')


