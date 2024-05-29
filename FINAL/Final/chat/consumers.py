from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from chat.models import Room

# JsonWebsocketConsumer는 receive_json/send_json 메서드를 추가로 지원
class ChatConsumer(JsonWebsocketConsumer):
    # 이제 고정 그룹명을 사용하지 않고, room_name에 기반하여 그룹명을 생성
    # room_name에 상관없이 모든 유저들을 광장(square)을 통해 채팅토록 지원
    # SQUARE_GROUP_NAME = "square"
    # groups = [SQUARE_GROUP_NAME]

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 인스턴스 변수는 생성자 내에서 정의
        self.group_name = "" # 인스턴스 변수 group_name 추가
        self.room = None

    # 웹소켓 클라이언트가 접속을 요청할 때, 호출
    def connect(self):
        # chat/routing.py 내 websocket_urlpatterns에 따라
        # /ws/chat/test/chat/ 요청의 겅우, self.scope["url_route"] 값은
        # => {'args': (), 'kwargs': {room_name': 'test'}}
        
        # asgi.py에서 AuthMiddlewareStack를 적용하지 않았다면 KeyError가 발생
        # AnonymousUser 인스턴스 혹은 User 인스턴스
        user = self.scope["user"]

        if not user.is_authenticated:
            # 인증되지 않은 웹소켓 접속은 거부
            # room_chat 뷰에서 인증 상태에만 렌더링되기에, 인증되지 않은 웹소켓 요청은 있을 수 없음
            # connect에서의 self.close() 호출은 종료코드 1006[비정상 종료]로 강제 전달
            # 다른 메서드에서의 self.close() 호출은 디폴트로 종료 코드 1000[정상 종료]으로 전달
            # 웹프론트엔드 웹소켓 onclsose 핸들러에서 event.code 속성으로 종료코드 참조
            self.close()

        else:
            room_pk = self.scope["url_route"]["kwargs"]["room_pk"]
            # room_name에 기반하여 그룹명 생성
            self.group_name = Room.make_chat_group_name(room_pk=room_pk)

            async_to_sync(self.channel_layer.group_add)(
                self.group_name,
                self.channel_name
            )

            # 본 웹소켓 접속을 허용합
            # connect 메서드 기본 구현에서는 self.accept() 호출부만 있음
            self.accept()

    # 웹소켓 클라이언트와의 접속이 끊겼을 때 호출
    def disconnect(self, code):
        # 소속 그룹에서 빠져나와야함
        if self.group_name:
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name, self.channel_name
            )

        user = self.scope["user"]

        if self.room is not None:
            is_last_leave = self.room.user_leave(self.channel_name, user)
            if is_last_leave:
                async_to_sync(self.channel_layer.group_send)(
                    self.group_name,
                    {
                        "type": "chat.user.leave",
                        "username": user.username,
                    }
                )

    # 단일 클라이언트로부터 메시지를 받으면 호출됩니다,.
    def receive_json(self, content, **kwargs):
        user = self.scope["user"]

        _type = content["type"]

        if _type == "chat.message":
            # message = content["message"]
            sender = user.username
            message = content["message"]

            # Publish 과정: "squeare" 그룹 내 다른 Consumer들에게 메시지를 전달
            # 웹소켓 클라이언트에서는 type="chat.message" 메시지를 받으면 이를 채팅 메시지로 간주하고 채팅 메시지로그에 출력 해줌
            async_to_sync(self.channel_layer.group_send)(
                self.group_name,
                {
                    "type": "chat.message",
                    "message": message,
                    "sender": sender,
                },
            )
        else:
            print(f"Invalid message type : ${_type}")

    # 그룹을 통해 type="chat.mesage" 메시지를 받으면 호출
    def chat_message(self, message_dict):
        # 접속되어 있는 클라이언트에게 메시지를 전달
        # 클라이언트에게 전달하는 값들을 명시적으로 지정
        # 원하는 포멧으로 메시지를 구성
        self.send_json({
            "type": "chat.message",
            "message": message_dict["message"],
            "sender": message_dict["sender"],
        })