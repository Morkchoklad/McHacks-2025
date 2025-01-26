# chat/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse


def index(request):
    return render(request, "chat/index.html")

def game(request):
    return render(request, "chat/game.html")

def time(request, severity, hospital):
    return render(request, "chat/time.html", {"hospital": hospital, "severity": severity})

def admin(request):
    return render(request, "chat/admin.html")

@csrf_exempt
def qr(request):
    return render(request, "chat/qr.html", {"hospital": request.POST['hospital'],"severity": request.POST['severity']})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})  
