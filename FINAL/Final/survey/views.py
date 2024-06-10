import openai
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SurveyRoom, Pred
import joblib
import pandas as pd
import numpy as np
from django.utils import timezone

# OpenAI API 키 설정
openai.api_key = os.environ.get("OPENAI_API_KEY")

def survey_room(request):
    return render(request, 'survey/survey.html')



# 결과 페이지를 보여주는 뷰
def result_view(request):
    survey = Pred.objects.all()  # 예시: 모든 데이터 가져오기
    context = {"survey" : survey}
    
    return render(request, 'survey/result.html', context)


def survey_result(request):
    if request.method == 'POST':
        # POST 요청으로 전송된 데이터 가져오기
        lr = joblib.load(os.path.join('static', "model", 'logistic_regression_model.pkl'))
        pred_df = dict()
        for key, value in request.POST.items():
            if "token" not in key:
                pred_df[key] = value
        pred = pd.DataFrame(pred_df.values()).T
        pred = np.round(lr.predict_proba(pred)[0][0] * 100).astype(int)
        context = {"predict" : pred, "pred_df" : pred_df}
        return render(request, 'survey/survey_result.html', context)
    
    else:
        return render(request, 'survey/survey.html')

def result_add(request):
    if request.method == 'POST':
        lr = joblib.load(os.path.join('static', "model", 'logistic_regression_model.pkl'))
        values = list()
        # POST 요청으로 전송된 데이터 확인
        for key, value in request.POST.items():
            if "token" in key:
                pass
            elif "predict" == key:
                key = value
            else:
                values.append(value)
        pred = pd.DataFrame(values).T
        pred = lr.predict(pred)

        if key == "1":
            # 저장 만들어 주기
            if pred[0] == 0:
                pred_dt = 0
        
            else:
                pred_dt = 1

            pred_proba = np.round(lr.predict_proba(pd.DataFrame(values).T)[0][0] * 100).astype(int)
        else:
            if pred[0] == 0:
                pred_dt = 1
            else:
                pred_dt = 0
            pred_proba = np.round(lr.predict_proba(pd.DataFrame(values).T)[0][1] * 100).astype(int)


        pred_instance = Pred(
            user=request.user,  # 사용자 객체
            predict=pred_dt,  # 예측 결과
            predict_proba=pred_proba,
            sleep_survey=request.POST.get('sleep_survey'),  # survey1 값
            stress_survey=request.POST.get('stress_survey'),  # survey2 값
            positive_survey=request.POST.get('poitive_survey'),  # survey3 값
        )
        pred_instance.save()

    return render(request, 'users/profile.html')

def survey5(request):
    return render(request, 'survey/survey5.html')

def plus_result(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            print(key, value)
    return render(request, 'survey/plus_result.html')


