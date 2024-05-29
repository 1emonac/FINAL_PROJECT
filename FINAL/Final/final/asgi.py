"""
ASGI config for final project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application

# myproject는 Django 프로젝트 이름
# 웹 서버와 애플리케이션 간의 연결을 설정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# 객체를 사용하여 요청을 Django 애플리케이션으로 전달
application = get_asgi_application()

# import os

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final.settings')

# django_asgi_app = get_asgi_application()

# import app.routing  # noqa: E402
# import chat.routing  # noqa: E402

# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 app.routing.websocket_urlpatterns +
#                 chatting.routing.websocket_urlpatterns
#             )
#         )
#     ),
# })