# chat/views.py
from django.shortcuts import render,  get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponse
from chat.models import Queue, Username, Message
import random
from mysite.settings import ADJECTIVES, ANIMALS


def chat(request):
    # we will get the chatbox name from the url
    messages = Message.objects.all().order_by('-id').values()[:10]
    print(messages)
    return render(request, "chat/chat.html", {'messages':messages})

def send_message(request, message, user):
    new_message = Message.objects.create(username = user,text = message)
    location = 'http://127.0.0.1:8000/chat/chat/'
    res = HttpResponse(location, status=302)
    res['Location'] = location
    return res
    

def index(request):
    return render(request, "chat/index.html")

def game(request):
    return render(request, "chat/game.html")

def time(request, severity, hospital):
    print(request)
    taken_usernames = Username.objects.values_list('username').all()
    username = random.choice(ADJECTIVES) + random.choice(ANIMALS)
    
    while username in taken_usernames :
        username = random.choice(ADJECTIVES) + random.choice(ANIMALS)
    user = Username.objects.create(username=username)
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
        
    elif severity == 3 :
        spot = queue.yellow
        overall_spot = (queue.blue + queue.red + spot)
        
    elif severity == 4 :
        spot = queue.green
        overall_spot = (queue.blue + queue.red + queue.yellow + spot)
        
    else :
        spot = queue.white
        overall_spot = (queue.blue + queue.red + queue.yellow + queue.green + spot) 
    time = overall_spot * 5

    user.overall_spot = overall_spot
    


    response = render(request, "chat/time.html", {"hospital": hospital, "severity": severity, "time": time})
    response.set_cookie('username', username)
    response.set_cookie('overall_spot', overall_spot)
    response.set_cookie('severity', severity)
    response.set_cookie('hospital', hospital)
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
    patients = Username.objects.filter(severity__gt=severity)
    
    for patient in patients :
        patient.overall_spot += 1
        patient.save()

    return render(request, "chat/qr.html", {"hospital": request.POST['hospital'],"severity": request.POST['severity']})

def treated(request, hospital, overall_spot, severity):

    queue = Queue.objects.get(hospital = hospital)
    if severity == 1 :
        queue.blue -= 1
    elif severity == 2 :
        queue.red -= 1
    elif severity == 3 :
        queue.yellow -= 1
    elif severity == 4 :
        queue.green -= 1
    elif severity == 5 :
        queue.white -= 1
    queue.save()

    patients = Username.objects.filter(overall_spot__lt=overall_spot)
    for patient in patients :
        patient.overall_spot -= 1
        patient.save()
    return render(request)