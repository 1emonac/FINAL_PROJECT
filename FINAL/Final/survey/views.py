import os
from django.shortcuts import render
from .models import Pred, PlusPred
import joblib
import pandas as pd
import numpy as np
from django.utils import timezone


def survey_door(request):
    return render(request, 'survey/survey_door.html')


def survey_room(request):
    return render(request, 'survey/survey.html')



# 결과 페이지를 보여주는 뷰
def result_view(request):
    survey = Pred.objects.filter(user=request.user)  # 예시: 모든 데이터 가져오기
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
        df = dict()
        # POST 요청으로 전송된 데이터 확인
        for key, value in request.POST.items():
            
            if "token" in key:
                pass
            elif "predict" == key:
                key = value
            else:
                values.append(value)
                df[key] = value
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

        user = request.user
        date = timezone.now().date()
        sleep_survey = df["sleep_survey"]
        stress_survey = df["stress_survey"]
        positive_survey = df["positive_survey"]
        if PlusPred.objects.filter(date=date, user=request.user).exists():
        # 오늘 날짜와 사용자를 기준으로 레코드를 찾습니다.
            pred_instance = Pred.objects.get(date=date, user=user)

            # 기존 레코드가 존재하면 업데이트합니다.
            pred_instance.predict = pred_dt
            pred_instance.predict_proba = pred_proba
            pred_instance.sleep_survey = sleep_survey
            pred_instance.stress_survey = stress_survey
            pred_instance.positive_survey = positive_survey
            pred_instance.save()

        else:
            # 오늘 날짜와 사용자에 해당하는 레코드가 없으면 새로운 레코드를 생성합니다.
            pred_instance = Pred(
                user=user,
                predict=pred_dt,
                predict_proba=pred_proba,
                sleep_survey=sleep_survey,
                stress_survey=stress_survey,
                positive_survey=positive_survey,
                date=date
            )
            pred_instance.save()

    return render(request, 'users/profile.html')

def alter_survey(request, date):
    context = {"date" : date} 
    return render(request, 'survey/survey.html', context)

def alter_plus_survey(request, date):
    context = {"date" : date} 
    return render(request, 'survey/plus_survey.html', context)


def plus_survey(request, date):
    df = dict()
    if PlusPred.objects.filter(date=date, user=request.user).exists():

        for PlusPred_instance in PlusPred.objects.filter(date=date, user=request.user):
            df["dream_survey"] = PlusPred_instance.dream_survey
            df["caffeine_survey"] = PlusPred_instance.caffeine_survey
            df["alcohol_survey"] = PlusPred_instance.alcohol_survey
            df["talk_survey"] = PlusPred_instance.talk_survey
            df["personal_care_survey"] = PlusPred_instance.personalcare_survey
            df["work_survey"] = PlusPred_instance.work_survey
            df["home_survey"] = PlusPred_instance.home_survey

        print(df)
        if df["dream_survey"] > 2:
            df["dream_survey"] = "악몽을 오랜기간 꾸고 있다면 스트레스로 인해 수면에 어려움이 있을 것으로 예상됩니다."
        else:
            df["dream_survey"] = "꿈을 꾸지 않는 것이 가장 좋다고 할 수 있지만"

        if df["caffeine_survey"] == 2:
            df["caffeine_survey"] ="☕과도한 카페인 섭취는 건강에 해로울 수 있습니다. 하루 카페인 섭취량을 줄여 더 건강하고 균형 잡힌 생활을 유지하세요."
        else:
            df["caffeine_survey"] ="☕하루 한 잔의 커피는 항산화제 섭취를 증가시키고, 집중력과 기분을 개선하며, 특정 질병의 위험을 감소시키는 등 건강에 긍정적인 영향을 미칠 수 있습니다."

        if df["alcohol_survey"] == 2:
            df["alcohol_survey"] = "🍺과도한 알코올 섭취는 건강에 해로울 수 있습니다. 적당한 음주를 통해 더 건강한 생활을 지향하세요."
        else:
            df["alcohol_survey"] = "🍻적당한 음주는 심혈관 건강을 증진시키고, 사회적 유대감을 강화하는 등 건강에 긍정적인 영향을 미칠 수 있습니다."

        if df["talk_survey"] > 2:
            df["talk_survey"] = "잘 하고 계십니다😊 많은 대화를 나누는 것은 관계를 강화하고, 새로운 아이디어를 얻으며, 이해와 공감을 높이는 데 도움이 됩니다."
        else:
            df["talk_survey"] = "멋집니다🍀 하루 동안 적당히 대화를 즐기면 스트레스 해소, 관계 강화, 그리고 새로운 시각을 얻는 데 도움이 됩니다."

        if df["personal_care_survey"] == 1:
            df["personal_care_survey"] = "외부 활동이 많으면 신체 건강을 증진시키고, 기분을 상쾌하게 하며, 새로운 경험과 만남을 통해 삶의 질을 높일 수 있습니다.👍"
        else:
            df["personal_care_survey"] = "외부 활동이 부족하면 건강과 기분에 부정적인 영향을 줄 수 있습니다. 신선한 공기를 마시고 새로운 경험을 쌓기 위해 자주 밖으로 나가보세요!🙌"

        if df["work_survey"] == 1:
            df["work_survey"] = "💻과도한 업무와 학업 부담은 만성 스트레스와 건강 문제를 초래할 수 있습니다. 이를 예방하기 위해 적절한 휴식이 반드시 필요합니다."
        else:
            df["work_survey"] = "🏫적절한 사회 활동과 학업은 정신 건강과 전반적인 삶의 만족도를 높이는 데 중요한 역할을 합니다."

        if df["home_survey"] == 1:
            df["home_survey"] = "좋습니다! 때로는 집에서 적당한 휴식을 취하는 것이 스트레스를 줄이고, 마음의 안정을 가져다주며, 전반적인 건강을 증진시킵니다.😎"
        else:
            df["home_survey"] = "실외 활동은 건강과 활력을 증진시키지만, 집에서 휴식을 취하는 것도 중요합니다. 집에서의 휴식은 몸과 마음을 재충전하는 데 큰 도움이 됩니다.😉"

        context = {"date" : date, "df" : df}
        return render(request, 'survey/plus_result.html', context)
        
    else:
        context = {"date" : date} 
        return render(request, 'survey/plus_survey.html', context)


