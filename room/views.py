from django.shortcuts import render, redirect, HttpResponse
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Room, Topic, Message
from .forms import RoomForm

# Create your views here.
# rooms = [
#     {"id":1, "name": "Python Room"},
#     {"id":2, "name": "Design Room"},
#     {"id":3, "name": "Javascript Room "},
# ]

def index(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    rooms = Room.objects.filter(Q(topic__name__icontains = q) |
                                Q(name__icontains=q)|
                                Q(description__icontains=q))
    topics = Topic.objects.all()[0:4]
    room_messages = Message.objects.filter(Q(room__topic__name__icontains = q))
    # |
                                # Q(name__icontains=q)|
                                # Q(description__icontains=q))
    # room_count = rooms.count()
    context = {
        "rooms": rooms,
        "topics": topics,
        "room_messages": room_messages,
        
        # "room_count": room_count,
    }
    # return render(request, "room/room_index.html", context)
    return render(request, "room/index.html", context)

def room(request, room_id):
    room = Room.objects.get(id = room_id)
    room_messages = room.message_set.all().order_by("-created")
    participants = room.participants.all()
    # for i in rooms:
    #     if i['id'] == int(room_id):
    #         room = i
    if request.method == "POST":
        message = Message.objects.create(
            user = request.user, room = room,
            body = request.POST.get("body")
        )
        room.participants.add(request.user)
        return redirect("room:room", room_id=room.id)
    context = { "room": room, "room_messages": room_messages,
               "participants": participants, }
    return render(request, "room/room.html", context)

def create_room(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == "POST":
        topic_name = request.POST['topic']
        topic, _ = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(host= request.user,
                            topic= topic,
                            name= request.POST.get('name'),
                            description = request.POST.get('description'))
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        return redirect("room:index")
    context = {
        "form": form,
        "topics": topics,
    }
    return render(request, "room/room_form.html", context)

@login_required(login_url="authentification:login")
def updateroom(request, room_id):
    room = Room.objects.get(id = room_id)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("<h2>Oups sorry, You are not allowed here!!</h2>")
    if request.method == "POST":
        topic_name = request.POST['topic']
        topic, _ = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST['name']
        room.description = request.POST['description']
        room.topic = topic
        # form = RoomForm(request.POST, instance=room)
        # if form.is_valid():
        #     form.save()
        room.save()
        return redirect("room:index")
        
    context = {
        # "room": room,
        "form": form,
    }
    return render(request, "room/room_form.html", context)


login_required(login_url="authentification:login")
def deleteRoom(request, room_id):
    page = "room_page"
    room = Room.objects.get(id = room_id)

    if request.user != room.host:
        return HttpResponse("<h2>Oups sorry, You are not allowed here!!</h2>")
    
    if request.method == "POST":
        room.delete()
        return redirect("room:index")

    context = {
        "obj": room,
        "page": page,
    }
    return render(request, "room/delete_room.html", context)




login_required(login_url="authentification:login")
def deleteMessage(request, message_id):
    page = "message_page"

    message = Message.objects.get(id = message_id)

    if request.user != message.user:
        return HttpResponse("<h2>Oups sorry, You are not allowed here!!</h2>")
    
    if request.method == "POST":
        message.delete()
        return redirect("room:index")

    context = {
        "obj": message,
        "page": page

    }
    return render(request, "room/delete_room.html", context)


def topicPage(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    topics = Topic.objects.filter(Q(name__icontains = q)) # |
                                # Q(name__icontains=q)|
                                # Q(description__icontains=q))
    # topics = Topic.objects.filter()
    context ={
        "topics": topics,
    }
    return render(request, "room/topics.html", context)




def activityPage(request):
    room_messages = Message.objects.all().order_by("-created")

    context ={
        "room_messages": room_messages,
    }
    return render(request, "room/activity.html", context)
