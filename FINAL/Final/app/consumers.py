import channels
from channels.generic.websocket import JsonWebsocketConsumer
import json
from asgiref.sync import async_to_sync

# 모든 Consumer 클래스의 부모 클래스인 AsyncConsumer를 통해 self.channel_layer = get_channel_layer() 가 자동으로 수행
# settings.CHANNEL_LAYERS 설정이 없다면, self.chaeenl_layer 같은 None

class EchoConsumer(JsonWebsocketConsumer):
    # 웹소켓 클라이언트에서
    # text frame 으로 보내면 text_data 인자에 담아지고
    # binary data frame 으로 보내면 bytes_data 인자에 값이 담겨져 호출
    def receive_json(self, content, **kwargs):
        # self.send(f"You said: {text_data}")
        # "You said":는 json 문자열을 오염시키기에 제거
        print("수신 :", content)

        # json_string: str = json.dumps(obj) # 객체를 문자열로 직렬화
        # self.send(json_string)
        self.send_json({
            "content": content["content"],
            "user": content["user"],
        })

# 정적으로 소솔될 그룹이 정해져있을 경우의 패턴
# - 클래스 변수 groups에 채널레이어 그룹명을 지정
# - 웹소켓 연결/끊김 시에 자동으로 그룹 add/discard를 수행
class LiveblogConsumer(JsonWebsocketConsumer):
    # 메시지를 받을 그룹을 암시
    # 매번 LiveblogConsumer 인스턴스에서 웹소켓 연결이 맺어지고, 
    # 끊어질 때, 자동으로 grouo_add와 group_discard가 수행
    groups = ["liveblog"]

    # def connect(self):
    #     self.channel_layer

    # # 채널 레이어를 통해 type="greeting"메시지를 받으면 자동 호출
    # def greeting(self, message_dict):
    #     print(message_dict)

    # 그룹을 통해 받은 메시지를 그대로 웹소켓 클라이언트에게 전달 (self.send(전달할_메시지))
    # 메시지의 type 값과 같은 이름의 메서드가 호출

    # ex) type "liveblog.post.created" -> "liveblog_post_creatred" 메서드 호출 -> 마침표를 언더바로 바꿈
    def liveblog_post_created(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_updated(self, event_dict):
        self.send_json(event_dict)

    def liveblog_post_deleted(self, event_dict):
        self.send_json(event_dict)
    # 채널레이어 그룹으로부터 받는 메시지를 통해 호출되는 메서드들은 호출 시에 수신한 메시지를 첫번째 인자로 받음
    # 그 메시지를 JSON 직렬화하여 웹소켓 클라이언트로 즉시 전달

# 웹 클라이언트와 연결 시점에 소솔될 그룹이 정해질 경우의 패턴
# - 웹 소켓 연결/끊김 시에 수동으로 그룹 add/discoard를 수행
# class LiveblogConsumer(WebsocketConsumer):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.group_name = ""

#     def connect(self):
#         # /ws/chat/django/chat/ 요청일 경우 => room_name이 "django"가 되도록 urlpatterns에 미리 설정된 경우
#         room_name = self.scope["url_route"]["kwargs"]["room_name"]

#         self.group_name = f"chat-{room_name}"
#         # channel_layer의 모든 메서드는 비동기(async)함수
#         # async_to_sync을 통해 동기 함수로 래핑하여 호출
#         async_to_sync(self.channel_layer.group_add)(
#             self.group_name,
#             # 모든 Consumer 클래스의 부모인 AsyncConsumer에서
#             # self.channel_name에 채널명을 랜덤으로 결정하여 자동 지정
#             self.channel_name
#         )

#         self.accept()

    # def disconnect(self, close_code):

    # text frame 전송: 문자열 타입
    # 장고 채널스 Consumer receive 호출 시에 text_data 인자에 담겨집니다.

    # binary data frame 전송: 이미지 등
    # - 보낼 때는 blob 타입 또는 ArrayBuffer 타입으로 전송 가능
    # - 받일 때는 ws.binaryType 속성값으로 포맷 결정 : 디폴트 "blob" (또는 "arrayBuffer")
    # ex) let blob = new Blob(["hello world"], {type: 'text/plain});
    #     ws.send(blob);
    # 장고 채널스 Consumer receive 호출 시에 bytes_data 인자에 담겨짐