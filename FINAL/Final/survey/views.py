from django.shortcuts import render, redirect
import random
from .models import Question, Choice

from django.utils import timezone
from .models import Question, Choice, Response
import random
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.core.paginator import Paginator

def start_survey(request):
    if request.method == "POST":
        user_id = request.user.id
        question_id = request.POST.get('question_id')
        question = Question.objects.get(pk=question_id)
        choices_ids = request.POST.getlist('response')

        if question.question_type == 'text':
            text_response = request.POST.get('response', '')
            Response.objects.create(question=question, user_id=user_id, text_response=text_response)
        elif choices_ids:
            response = Response.objects.create(question=question, user_id=user_id)
            response.choice_responses.set(Choice.objects.filter(id__in=choices_ids))
        
        current_index = request.session.get('current_index', 0)
        questions_ids = request.session.get('questions_ids', [])
        if current_index < len(questions_ids) - 1:
            request.session['current_index'] = current_index + 1
            next_question_id = questions_ids[current_index + 1]
            next_question = Question.objects.get(pk=next_question_id)
            return render(request, 'survey/survey.html', {'question': next_question})
        else:
            return render(request, 'survey/survey.html')
    else:
        questions_ids = list(Question.objects.order_by('id').values_list('id', flat=True))
        request.session['questions_ids'] = questions_ids
        request.session['current_index'] = 0
        if questions_ids:
            first_question_id = questions_ids[0]
            first_question = Question.objects.get(pk=first_question_id)
            return render(request, 'survey/survey.html', {'question': first_question})
        else:
            return render(request, 'survey/survey.html')


    
def create_survey_questions():
    # 질문과 선택지 생성
    questions_and_choices = [
        ("당신의 키는 얼마입니까?", [], "text"),
        ("당신의 몸무게는 얼마입니까?", [], "text"),
        ("어제 잠은 잘 주무셨나요?", ["네", "아니요"], "choice"),
        ("어제 몇 시에 주무셨나요?  (0시부터 23시까지 적어주세요)", [], "text"),
        ("어제 총 몇 시간 정도 주무셨나요?", [], "text"),
        ("수면 중에 문제가 있으셨나요?", ["잠 드는 데 30분 이상 걸림", "밤에 또는 예정된 기상 시간 전에 깨어남", "화장실에 가기 위해 밤에 깨어남", "큰 코골이 또는 질식으로 인해 깨어남", "낮은 온도로 인해 방해받음", "높은 온도로 인해 방해받음", "악몽을 꿈", "통증으로 인해 방해받음", "위에 나열되지 않은 다른 이유로 방해받음", "문제 없었음"], "choice"),
        ("일어나서 상쾌함을 느끼셨나요?", ["전혀 상쾌하지 않음", "거의 상쾌하지 않음", "보통", "꽤 상쾌함", "매우 상쾌함"], "choice"),
        ("일어난 후 기분이 어떠셨나요?", ["매우 불쾌함", "불쾌함", "보통", "기분 좋음", "매우 기분 좋음"], "choice"),
        ("꿈을 꾸셨나요? 꾸셨다면 어떤 유형의 꿈이었나요?", ["악몽", "중립적인 꿈", "좋은 꿈", "꿈을 꾸지 않음"], "choice"),
        ("자기 전 기분은 어떠셨나요?", ["매우 불쾌함", "불쾌함", "보통", "기분 좋음", "매우 기분 좋음"], "choice"),
        ("전 날 얼마나 스트레스를 받았나요?", ["매우 많이", "꽤 많이", "평소와 같음", "별로 안 받음", "전혀 안 받음"], "choice"),
        ("자기 전 얼마나 피곤하셨나요?", ["매우 많이", "꽤 많이", "평소와 같음", "별로 안 피곤함", "전혀 안 피곤함"], "choice"),
        ("어제 하루 평균적으로 얼마나 긴장하셨나요?", ["1", "2", "3", "4", "5", "6", "7"], "choice"),
        ("어제 하루 긍정적이었나요?", ["1", "2", "3", "4", "5", "6", "7"], "choice"),
        ("전 날 카페인이 든 음료를 섭취하셨나요?", ["커피", "에너지드링크", "그 외", "마시지 않음"], "choice"),
        ("음료 드셨다면 얼마나 드셨나요?", ["평균(500ml~1L)", "평균 이상(1L 이상)", "마시지 않음"], "choice"),
        ("전 날 술을 드셨나요?", ["마셨다", "마시지 않았다"], "choice"),
        ("술을 마셨다면 얼마나 드셨나요?", ["소주 1 ~ 3병", "맥주 1 ~ 2캔", "그 이상", "마시지 않음"], "choice"),
        ("전 날 낮잠은 주무셨나요?", ["30분 ~ 1시간 정도 잤다", "1시간 이상 잤다", "낮잠을 자지 않았다"], "choice"),
        ("전 날 많은 시간을 누구와 보내셨나요?", ["혼자 보낸 시간이 많다", "다른 사람들과 많은 시간을 보냈다"], "choice"),
        ("전 날 대화는 많이 나누셨나요?", ["대화를 적극적으로 대화를 많이 나눴다", "적당히 대화를 나눴다", "적은 양의 대화를 주고 받았다", "화를 하지 않았다"], "choice"),
        ("전 날 많은 시간을 어디서 보내셨나요?", ["집", "직장", "그 외"], "choice"),
        ("전 날 가장 많은 시간을 어떻게 보내셨나요? (중복 선택 가능)", ["일 혹은 공부", "개인 관리(쇼핑 포함)", "집안일", "취미(야외 활동 및 스포츠 포함)", "여가활동(자원봉사 혹은 파티 참여 등 포함)"], "multiple"),
        ("전 날 식사는 하셨나요?(중복 선택 가능)", ["아침", "점심", "저녁", "야식", "밥을 먹지 않았다"], "multiple"),
    ]

    for text, choices, q_type in questions_and_choices:
        q = Question(text=text, question_type=q_type)
        q.save()
        for choice in choices:
            Choice(question=q, choice_text=choice).save()

def store_response(question_id, user_id, text_response=None, choice_id=None):
    question = Question.objects.get(pk=question_id)
    if question.question_type == 'text':
        Response(question=question, user_id=user_id, text_response=text_response).save()
    elif question.question_type == 'choice':
        choice = Choice.objects.get(pk=choice_id)
        Response(question=question, user_id=user_id, choice_response=choice).save()

def view_results(request):
    user_id = request.user.id
    responses = Response.objects.filter(user_id=user_id)
    return render(request, 'survey/result.html', {'responses': responses})


def sleep_results(request):
    user_id = request.user.id
    responses = Response.objects.filter(user_id=user_id)
    paginator = Paginator(responses, 24)  # 페이지당 5개의 응답
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': request.user,
        'page_obj': page_obj,
        'responses': responses
    }
    return render(request, 'survey/result.html', context)
