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
    path('survey_door/', views.survey_door, name='survey_door'),
    path('survey/', views.survey_room, name='survey'),
    path('survey_result/', views.survey_result, name="survey_result"),
    path('result_add/', views.result_add, name="result_add"),
    path('alter_survey/<str:date>/', views.alter_survey, name='alter_survey'),
    path('plus_survey/<str:date>', views.plus_survey, name="plus_survey"),
    path('plus_result/<str:date>', views.plus_result, name="plus_result"),
    path('alter_plus_survey/<str:date>/', views.alter_plus_survey, name='alter_plus_survey'),
]