def plus_result(request, date):
    if request.method == 'POST':
        df = dict()
        save_value = list()
        for key, value in request.POST.items():
            if "survey" in key:
                df[key] = int(value)
                save_value.append(value)
        
        
        user = request.user
        day = date
        dream_survey = df["dream_survey"]
        caffeine_survey = df["caffeine_survey"]
        alcohol_survey = df["alcohol_survey"]
        talk_survey = df["talk_survey"]
        personal_care_survey = df["personal_care_survey"]
        work_survey = df["work_survey"]
        home_survey = df["home_survey"]


        try:
        # 오늘 날짜와 사용자를 기준으로 레코드를 찾습니다.
            PlusPred_instance = PlusPred.objects.get(date=day, user=user)

            # 기존 레코드가 존재하면 업데이트합니다.
            PlusPred_instance.dream_survey = dream_survey
            PlusPred_instance.caffeine_survey = caffeine_survey
            PlusPred_instance.alcohol_survey = alcohol_survey
            PlusPred_instance.talk_survey = talk_survey
            PlusPred_instance.personalcare_survey = personal_care_survey
            PlusPred_instance.work_survey = work_survey
            PlusPred_instance.home_survey = home_survey
            PlusPred_instance.save()

        except PlusPred.DoesNotExist:
            # 오늘 날짜와 사용자에 해당하는 레코드가 없으면 새로운 레코드를 생성합니다.
            PlusPred_instance = PlusPred(
                user=user,
                dream_survey=dream_survey,
                caffeine_survey=caffeine_survey,
                alcohol_survey=alcohol_survey,
                talk_survey=talk_survey,
                personalcare_survey=personal_care_survey,
                work_survey=work_survey,
                home_survey=home_survey,
                date=date
            )
            PlusPred_instance.save()


        if df["dream_survey"] > 2:
            df["dream_survey"] = "악몽을 오랜기간 꾸고 있다면 스트레스로 인해 수면에 어려움이 있을 것으로 예상됩니다."
        else:
            df["dream_survey"] = "꿈을 꾸지 않는 것이 가장 좋다고 할 수 있지만"

        if df["caffeine_survey"] == 2:
            df["caffeine_survey"] ="과한 카페인 심함"
        else:
            df["caffeine_survey"] ="카페인 져아~"

        if df["alcohol_survey"] == 2:
            df["alcohol_survey"] = "과한 알코올 심함"
        else:
            df["alcohol_survey"] = "한잔해~"

        if df["talk_survey"] > 2:
            df["talk_survey"] = "대화많음"
        else:
            df["talk_survey"] = "적당"

        if df["personal_care_survey"] == 1:
            df["personal_care_survey"] = "개인정비최고"
        else:
            df["personal_care_survey"] = "업승ㅁ"

        if df["work_survey"] == 1:
           df["work_survey"] = "퇴근해"
        else:
            df["work_survey"] = "출근해야지~"

        if df["home_survey"] == 1:
            df["home_survey"] = "집 최고임"
        else:
            df["home_survey"] = "하...."
        context = {"df" : df, "date" : date}
    return render(request, 'survey/plus_result.html', context)


