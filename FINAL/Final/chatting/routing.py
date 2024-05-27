from django.urls import path
from . import consumers

# 장고의 urls urlpatterns와 유사한 역할 (URL에 매핑)
# 장고 기본의 urls.py urlpatterns 와 다르게 이는 장고에서 찾아서 읽어가는 것이 아니라, 우리가 asgi.py 직접 임포트 하여 지정함
# 그래서 이름이 달라도 상관이 없음!
websocket_urlpatterns = [
    path("ws/chat/", consumers.EchoConsumer.as_asgi()),
]