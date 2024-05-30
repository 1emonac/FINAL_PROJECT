from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from users.forms import *
from .models import *

from api import address
from private_file import key
import json
from django.http import JsonResponse

import geocoder

# Create your views here.
# video.html
def video(request):    
    return render(request, "main/videomain.html")

def main(request):    
    return render(request, "main/main.html")

def define(request):    
    return render(request, "feed/define.html")

def chatbot(request):    
    return render(request, "feed/chatbot.html")

def result(request):    
    return render(request, "feed/result.html")

def team(request):    
    return render(request, "business/team.html")

# map.html
def map(request):
    data = address.search()

    if request.method == "POST":
        fetchData = json.loads(request.body)
        x = fetchData["x"]
        y = fetchData["y"]
        sleep_clinic = address.searchGeo(x,y,"정신과")
        return JsonResponse({"sleep_clinic": sleep_clinic,})
    
    context = {
        "map_key" : "0e03efef5a20230c182645bf000aa33c",
        "data" : json.dumps(data), 
        "sleep_clinic" : "수면클리닉"
    }
    return render(request, "feed/mapping.html", context)