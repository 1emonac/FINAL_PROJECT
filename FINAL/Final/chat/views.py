from django.shortcuts import render, redirect
from chat.forms import RoomForm
from chat.models import Room
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    # .order_by("-pk")를 지정하지 않으면, Room 모델의 디폴트 정렬 옵션이 적용
    room_qs = Room.objects.all()

    return render(request, "chat/index.html", {
        "room_list": room_qs,
    })

def room_chat(request, room_pk):
    if request.user.is_authenticated:
        room = get_object_or_404(Room, pk=room_pk)
        return render(request, "chat/room_chat.html", {
            "room": room,
        })
    else:
        return redirect("users:login") 

def room_new(request):
    if request.user.is_authenticated: # 로그인 되어 있다면
        if request.method == "POST":
            form = RoomForm(request.POST)
            if form.is_valid():
                created_room: Room = form.save(commit=False)
                created_room.owner = request.user
                created_room.save()
                # room pk 기반으로 채팅방 URL을 만듦
                return redirect("chat:room_chat", created_room.pk)
        else:
            form = RoomForm()

        return render(request, "chat/room_form.html", {
            "form": form,
        })
    else:
        return redirect("users:login")


@login_required
def room_delete(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)

    # 권한을 체크하는 방법은 다양하며, 다양한 철학의 라이브러리가 있음
    # 소유자에게만 삭제버튼을 노출하는 것만으로 충분하지 않음. URL을 예상하여 요청이 들어올 수 있음
    # 프론트 단에서의 채킹과 별개로 백엔드 단에서의 권한 체크는 필수
    
    if request.method == "POST":
        room.delete() # HARD DELETE : 데이터베이스에서 삭제
        return redirect("chat:index")

    return render(request, "chat/room_confirm_delete.html", {
        "room": room,
    })
    
@login_required
def room_users(request, room_pk):
    room = get_object_or_404(Room, pk=room_pk)

    if not room.is_joined_user(request.user):
        return HttpResponse("Unauthorized user", status=401)

    username_list = room.get_online_usernames()

    return JsonResponse({
        "username_list": username_list,
    })