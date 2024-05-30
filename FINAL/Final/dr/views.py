
from django.views.generic import TemplateView

class ChatView(TemplateView):
    template_name: str = "dr/dr_chat.html"