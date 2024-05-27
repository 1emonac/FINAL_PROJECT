import channels
from channels.generic.websocket import WebsocketConsumer
import json

class EchoConsumer(WebsocketConsumer):
    # 웹소켓 클라이언트에서
    # text frame 으로 보내면 text_data 인자에 담아지고
    # binary data frame 으로 보내면 bytes_data 인자에 값이 담겨져 호출
    def receive(self, text_data=None, bytes_data=None):
        # self.send(f"You said: {text_data}")
        # "You said":는 json 문자열을 오염시키기에 제거
        obj = json.loads(text_data) # 문자열 -> 객체로 역직렬화
        print("수신 :", obj)

        # json_string: str = json.dumps(obj) # 객체를 문자열로 직렬화
        # self.send(json_string)

        json_string = json.dumps({
            "content": obj["content"],
            "user": obj["user"],
        })
        self.send(json_string)



    # text frame 전송: 문자열 타입
    # 장고 채널스 Consumer receive 호출 시에 text_data 인자에 담겨집니다.

    # binary data frame 전송: 이미지 등
    # - 보낼 때는 blob 타입 또는 ArrayBuffer 타입으로 전송 가능
    # - 받일 때는 ws.binaryType 속성값으로 포맷 결정 : 디폴트 "blob" (또는 "arrayBuffer")
    # ex) let blob = new Blob(["hello world"], {type: 'text/plain});
    #     ws.send(blob);
    # 장고 채널스 Consumer receive 호출 시에 bytes_data 인자에 담겨짐

