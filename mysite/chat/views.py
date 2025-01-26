# chat/views.py
from django.shortcuts import render,  get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from chat.models import Queue, Username
import random
from mysite.settings import ADJECTIVES, ANIMALS


def chat_box(request, chat_box_name):
    # we will get the chatbox name from the url
    return render(request, "chatbox.html", {"chat_box_name": chat_box_name})

def index(request):
    return render(request, "chat/index.html")

def game(request):
    return render(request, "chat/game.html")

def time(request, severity, hospital):

    taken_usernames = Username.objects.values_list('username').all()
    username = random.choice(ADJECTIVES) + random.choice(ANIMALS)
    
    while username in taken_usernames :
        username = random.choice(ADJECTIVES) + random.choice(ANIMALS)
    Username.objects.create(username=username)
    overall_spot = 0
    time = 0
    queue = Queue.objects.get(hospital = hospital)
    if severity == 1 :
        spot = queue.blue
        overall_spot = spot
        time = spot*5
    elif severity == 2 :
        spot = queue.red
        overall_spot = (queue.blue + spot)
        time = overall_spot * 5
    elif severity == 3 :
        spot = queue.yellow
        overall_spot = (queue.blue + queue.red + spot)
        time = overall_spot * 5
    elif severity == 4 :
        spot = queue.green
        overall_spot = (queue.blue + queue.red + queue.yellow + spot)
        time = overall_spot * 5
    else :
        spot = queue.white
        overall_spot = (queue.blue + queue.red + queue.yellow + queue.green + spot) 
        time = overall_spot * 5

    


    response = render(request, "chat/time.html", {"hospital": hospital, "severity": severity, "time": time})
    response.set_cookie('username', username)
    response.set_cookie('spot', spot)
    response.set_cookie('severity', severity)
    return response

def admin(request):
    return render(request, "chat/admin.html")

@csrf_exempt
def qr(request):
    queue = Queue.objects.filter(hospital = request.POST['hospital'])
    severity = request.POST['severity']
    

    if not queue :  
        new_queue = Queue.objects.create(hospital = request.POST['hospital'])

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
 
    return render(request, "chat/qr.html", {"hospital": request.POST['hospital'],"severity": request.POST['severity']})


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})  
