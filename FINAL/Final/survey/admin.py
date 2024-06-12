from django.contrib import admin
from .models import Pred, PlusPred


class PlusPredAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'dream_survey', 'caffeine_survey', 'alcohol_survey', 'talk_survey', 'personalcare_survey', 'work_survey', 'home_survey')
    search_fields = ('user__username',)  # 사용자명으로 검색 가능하도록 설정
    list_filter = ('date', 'dream_survey', 'caffeine_survey', 'alcohol_survey', 'talk_survey', 'personalcare_survey', 'work_survey', 'home_survey')  # 필터 옵션 추가

class PredAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'date', 'predict', 'predict_proba', 'sleep_survey', 'stress_survey', 'positive_survey')
    search_fields = ('user__username', 'user_username')  # 사용자명으로 검색 가능하도록 설정
    list_filter = ('date', 'predict', 'sleep_survey', 'stress_survey', 'positive_survey')  # 필터 옵션 추가
    ordering = ('date',)  # 최신 날짜가 먼저 나오도록 정렬

admin.site.register(Pred, PredAdmin)
admin.site.register(PlusPred, PlusPredAdmin)

