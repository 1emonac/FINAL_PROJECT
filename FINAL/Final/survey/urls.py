# from django.urls import path
# from . import views

# app_name = "survey"
# urlpatterns = [
#     path('start/', views.start_survey, name='survey'),  # 사용자가 설문을 시작하는 주소
#     # path("result/", views.result, name="result"),  # 결과 페이지를 위한 뷰 필요
#     path('result/', views.sleep_results, name='result'),
# ]

# survey/urls.py

# survey/urls.py

from django.urls import path
from . import views

app_name="survey"
urlpatterns = [
    path('result/', views.result_view, name='result'),
    path('survey/', views.chat_view, name='survey'),  # Chat URL 추가
    path('survey3/', views.example, name='survey3'),
    path('survey4/', views.example2, name="survey4"),
]
