from django.urls import path
from . import views

app_name = "survey"
urlpatterns = [
    path('start/', views.start_survey, name='survey'),  # 사용자가 설문을 시작하는 주소
    # path("result/", views.result, name="result"),  # 결과 페이지를 위한 뷰 필요
    path('result/', views.view_results, name='result'),
]
