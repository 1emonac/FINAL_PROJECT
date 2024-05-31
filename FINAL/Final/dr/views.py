from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import DetailView

from .models import SleepClinicRoom

FIXED_ROOM_PK = 1  # 고정된 방의 Primary Key

# @method_decorator(staff_member_required, name="dispatch")
class SleepClinicRoomDetailView(DetailView):
    model = SleepClinicRoom

    def get_object(self):
        return get_object_or_404(SleepClinicRoom, pk=FIXED_ROOM_PK)

sleep_clinic_room_detail = SleepClinicRoomDetailView.as_view()
