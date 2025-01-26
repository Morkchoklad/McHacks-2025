# chat/views.py
from django.shortcuts import render,  get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from chat.models import Queue


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
    queue = Queue.objects.filter(hospital = request.POST['hospital'])
    severity = request.POST['severity']
    print(severity)
    if queue :  
        if severity == '1' :
            queue[0].blue += 1
        elif severity == '2' :
            queue[0].red += 1
        elif severity == '3' :
            queue[0].yellow += 1
        elif severity == '4' :
            queue[0].green += 1
        else :
            queue[0].white += 1
        queue[0].save()
    else :
        new_queue = Queue.objects.create(hospital = request.POST['hospital'])
    return render(request, "chat/qr.html", {"hospital": request.POST['hospital'],"severity": request.POST['severity']})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})  
