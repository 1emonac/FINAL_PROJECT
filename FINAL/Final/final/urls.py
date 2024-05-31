"""
URL configuration for final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from final import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("sleep/", include("sleep.urls")),
    path("users/", include("users.urls")),
    path("chat/", include("chat.urls")),
    path("dr/", include("dr.urls")),
    # 최상위 주소로 요청이 들어오면, chat:index 패턴의 주소로 페이지 이동하도록 RedirectView를 지정
    # 즉, / 주소로 요청이 들어오면 /chat/ 주소로 이동
    path('', RedirectView.as_view(pattern_name="chat:index"), name="root"),
    path("polls/", include("polls.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)