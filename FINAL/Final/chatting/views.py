from django.shortcuts import render

# Create your views here.
def chat_page(request):
    return render(request, "feed/chatting.html")