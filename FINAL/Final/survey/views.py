import openai
import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SurveyRoom
import joblib
import pandas as pd
import numpy as np

# OpenAI API 키 설정
openai.api_key = os.environ.get("OPENAI_API_KEY")

def survey_room(request):
    return render(request, 'survey/survey.html')



# 결과 페이지를 보여주는 뷰
def result_view(request):
    return render(request, 'survey/result.html')


def example2(request):
   if request.method == 'POST':
        # POST 요청으로 전송된 데이터 가져오기
        lr = joblib.load(os.path.join('static', "model", 'logistic_regression_model.pkl'))
        pred_df = list()
        for key, value in request.POST.items():
            if "token" not in key:
                pred_df.append(value)
        pred_df = pd.DataFrame(pred_df).T
        print(lr.predict_proba(pred_df)[0][1])
        pred_df = np.round(lr.predict_proba(pred_df)[0][1] * 100).astype(int)
        context = {"predict" : pred_df}
        return render(request, 'survey/survey4.html', context)

def survey5(request):
    return render(request, 'survey/survey5.html')


