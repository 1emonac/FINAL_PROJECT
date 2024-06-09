import openai
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Response

openai.api_key = 'YOUR_OPENAI_API_KEY'

# 이 함수는 더 이상 사용하지 않지만, GPT 응답을 얻기 위해 남겨둘 수 있습니다.
def get_gpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']

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

