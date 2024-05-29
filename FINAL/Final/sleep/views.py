from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from users.forms import *
from .models import *

from api import address
from private_file import key
import json
from django.http import JsonResponse

import geocoder

# Create your views here.
# video.html
def video(request):    
    return render(request, "main/videomain.html")

def main(request):
    user = request.user
    context = {"user" : user,}
    return render(request, "main/main.html", context)

# # main 페이지 연결
# def main(request):
#     if request.user.is_authenticated:
#         return redirect("sleep:main")
    
#     if request.method == "POST":
#         form = LoginForm(data=request.POST)
#         if form.is_valid():
#             # username과 password 값을 가져와 변수에 할당
#             username = form.cleaned_data["username"]
#             password = form.cleaned_data["password"]

#             # username, password 에 해당하는 사용자가 있는지 검사
#             user = authenticate(username=username, password=password)

#             # 해당 사용자가 존재한다면
#             if user:
#                 # 로그인 처리 후, 피드페이지로 redirect
#                 login(request, user)
#                 return redirect("sleep:main")
#             # 사용자가 없다면 form에 에러 추가
#             else: 
#                 form.add_error(None, "입력한 자격증명에 해당하는 사용자가 없습니다(이걸 틀리네 낄낄)")

#         # 실패한 경우 다시 LoginForm 을 사용한 로그 페이지 렌더링
#         context = {"form" : form}

#     else:
#         # LoginForm 인스턴스를 생성
#         form = LoginForm()

#         # 생성한 LoginForm 인스턴스를 템플릿에 "form" 이라는 키로 전달
#         context = {
#             "form" : form,
#         }
#     return render(request, 'main/main.html', context)

def define(request):    
    return render(request, "feed/define.html")

def chatbot(request):    
    return render(request, "feed/chatbot.html")

# def chatting(request):    
#     return render(request, "feed/chatting.html")

def drai(request):    
    return render(request, "feed/drai.html")

def result(request):    
    return render(request, "feed/result.html")

def team(request):    
    return render(request, "business/team.html")

# map.html
def map(request):
    data = address.search()
    kakao_map_key = key.kakao_map_key
    if request.method == "POST":
        fetchData = json.loads(request.body)
        x = fetchData["x"]
        y = fetchData["y"]
        sleep_clinic = address.searchGeo(x,y,"정신과")
        return JsonResponse({"sleep_clinic": sleep_clinic,})
    
    context = {
        "map_key" : kakao_map_key,
        "data" : json.dumps(data), 
        "sleep_clinic" : "수면클리닉"
    }
    return render(request, "feed/mapping.html", context)
# from sleep.models import Survey

# def list_answer(request):
#     survey = Survey.objects.filter(status="y").order_by('-survey_idx')[0]
#     context = {
#         "survey" : survey
#     }
#     return render(request, "list.html", context)